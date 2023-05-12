from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0

    def visitExpressioBinaria(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + str(operador))
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())

class EvalVisitor(exprsVisitor):
    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))
    def visitExpressioBinaria(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if str(operador) == '+':
            return self.visit(expressio1) + self.visit(expressio2)
        elif str(operador) == '-':
            return self.visit(expressio1) - self.visit(expressio2)
        elif str(operador) == '/':
            return self.visit(expressio1) / self.visit(expressio2)
        elif str(operador) == '*':
            return self.visit(expressio1) * self.visit(expressio2)
        elif str(operador) == '^':
            return self.visit(expressio1) ** self.visit(expressio2)
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())

##afegir un map 
#visit write y asignacio
    


input_stream = InputStream(input('? '))
lexer = exprsLexer(input_stream)

#convertir los inputs en un bucle 
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()
#if parser.getNumberOfSyntaxErrors() == 0:

#visitador para expresiones
visitor_tree = TreeVisitor()
visitor_tree.visit(tree)

#visitador para evaluaciones
visitor_eval = EvalVisitor()
visitor_eval.visit(tree)

