from __future__ import annotations
from dataclasses import dataclass

from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from lambdaVisitor import lambdaVisitor

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

class TreeVisitor(lambdaVisitor):
    def visitVariable(self, ctx):
        [var] = list(ctx.getChildren())
        print(var.getText())
        return Variable(var.getText())

    def visitTermeParentitzat(self, ctx):
        [p1,ter,p2] = list(ctx.getChildren())
        return self.visit(ter)

    def visitAbstraccio(self, ctx):
        [op1, vars, op2, terme] = list(ctx.getChildren())

        t = self.visit(terme)
        for c in reversed(self.visit(vars)):
            t = Abstraction(c, t)
        return t

    def visitVariables(self, ctx):
        vars = list(ctx.getChildren())
        return ''.join([var.getText() for var in vars])

    def visitAplicacio(self, ctx):
        [function,argument] = list(ctx.getChildren())
        return Application(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)
    
def show(t: Term) -> string:
    match t:
        case Variable(name):
            return name
        case Abstraction(var,term):
            return "(" + "λ" + var + "." + term + ")"
        case Application(function,argument):
            return "(" + function + argument + ")"
        
#ojo con el numero maximo de pasos
#en los tres puntos ponemos un log de las transacciones
#de las reducciones que voy haciendo
def eval(t: Term): #def eval(t: Term,...):-> (Terme?)
    match t:
        case Variable(name):
            return t #, ...
        case Abstraction(var,term):
            return "(" + "λ" + var + "." + term + ")"
        case Application(function,argument):
            if(isInstance(a,Abstraction)):
                result = 1 #beta(a,b,...)
                        #, ... aqui van las historias de transacciones
                        #si es una abstraccion el resultado es aplciar beta

input_stream = InputStream(input('? '))
while input_stream:
    lexer = lambdaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lambdaParser(token_stream)
    tree = parser.root()

    print(tree.toStringTree(recog=parser))

    visitor = TreeVisitor()
    expresion = visitor.visit(tree)
    print(expresion)
    
    #visitor2.visit(tree)
    input_stream = InputStream(input('? '))

