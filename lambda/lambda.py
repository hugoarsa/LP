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
        [l,variables,punt,body] = list(ctx.getChildren())

        t = self.visit(body)

        for c in reversed(vars.getText()):
            t = Abstraction(c,t)
        return td

    def visitVariables(self,ctx):
        vars = list(ctx.getChildren())
        return ''.join([vars.getText() for var in vars])

    def visitAplicacio(self, ctx):
        [function,argument] = list(ctx.getChildren())
        return Application(self.visit(function), self.visit(argument))

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        return self.visit(terme)

        

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

