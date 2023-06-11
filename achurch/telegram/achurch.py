from __future__ import annotations
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from telegram import __version__ as TG_VER
import uuid
import pydot
import logging
from dataclasses import dataclass
import string

from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor


@dataclass
class Variable:
    name: str


@dataclass
class NAbstraction:
    variable: str
    body: Term


@dataclass
class NApplication:
    function: Term
    argument: Term


Term = Variable | NAbstraction | NApplication


class TreeVisitor(lcVisitor):
    def __init__(self, macros_usuari):
        self.macros = macros_usuari

    def visitVariable(self, ctx):
        [var] = list(ctx.getChildren())
        return Variable(var.getText())

    def visitTermeParentitzat(self, ctx):
        [p1, ter, p2] = list(ctx.getChildren())
        return self.visit(ter)

    def visitMacroInfija(self, ctx):
        [terme1, ID, terme2] = list(ctx.getChildren())
        return NApplication(NApplication(
            self.macros[str(ID)], self.visit(terme1)), self.visit(terme2))

    def visitAbstraccio(self, ctx):
        [op1, vars, op2, terme] = list(ctx.getChildren())
        t = self.visit(terme)
        for c in reversed(self.visit(vars)):
            t = NAbstraction(c, t)
        return t

    def visitVariables(self, ctx):
        vars = list(ctx.getChildren())
        return ''.join([var.getText() for var in vars])

    def visitMacro(self, ctx):
        [ID] = list(ctx.getChildren())
        return self.macros[str(ID)]

    def visitAplicacio(self, ctx):
        [function, argument] = list(ctx.getChildren())
        return NApplication(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)

    def visitAssignacio1(self, ctx):
        [m, eq, terme] = list(ctx.getChildren())
        self.macros[str(m)] = self.visit(terme)
        return 0

    def returnMacros(self):
        return self.macros


def show(t: Term) -> string:
    match t:

        case Variable(name):
            return name
        
        case NAbstraction(var, term):
            return "(" + "λ" + var + "." + show(term) + ")"
        
        case NApplication(function, argument):
            return "(" + show(function) + show(argument) + ")"


async def evaluate_term(term: Term, max_reductions: int, verbose: bool, update: Update) -> Term:

    # it generates a new variable for a particular term
    def generate_new_variable_name(existing_variables: set[str]) -> str:
        alphabet = string.ascii_lowercase

        for char in alphabet:
            if char not in existing_variables:
                return char

        raise ValueError("Cannot generate any new variables")

    # gives a set of all variables within a term
    def get_variables(term: Term) -> set[str]:
        variables = set()

        if isinstance(term, Variable):
            variables.add(term.name)

        elif isinstance(term, NAbstraction):
            variables.add(term.variable)
            variables.update(get_variables(term.body))

        elif isinstance(term, NApplication):
            variables.update(get_variables(term.function))
            variables.update(get_variables(term.argument))

        return variables

    # replaces old_variable with new_variable in a term generally
    def replace_alfa(t: Term, old_variable: str, new_variable: str) -> Term:
        match t:

            case Variable(name):
                if name == old_variable:
                    return Variable(new_variable)
                return t

            case NAbstraction(var, body):
                if var == old_variable:
                    var = new_variable
                body = replace_alfa(body, old_variable, new_variable)
                return NAbstraction(var, body)

            case NApplication(function, argument):
                function = replace_alfa(function, old_variable, new_variable)
                argument = replace_alfa(argument, old_variable, new_variable)
                return NApplication(function, argument)

    def alfas_rec(term: Term, used_vars, variables_to_replace, var_original) -> Term:
        match term:

            case NAbstraction(var, body):
                # if we need to preform an alpha conversion we do so
                if var in variables_to_replace and var_original in get_variables(body):
                    new_variable = generate_new_variable_name(used_vars)

                    new_body = replace_alfa(body, var, new_variable)

                    used_vars.add(new_variable)
                    new_body2 = alfas_rec(new_body, used_vars, variables_to_replace, var_original)
                    return NAbstraction(new_variable, new_body2)

                new_body = alfas_rec(body, used_vars, variables_to_replace, var_original)
                return NAbstraction(var, new_body)

            case NApplication(function, argument):

                new_function = alfas_rec(function, used_vars, variables_to_replace, var_original)
                new_argument = alfas_rec(argument, used_vars, variables_to_replace, var_original)
                return NApplication(new_function, new_argument)

        return term

    async def do_needed_alfas(term: Term, used_vars, verbose: bool, update: Update) -> Term:

        variables_to_replace = get_variables(term.argument)

        if term.function.variable in variables_to_replace:
            variables_to_replace.remove(term.function.variable)

        new_body = alfas_rec(term.function.body,
                             used_vars,
                             variables_to_replace,
                             term.function.variable)

        if new_body != term.function.body:
            if verbose:
                await update.message.reply_text(show(term.function) + " →α→ " + show(NAbstraction(term.function.variable, new_body)))
            return NApplication(NAbstraction(term.function.variable, new_body), term.argument)

        return term

    def replace_beta(term: Term, substitutions: dict) -> Term:
        match term:

            case Variable(name):
                if name in substitutions:
                    return substitutions[term.name]
                return term
            
            case NAbstraction(variable, body):
                new_substitutions = {
                    key: value for key,
                    value in substitutions.items()}
                new_substitutions.pop(variable, None)
                new_body = replace_beta(body, new_substitutions)
                return NAbstraction(variable, new_body)
            
            case NApplication(function, argument):
                new_function = replace_beta(function, substitutions)
                new_argument = replace_beta(argument, substitutions)
                return NApplication(new_function, new_argument)

    async def evaluate_a_beta(term: Term, used_vars: set, verbose: bool, update: Update) -> Term:
        match term:

            case Variable(var):
                return term, False

            case NAbstraction(var, body):
                new_body, modif = await evaluate_a_beta(body, used_vars, verbose, update)
                return NAbstraction(var, new_body), modif

            case NApplication(function, argument):

                if isinstance(term.function, NAbstraction):

                    alfa_term = await do_needed_alfas(term, used_vars, verbose, update)

                    new_term = replace_beta(alfa_term.function.body, 
                                            {alfa_term.function.variable: argument})

                    if verbose:
                        await update.message.reply_text(show(alfa_term) + " →β→ " + show(new_term))

                    return new_term, True

                else:

                    new_function, modif = await evaluate_a_beta(function, used_vars, verbose, update)
                    if modif:
                        return NApplication(new_function, argument), modif

                    new_argument, modif = await evaluate_a_beta(argument, used_vars, verbose, update)
                    return NApplication(function, new_argument), modif

        return term

    for i in range(0, max_reductions):
        set_used_vars = get_variables(term)
        new_term, modif = await evaluate_a_beta(term, set_used_vars, verbose, update)
        if not modif:
            return new_term
        term = new_term

    return 0

# a partir de aqui todo telegram ----------------------------------------
# basado en el ejemplo: 
# https://docs.python-telegram-bot.org/en/stable/examples.echobot.html

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
logger = logging.getLogger(__name__)


async def show_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = update.effective_user

    context.user_data["macros_user"] = {}

    context.user_data["max_steps"] = 20

    context.user_data["verbose"] = True

    await update.message.reply_html(

        rf"Hi {user.mention_html()} I'm Hugo's AChurch Bot!",

        reply_markup=ForceReply(selective=True),

    )


async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("/start \n/author \n/help \n/macros \n/maxsteps \n/setsteps <NUM_STEPS> \n/showsteps " 
                                    + "\n/hidesteps \nLambda Calculus Expression to eval \nMACRO = Lambda Calculus Expression")


async def show_author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("AChurchBot! \n@ Hugo Aranda Sanchez, 2023")


async def show_macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    macros = context.user_data.get("macros_user")

    if macros:

        output = ""
        for key, var in macros.items():
            output = output + key + " ≡ " + show(var) + "\n"
        await update.message.reply_text(output)

    else:

        await update.message.reply_text("No macros defined, define macros with: \n\"MACROINCAPS\" (=|≡) expression")

async def show_maxsteps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    max = context.user_data.get("max_steps")
    await update.message.reply_text("The maximum number of steps is " + str(max))

async def setmaxsteps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    max = context.args[0]
    context.user_data["max_steps"] = int(max)
    await update.message.reply_text("The maximum number of steps has been modified to " + max)

async def showsteps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    context.user_data["verbose"] = True
    await update.message.reply_text("Now we will show middle steps")

async def hidesteps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    context.user_data["verbose"] = False
    await update.message.reply_text("Now we will hide middle steps")


def makeGraph(t: Term, graph, bounded):

    match t:

        case Variable(v):
            node = pydot.Node(name=str(uuid.uuid1()),
                              label=v,
                              shape="plaintext")
            graph.add_node(node)

            # I add the bounded variables dashed lines
            if v in bounded:
                edge = pydot.Edge(node, bounded[v])
                edge.set_style("dashed")
                graph.add_edge(edge)

            return node

        case NApplication(function, argument):

            node = pydot.Node(name=str(uuid.uuid1()),
                              label='@',
                              shape="plaintext")
            graph.add_node(node)

            secure = bounded
            func_node = makeGraph(function, graph, bounded)
            graph.add_edge(pydot.Edge(node, func_node))

            bounded = secure
            arg_node = makeGraph(argument, graph, bounded)
            graph.add_edge(pydot.Edge(node, arg_node))

            return node

        case NAbstraction(var, body):

            node = pydot.Node(name=str(uuid.uuid1()),
                              label="λ" + var,
                              shape="plaintext")
            graph.add_node(node)

            bounded[var] = node

            child_node = makeGraph(body, graph, bounded)
            graph.add_edge(pydot.Edge(node, child_node))

            return node


async def outputGraph(t: Term, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    graph = pydot.Dot(graph_type='digraph')
    makeGraph(t, graph, dict())
    graph.write_png('graph.png')
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('graph.png', 'rb'))


async def evaluate_expression(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    input_text = update.message.text
    input_stream = InputStream(input_text)
    visitor = TreeVisitor(context.user_data.get("macros_user"))
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()

    expresion = visitor.visit(tree)

    if expresion:

        await update.message.reply_text(show(expresion))

        await outputGraph(expresion, update, context)

        max_reductions = context.user_data.get("max_steps")

        await update.message.reply_text("beggining evaluation...")

        verbose = context.user_data.get("verbose")

        evaluated_expression = await evaluate_term(expresion, max_reductions, verbose, update)

        await update.message.reply_text("evaluation complete!")

        if evaluated_expression:

            await update.message.reply_text(show(evaluated_expression))

            await outputGraph(evaluated_expression, update, context)

        else:
            await update.message.reply_text("Nothing, cannot be computed on " + str(max_reductions) + " steps")


def main() -> None:
    #el username que responde a este token es @AChurch_HugoBot
    application = Application.builder().token("6021919629:AAESJhrndta0eAlPLRMw1ehumFnq7NQ5A6M").build()

    application.add_handler(CommandHandler('start', show_start))
    application.add_handler(CommandHandler('help', show_help))
    application.add_handler(CommandHandler('author', show_author))
    application.add_handler(CommandHandler('macros', show_macros))
    application.add_handler(CommandHandler('maxsteps', show_maxsteps))
    application.add_handler(CommandHandler('setsteps', setmaxsteps))
    application.add_handler(CommandHandler('showsteps', showsteps))
    application.add_handler(CommandHandler('hidesteps', hidesteps))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, evaluate_expression))

    application.run_polling(1.0)


if __name__ == "__main__":

    main()