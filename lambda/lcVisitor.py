# Generated from lc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#variable.
    def visitVariable(self, ctx:lcParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#termeParentitzat.
    def visitTermeParentitzat(self, ctx:lcParser.TermeParentitzatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#abstraccio.
    def visitAbstraccio(self, ctx:lcParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#aplicacio.
    def visitAplicacio(self, ctx:lcParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#variables.
    def visitVariables(self, ctx:lcParser.VariablesContext):
        return self.visitChildren(ctx)



del lcParser