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

        for key, var in macros.items():
            await update.message.reply_text(key + " ≡ " + show(var))

    else: 

        await update.message.reply_text("No macros defined, define macros with \"MACROINCAPS\" (=|≡) expression")

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