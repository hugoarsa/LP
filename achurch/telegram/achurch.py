from __future__ import annotations
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
class Abstraction:
    variable: str
    body: Term

@dataclass
class NApplication:
    function: Term
    argument: Term

Term = Variable | Abstraction | NApplication

class TreeVisitor(lcVisitor):
    def __init__(self, macros_usuari):
        self.macros = macros_usuari

    def visitVariable(self, ctx):
        [var] = list(ctx.getChildren())
        return Variable(var.getText())

    def visitTermeParentitzat(self, ctx):
        [p1,ter,p2] = list(ctx.getChildren())
        return self.visit(ter)
    
    def visitMacroInfija(self, ctx):
        [terme1,ID,terme2] = list(ctx.getChildren())
        return NApplication(NApplication(self.macros[str(ID)],self.visit(terme1)),self.visit(terme2))

    def visitAbstraccio(self, ctx):
        [op1, vars, op2, terme] = list(ctx.getChildren())

        t = self.visit(terme)
        for c in reversed(self.visit(vars)):
            t = Abstraction(c, t)
        return t

    def visitVariables(self, ctx):
        vars = list(ctx.getChildren())
        return ''.join([var.getText() for var in vars])
    
    def visitMacro(self, ctx):
        [ID] = list(ctx.getChildren())
        return self.macros[str(ID)]

    def visitAplicacio(self, ctx):
        [function,argument] = list(ctx.getChildren())
        return NApplication(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)
    
    def visitAssignacio1(self, ctx):  
        [m, eq, terme] = list (ctx.getChildren())
        self.macros[str(m)] = self.visit(terme)
        return 0
    
    def returnMacros(self):  
        return self.macros

def show(t: Term) -> string:
    match t:
        case Variable(name):
            return name
        
        case Abstraction(var,term):
            return "(" + "λ" + var + "." + show(term) + ")"
        
        case NApplication(function,argument):
            return "(" + show(function) + show(argument) + ")"
        
async def evaluate_term(term: Term, max_reductions: int, update: Update) -> Term:

    #genera una nueva variable la cual no este presente en el termino     
    def generate_new_variable_name(term: Term) -> str:
        existing_variables = get_variables(term)
        alphabet = string.ascii_lowercase

        for char in alphabet:
            if char not in existing_variables:
                return char

        raise ValueError("No se pudo generar un nuevo nombre de variable.")

    #da un set de todas las variables que se encuentran en un termino
    def get_variables(term: Term) -> set[str]:
        variables = set()
        if isinstance(term, Variable):
            variables.add(term.name)
        elif isinstance(term, Abstraction):
            variables.add(term.variable)
            variables.update(get_variables(term.body))
        elif isinstance(term, NApplication):
            variables.update(get_variables(term.function))
            variables.update(get_variables(term.argument))
        return variables

    #esta funcion toma un termino, una variable a reemplazar y una nueva variable propuesta
    def replace_alfa(t: Term, old_variable: str, new_variable: str) -> Term:
        match t:

            case Variable(name):

                if name == old_variable:
                    return Variable(new_variable)
                
                return t
            
            case Abstraction(var,body):

                if var == old_variable:
                    var = new_variable

                body = replace_alfa(body,old_variable,new_variable)
                return Abstraction(var,body)
            
            case NApplication(function,argument):

                function = replace_alfa(function, old_variable, new_variable)
                argument = replace_alfa(argument, old_variable, new_variable)
                return NApplication(function,argument)
            
    def alfas_rec(term: Term, variables_to_replace, var_original) -> Term:
        match term:

            case Abstraction(var,body):

                if var in variables_to_replace and var_original in get_variables(body):   
                    new_variable = generate_new_variable_name(body)

                    new_body = replace_alfa(body,var,new_variable)
                    return Abstraction(new_variable,new_body)
                
                new_body = alfas_rec(body, variables_to_replace, var_original)
                return Abstraction(var,new_body)
            
            case NApplication(function,argument):

                new_function = alfas_rec(function, variables_to_replace, var_original)
                new_argument = alfas_rec(argument, variables_to_replace, var_original)
                return NApplication(new_function,new_argument)
        
        return term
    
    async def do_needed_alfas(term: Term, update: Update) -> Term:

        variables_to_replace = get_variables(term.argument)

        if term.function.variable in variables_to_replace:
            variables_to_replace.remove(term.function.variable)

        new_body = alfas_rec(term.function.body, variables_to_replace, term.function.variable)

        if new_body != term.function.body:

            await update.message.reply_text(show(term.function) + " →α→ " + show(Abstraction(term.function.variable,new_body)))
            
            return NApplication(Abstraction(term.function.variable,new_body),term.argument)
        
        return term
    
    def replace_beta(term: Term, substitutions: dict) -> Term:
        match term:
            case Variable(name):
                if name in substitutions:
                    return substitutions[term.name]
                return term
            case Abstraction(variable,body):
                new_substitutions = {key: value for key, value in substitutions.items()}
                new_substitutions.pop(variable, None)
                new_body = replace_beta(body, new_substitutions)
                return Abstraction(variable, new_body)
            case NApplication(function,argument):
                new_function = replace_beta(function, substitutions)
                new_argument = replace_beta(argument, substitutions)
                return NApplication(new_function, new_argument)


    async def evaluate_a_beta(term: Term, update: Update) -> Term:
        match term:

            case Variable(var):
                return term, False
            
            case Abstraction(var,body):
                new_body, modif = await evaluate_a_beta(body, update)
                return Abstraction(var, new_body), modif
            
            case NApplication(function,argument):

                if isinstance(term.function, Abstraction):

                    alfa_term = await do_needed_alfas(term, update)

                    new_term = replace_beta(alfa_term.function.body, {alfa_term.function.variable: argument})

                    await update.message.reply_text(show(alfa_term) + " →β→ " + show(new_term))

                    return new_term, True
                
                else:

                    new_function, modif = await evaluate_a_beta(function, update)
                    if modif:
                        return NApplication(new_function, argument), modif

                    new_argument, modif = await evaluate_a_beta(argument, update)
                    return NApplication(function, new_argument), modif
                
        return term
    
    
    for i in range(1,max_reductions):
        new_term, modif = await evaluate_a_beta(term, update)
        if not modif:
            return new_term
        term = new_term

    return 0

#cosas de telegram ------------------------------------------------------------------------------------
import logging
import pydot
import uuid
from telegram import __version__ as TG_VER
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def show_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user = update.effective_user

    context.user_data["macros_user"] = {}

    await update.message.reply_html(

        rf"Hi {user.mention_html()} I'm Hugo's AChurch Bot!",

        reply_markup=ForceReply(selective=True),

    )

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("/start \n/author \n/help \n/macros \nLambda Calculus Expression to eval \nMACRO = Lambda Calculus Expression")

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

def makeGraph(t:Term,graph,lligades,):
    match t:
        case Variable(v):
            node = pydot.Node(name=str(uuid.uuid1()),label=v,shape="plaintext")
            graph.add_node(node)

            if v in lligades:
                edge = pydot.Edge(node, lligades[v])
                edge.set_style("dashed")
                graph.add_edge(edge)

            return node

        case NApplication(function,argument):

            node = pydot.Node(name=str(uuid.uuid1()), label='@', shape="plaintext")
            graph.add_node(node)

            secure = lligades
            func_node = makeGraph(function,graph,lligades)
            graph.add_edge(pydot.Edge(node,func_node))

            lligades = secure
            arg_node = makeGraph(argument,graph,lligades)
            graph.add_edge(pydot.Edge(node,arg_node))

            return node
        
        case Abstraction(var,body):

            node = pydot.Node(name=str(uuid.uuid1()), label="λ" + var, shape="plaintext")
            graph.add_node(node)

            lligades[var] = node

            child_node = makeGraph(body, graph, lligades)
            graph.add_edge(pydot.Edge(node, child_node))

            return node



async def outputGraph(t:Term, update: Update, context: ContextTypes.DEFAULT_TYPE):
    graph = pydot.Dot(graph_type='digraph')
    makeGraph(t,graph,dict())
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

        await outputGraph(expresion,update,context)

        max_reductions=20

        await update.message.reply_text("beggining evaluation...")

        evaluated_expression = await evaluate_term(expresion, max_reductions ,update)

        await update.message.reply_text("evaluation complete!")

        if evaluated_expression:

            await update.message.reply_text(show(evaluated_expression))
            await outputGraph(evaluated_expression,update,context)

        else:
            await update.message.reply_text("Nothing, cannot be computed on " + str(max_reductions) + " steps")


def main() -> None:

    application = Application.builder().token("6021919629:AAESJhrndta0eAlPLRMw1ehumFnq7NQ5A6M").build()

    application.add_handler(CommandHandler('start', show_start))
    application.add_handler(CommandHandler('help', show_help))
    application.add_handler(CommandHandler('author', show_author))
    application.add_handler(CommandHandler('macros', show_macros))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, evaluate_expression))

    application.run_polling(1.0)

if __name__ == "__main__":

    main()