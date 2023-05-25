# Generated from lambda.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .lambdaParser import lambdaParser
else:
    from lambdaParser import lambdaParser

# This class defines a complete generic visitor for a parse tree produced by lambdaParser.

class lambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lambdaParser#root.
    def visitRoot(self, ctx:lambdaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#variable.
    def visitVariable(self, ctx:lambdaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#termeParentitzat.
    def visitTermeParentitzat(self, ctx:lambdaParser.TermeParentitzatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#abstraccio.
    def visitAbstraccio(self, ctx:lambdaParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#aplicacio.
    def visitAplicacio(self, ctx:lambdaParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#vars.
    def visitVars(self, ctx:lambdaParser.VarsContext):
        return self.visitChildren(ctx)



del lambdaParser