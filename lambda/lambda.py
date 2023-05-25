from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from lambdaVisitor import lambdaVisitor
from dataclasses import dataclass

@dataclass
class Variable:
    name: str

@dataclass
class Abstraction:
    variables: list[Variable]
    body: 'Term'

@dataclass
class Application:
    function: 'Term'
    argument: 'Term'

Term = Variable | Abstraction | Application

class TreeVisitor(lambdaVisitor):

    def visitVariable(self, ctx):
        [var] = list(ctx.getChildren())
        return Variable(var.getText())

    def visitTermeParentitzat(self, ctx):
        return self.visit(ctx.terme())

    def visitAbstraccio(self, ctx):
        variables = [Variable(var.getText()) for var in ctx.vars().VAR()]
        body = self.visit(ctx.terme())
        return Abstraction(variables, body)

    def visitAplicacio(self, ctx):
        [function,argument] = list(ctx.getChildren())
        return Application(function, argument)

    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        print("Arbre:")
        print("(" + show(self.visit(terme)) + ")") 

def show(t: Term):
    match t:
        case Variable(s):
            return s
        case Application(vars,bod):
            return "(λ" + vars + "." + bod + ")"
        case Abstraction(term1,term2):
            return "(" + term1 + "" + term2 + ")"
   


#visitor2 = LambdaVisitor()
input_stream = InputStream(input('? '))
while input_stream:
    lexer = lambdaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lambdaParser(token_stream)
    tree = parser.root()

    visitor = TreeVisitor()
    expression = visitor.visit(tree)
    #visitor2.visit(tree)