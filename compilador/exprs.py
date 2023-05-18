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
    def __init__(self):
        self.taula_continguts = {}

    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))

    def visitExpressioBinaria(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if str(operador) == '+':
            return self.visit(expressio1) + self.visit(expressio2)
        elif str(operador) == '-':
            return self.visit(expressio1) - self.visit(expressio2)
        elif str(operador) == '//':
            return self.visit(expressio1) / self.visit(expressio2)
        elif str(operador) == '*':
            return self.visit(expressio1) * self.visit(expressio2)
        elif str(operador) == '^':
            return self.visit(expressio1) ** self.visit(expressio2)
        
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    
    def visitVariable(self, ctx):
        [ID] = list(ctx.getChildren())
        return int(self.taula_continguts[str(ID)])

    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        [ID, operador, expressio] = list(ctx.getChildren())
        result = self.visit(expressio)
        self.taula_continguts[str(ID)] = result

    def visitWrite(self, ctx:exprsParser.WriteContext):
        [operador, expr] = list(ctx.getChildren())
        res = self.visit(expr)
        print(res)
    
    def visitCondicional(self, ctx:exprsParser.CondicionalContext):
        [inici, condicio, then, instruccions, end] = list(ctx.getChildren())
        if self.visit(condicio):
            self.visit(instruccions)

    def visitBucle(self, ctx:exprsParser.CondicionalContext):
        [inici, condicio, do, instruccions, end] = list(ctx.getChildren())
        while self.visit(condicio):
            self.visit(instruccions)

    def visitIgualtat(self, ctx):
        [expressio1, comparador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) == self.visit(expressio2)
    
    def visitDesigualtat(self, ctx):
        [expressio1, comparador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) != self.visit(expressio2)
    

visitor2 = EvalVisitor()
input_stream = InputStream(input('? '))
while input_stream:
    lexer = exprsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = exprsParser(token_stream)
    tree = parser.root()

#    if parser.getNumberOfSyntaxErrors() == 0:
#        #visitor = TreeVisitor()
#        #visitor.visit(tree)
    visitor2.visit(tree)
#    else:
#        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
#        print(tree.toStringTree(recog=parser))
    input_stream = InputStream(input('? '))

