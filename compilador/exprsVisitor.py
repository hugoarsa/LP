# Generated from exprs.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#instruccio.
    def visitInstruccio(self, ctx:exprsParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#ExpressioBinaria.
    def visitExpressioBinaria(self, ctx:exprsParser.ExpressioBinariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicional.
    def visitCondicional(self, ctx:exprsParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#igualtat.
    def visitIgualtat(self, ctx:exprsParser.IgualtatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#desigualtat.
    def visitDesigualtat(self, ctx:exprsParser.DesigualtatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)



del exprsParser