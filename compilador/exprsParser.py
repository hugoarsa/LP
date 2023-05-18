# Generated from exprs.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\4\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\62\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\5\nC\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\7\nT\n\n\f\n\16\nW\13\n\3\n\2\3\22\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\2\2Z\2\24\3\2\2\2\4\31\3\2\2\2")
        buf.write("\6 \3\2\2\2\b\"\3\2\2\2\n&\3\2\2\2\f\61\3\2\2\2\16\63")
        buf.write("\3\2\2\2\209\3\2\2\2\22B\3\2\2\2\24\25\5\4\3\2\25\3\3")
        buf.write("\2\2\2\26\30\5\6\4\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\31\3\2\2\2\34!")
        buf.write("\5\b\5\2\35!\5\16\b\2\36!\5\20\t\2\37!\5\n\6\2 \34\3\2")
        buf.write("\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\7\3\2\2\2\"")
        buf.write("#\7\22\2\2#$\7\3\2\2$%\5\22\n\2%\t\3\2\2\2&\'\7\4\2\2")
        buf.write("\'(\5\22\n\2(\13\3\2\2\2)*\5\22\n\2*+\7\5\2\2+,\5\22\n")
        buf.write("\2,\62\3\2\2\2-.\5\22\n\2./\7\6\2\2/\60\5\22\n\2\60\62")
        buf.write("\3\2\2\2\61)\3\2\2\2\61-\3\2\2\2\62\r\3\2\2\2\63\64\7")
        buf.write("\7\2\2\64\65\5\f\7\2\65\66\7\b\2\2\66\67\5\4\3\2\678\7")
        buf.write("\t\2\28\17\3\2\2\29:\7\n\2\2:;\5\f\7\2;<\7\13\2\2<=\5")
        buf.write("\4\3\2=>\7\t\2\2>\21\3\2\2\2?@\b\n\1\2@C\7\21\2\2AC\7")
        buf.write("\22\2\2B?\3\2\2\2BA\3\2\2\2CU\3\2\2\2DE\f\t\2\2EF\7\f")
        buf.write("\2\2FT\5\22\n\tGH\f\b\2\2HI\7\r\2\2IT\5\22\n\tJK\f\7\2")
        buf.write("\2KL\7\16\2\2LT\5\22\n\bMN\f\6\2\2NO\7\17\2\2OT\5\22\n")
        buf.write("\7PQ\f\5\2\2QR\7\20\2\2RT\5\22\n\6SD\3\2\2\2SG\3\2\2\2")
        buf.write("SJ\3\2\2\2SM\3\2\2\2SP\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3")
        buf.write("\2\2\2V\23\3\2\2\2WU\3\2\2\2\b\31 \61BSU")
        return buf.getvalue()


class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'='", "'<>'", "'if'", 
                     "'then'", "'end'", "'while'", "'do'", "'^'", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "WS" ]

    RULE_root = 0
    RULE_instruccions = 1
    RULE_instruccio = 2
    RULE_assignacio = 3
    RULE_write = 4
    RULE_condicio = 5
    RULE_condicional = 6
    RULE_bucle = 7
    RULE_expr = 8

    ruleNames =  [ "root", "instruccions", "instruccio", "assignacio", "write", 
                   "condicio", "condicional", "bucle", "expr" ]

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
    T__12=13
    T__13=14
    NUM=15
    ID=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.instruccions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.InstruccioContext)
            else:
                return self.getTypedRuleContext(exprsParser.InstruccioContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_instruccions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccions" ):
                return visitor.visitInstruccions(self)
            else:
                return visitor.visitChildren(self)




    def instruccions(self):

        localctx = exprsParser.InstruccionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << exprsParser.T__1) | (1 << exprsParser.T__4) | (1 << exprsParser.T__7) | (1 << exprsParser.ID))) != 0):
                self.state = 20
                self.instruccio()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def bucle(self):
            return self.getTypedRuleContext(exprsParser.BucleContext,0)


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
        self.enterRule(localctx, 4, self.RULE_instruccio)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assignacio()
                pass
            elif token in [exprsParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.condicional()
                pass
            elif token in [exprsParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.bucle()
                pass
            elif token in [exprsParser.T__1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
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
        self.enterRule(localctx, 6, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(exprsParser.ID)
            self.state = 33
            self.match(exprsParser.T__0)
            self.state = 34
            self.expr(0)
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

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = exprsParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(exprsParser.T__1)
            self.state = 37
            self.expr(0)
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = exprsParser.IgualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(exprsParser.T__2)
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = exprsParser.DesigualtatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(exprsParser.T__3)
                self.state = 45
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(exprsParser.CondicioContext,0)


        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = exprsParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(exprsParser.T__4)
            self.state = 50
            self.condicio()
            self.state = 51
            self.match(exprsParser.T__5)
            self.state = 52
            self.instruccions()
            self.state = 53
            self.match(exprsParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BucleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(exprsParser.CondicioContext,0)


        def instruccions(self):
            return self.getTypedRuleContext(exprsParser.InstruccionsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_bucle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle" ):
                return visitor.visitBucle(self)
            else:
                return visitor.visitChildren(self)




    def bucle(self):

        localctx = exprsParser.BucleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bucle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(exprsParser.T__7)
            self.state = 56
            self.condicio()
            self.state = 57
            self.match(exprsParser.T__8)
            self.state = 58
            self.instruccions()
            self.state = 59
            self.match(exprsParser.T__6)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [exprsParser.NUM]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(exprsParser.NUM)
                pass
            elif token in [exprsParser.ID]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(exprsParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 67
                        self.match(exprsParser.T__9)
                        self.state = 68
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        self.match(exprsParser.T__10)
                        self.state = 71
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        self.match(exprsParser.T__11)
                        self.state = 74
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 76
                        self.match(exprsParser.T__12)
                        self.state = 77
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 79
                        self.match(exprsParser.T__13)
                        self.state = 80
                        self.expr(4)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
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
         




