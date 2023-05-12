# Generated from exprs.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\5\3\31\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\5\5\"\n\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\63\n\5\f")
        buf.write("\5\16\5\66\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7F\n\7\3\b\3\b\3\b\3\b\2\3\b\t\2")
        buf.write("\4\6\b\n\f\16\2\2\2N\2\23\3\2\2\2\4\30\3\2\2\2\6\32\3")
        buf.write("\2\2\2\b!\3\2\2\2\n\67\3\2\2\2\fE\3\2\2\2\16G\3\2\2\2")
        buf.write("\20\24\3\2\2\2\21\24\5\4\3\2\22\24\5\b\5\2\23\20\3\2\2")
        buf.write("\2\23\21\3\2\2\2\23\22\3\2\2\2\24\3\3\2\2\2\25\31\5\6")
        buf.write("\4\2\26\31\5\n\6\2\27\31\5\16\b\2\30\25\3\2\2\2\30\26")
        buf.write("\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\7\20\2\2\33")
        buf.write("\34\7\3\2\2\34\35\5\b\5\2\35\7\3\2\2\2\36\37\b\5\1\2\37")
        buf.write("\"\7\17\2\2 \"\7\20\2\2!\36\3\2\2\2! \3\2\2\2\"\64\3\2")
        buf.write("\2\2#$\f\t\2\2$%\7\4\2\2%\63\5\b\5\t&\'\f\b\2\2\'(\7\5")
        buf.write("\2\2(\63\5\b\5\t)*\f\7\2\2*+\7\6\2\2+\63\5\b\5\b,-\f\6")
        buf.write("\2\2-.\7\7\2\2.\63\5\b\5\7/\60\f\5\2\2\60\61\7\b\2\2\61")
        buf.write("\63\5\b\5\6\62#\3\2\2\2\62&\3\2\2\2\62)\3\2\2\2\62,\3")
        buf.write("\2\2\2\62/\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3")
        buf.write("\2\2\2\65\t\3\2\2\2\66\64\3\2\2\2\678\7\t\2\289\5\f\7")
        buf.write("\29:\7\n\2\2:;\5\4\3\2;<\7\13\2\2<\13\3\2\2\2=>\5\b\5")
        buf.write("\2>?\7\f\2\2?@\5\b\5\2@F\3\2\2\2AB\5\b\5\2BC\7\r\2\2C")
        buf.write("D\5\b\5\2DF\3\2\2\2E=\3\2\2\2EA\3\2\2\2F\r\3\2\2\2GH\7")
        buf.write("\16\2\2HI\7\20\2\2I\17\3\2\2\2\b\23\30!\62\64E")
        return buf.getvalue()


class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'^'", "'*'", "'/'", "'+'", "'-'", 
                     "'if'", "'then'", "'end'", "'='", "'<>'", "'write'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "ID", "WS" ]

    RULE_root = 0
    RULE_instruccio = 1
    RULE_assignacio = 2
    RULE_expr = 3
    RULE_condicional = 4
    RULE_condicio = 5
    RULE_write = 6

    ruleNames =  [ "root", "instruccio", "assignacio", "expr", "condicional", 
                   "condicio", "write" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NUM=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccio(self):
            return self.getTypedRuleContext(exprsParser.InstruccioContext,0)


        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.instruccio()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignacio(self):
            return self.getTypedRuleContext(exprsParser.AssignacioContext,0)


        def condicional(self):
            return self.getTypedRuleContext(exprsParser.CondicionalContext,0)


        def write(self):
            return self.getTypedRuleContext(exprsParser.WriteContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_instruccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccio" ):
                return visitor.visitInstruccio(self)
            else:
                return visitor.visitChildren(self)




    def instruccio(self):

        localctx = exprsParser.InstruccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccio)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignacio()
                pass
            elif token in [exprsParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.condicional()
                pass
            elif token in [exprsParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.write()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_assignacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)




    def assignacio(self):

        localctx = exprsParser.AssignacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(exprsParser.ID)
            self.state = 25
            self.match(exprsParser.T__0)
            self.state = 26
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ExpressioBinariaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressioBinaria" ):
                return visitor.visitExpressioBinaria(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.NUM]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.match(exprsParser.NUM)
                pass
            elif token in [exprsParser.ID]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(exprsParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 34
                        self.match(exprsParser.T__1)
                        self.state = 35
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        self.match(exprsParser.T__2)
                        self.state = 38
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 40
                        self.match(exprsParser.T__3)
                        self.state = 41
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 43
                        self.match(exprsParser.T__4)
                        self.state = 44
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(exprsParser.T__5)
                        self.state = 47
                        self.expr(4)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(exprsParser.CondicioContext,0)


        def instruccio(self):
            return self.getTypedRuleContext(exprsParser.InstruccioContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = exprsParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(exprsParser.T__6)
            self.state = 54
            self.condicio()
            self.state = 55
            self.match(exprsParser.T__7)
            self.state = 56
            self.instruccio()
            self.state = 57
            self.match(exprsParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_condicio

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IgualtatContext(CondicioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondicioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualtat" ):
                return visitor.visitIgualtat(self)
            else:
                return visitor.visitChildren(self)


    class DesigualtatContext(CondicioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondicioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesigualtat" ):
                return visitor.visitDesigualtat(self)
            else:
                return visitor.visitChildren(self)



    def condicio(self):

        localctx = exprsParser.CondicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicio)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = exprsParser.IgualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(exprsParser.T__9)
                self.state = 61
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = exprsParser.DesigualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(exprsParser.T__10)
                self.state = 65
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def getRuleIndex(self):
            return exprsParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = exprsParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(exprsParser.T__11)
            self.state = 70
            self.match(exprsParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




