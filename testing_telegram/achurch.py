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
class Application:
    function: Term
    argument: Term

Term = Variable | Abstraction | Application

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
        return Application(Application(self.macros[str(ID)],self.visit(terme1)),self.visit(terme2))

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
        return Application(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)
    
    def visitAssignacio1(self, ctx):  
        [m, eq, terme] = list (ctx.getChildren())
        self.macros[str(m)] = self.visit(terme)
        return 0
    
    def printMacros(self):
        for key, value in self.macros.items():
            print(key + " ≡ " + show(value))  

def show(t: Term) -> string:
    match t:

        case Variable(name):
            return name
        
        case Abstraction(var,term):
            return "(" + "λ" + var + "." + show(term) + ")"
        
        case Application(function,argument):
            return "(" + show(function) + show(argument) + ")"
        
async def evaluate_term(term: Term, max_reductions: int, update, context) -> Term:

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
        elif isinstance(term, Application):
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
            
            case Application(function,argument):

                function = replace_alfa(function, old_variable, new_variable)
                argument = replace_alfa(argument, old_variable, new_variable)
                return Application(function,argument)
            
    def alfas_rec(term: Term, variables_to_replace, var_original) -> Term:
        match term:

            case Abstraction(var,body):

                if var in variables_to_replace and var_original in get_variables(body):   

                    new_variable = generate_new_variable_name(body)
                    #print("en el body " + show(body) + " de la abstracion "+ show(term))
                    #print("reemplazaremos la variable " + var + " por la variable " + new_variable)
                    new_body = replace_alfa(body,var,new_variable)
                    return Abstraction(new_variable,new_body)
                
                new_body = alfas_rec(body, variables_to_replace, var_original)
                return Abstraction(var,new_body)
            
            case Application(function,argument):

                new_function = alfas_rec(function, variables_to_replace, var_original)
                new_argument = alfas_rec(argument, variables_to_replace, var_original)
                return Application(new_function,new_argument)
        
        return term
    
    def do_needed_alfas(term: Term) -> Term:

        variables_to_replace = get_variables(term.argument)

        if term.function.variable in variables_to_replace:
            variables_to_replace.remove(term.function.variable)

 
        #print("alfas_rec(" + show(term.function.body) + ", variables to replace, " + term.function.variable + ")")

        new_body = alfas_rec(term.function.body, variables_to_replace, term.function.variable)

        if new_body != term.function.body:
            print("α-conversió:")
            print(show(term.function) + " → " + show(Abstraction(term.function.variable,new_body)))
            
            return Application(Abstraction(term.function.variable,new_body),term.argument)
        
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
            case Application(function,argument):
                new_function = replace_beta(function, substitutions)
                new_argument = replace_beta(argument, substitutions)
                return Application(new_function, new_argument)


    def evaluate_a_beta(term: Term,update, context) -> Term:

        match term:

            case Variable(var):
                return term, False
            
            case Abstraction(var,body):
                new_body, modif = evaluate_a_beta(body)
                return Abstraction(var, new_body), modif
            
            case Application(function,argument):

                if isinstance(term.function, Abstraction):

                    alfa_term = do_needed_alfas(term)

                    new_term = replace_beta(alfa_term.function.body, {alfa_term.function.variable: argument})

                    print("β-reducció:")
                    print(show(term) + " → " + show(new_term))

                    return new_term, True
                
                else:

                    new_function, modif = evaluate_a_beta(function)
                    if modif:
                        return Application(new_function, argument), modif

                    new_argument, modif = evaluate_a_beta(argument)
                    return Application(function, new_argument), modif
                
        return term
    
    
    for i in range(1,max_reductions):
        new_term, modif = evaluate_a_beta(term,update, context)
        if not modif:
            return new_term
        term = new_term
    
    #si llegamos aqui no hemos encontrado en los pasos el resultado
    return 0


import logging


from telegram import __version__ as TG_VER

try:

    from telegram import __version_info__

except ImportError:

    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]


if __version_info__ < (20, 0, 0, "alpha", 1):

    raise RuntimeError(

        f"This example is not compatible with your current PTB version {TG_VER}. To view the "

        f"{TG_VER} version of this example, "

        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"

    )

from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and context.

async def show_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user = update.effective_user

    context.user_data["macros_user"] = {}

    await update.message.reply_html(

        rf"Hi {user.mention_html()} I'm Hugo's AChurch Bot!",

        reply_markup=ForceReply(selective=True),

    )

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.message.chat_id, 
                                   text="\\start \n \\author \n \\help \n \\macros \n Lambda Calculus Expression to eval \n MACRO = Lambda Calculus Expression")

async def show_author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.message.chat_id, 
                                   text="AChurchBot! \n @ Hugo Aranda Sanchez, 2023")
    
async def show_macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.message.chat_id, 
                                   text="AChurchBot! \n @ Hugo Aranda Sanchez, 2023")
    

async def evaluate_expression(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    input_text = update.message.text
    input_stream = InputStream(input_text)
    visitor = TreeVisitor(context.user_data.get("macros_user"))
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()

    expresion = visitor.visit(tree)

    await update.message.reply_text(show(expresion))

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