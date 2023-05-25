# Generated from exprs.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,2,1,
        2,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,48,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,3,8,65,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,
        16,0,2,1,0,11,12,1,0,13,14,80,0,18,1,0,0,0,2,23,1,0,0,0,4,30,1,0,
        0,0,6,32,1,0,0,0,8,36,1,0,0,0,10,47,1,0,0,0,12,49,1,0,0,0,14,55,
        1,0,0,0,16,64,1,0,0,0,18,19,3,2,1,0,19,1,1,0,0,0,20,22,3,4,2,0,21,
        20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,3,1,0,0,
        0,25,23,1,0,0,0,26,31,3,6,3,0,27,31,3,12,6,0,28,31,3,14,7,0,29,31,
        3,8,4,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,
        31,5,1,0,0,0,32,33,5,16,0,0,33,34,5,1,0,0,34,35,3,16,8,0,35,7,1,
        0,0,0,36,37,5,2,0,0,37,38,3,16,8,0,38,9,1,0,0,0,39,40,3,16,8,0,40,
        41,5,3,0,0,41,42,3,16,8,0,42,48,1,0,0,0,43,44,3,16,8,0,44,45,5,4,
        0,0,45,46,3,16,8,0,46,48,1,0,0,0,47,39,1,0,0,0,47,43,1,0,0,0,48,
        11,1,0,0,0,49,50,5,5,0,0,50,51,3,10,5,0,51,52,5,6,0,0,52,53,3,2,
        1,0,53,54,5,7,0,0,54,13,1,0,0,0,55,56,5,8,0,0,56,57,3,10,5,0,57,
        58,5,9,0,0,58,59,3,2,1,0,59,60,5,7,0,0,60,15,1,0,0,0,61,62,6,8,-1,
        0,62,65,5,15,0,0,63,65,5,16,0,0,64,61,1,0,0,0,64,63,1,0,0,0,65,77,
        1,0,0,0,66,67,10,5,0,0,67,68,5,10,0,0,68,76,3,16,8,5,69,70,10,4,
        0,0,70,71,7,0,0,0,71,76,3,16,8,5,72,73,10,3,0,0,73,74,7,1,0,0,74,
        76,3,16,8,4,75,66,1,0,0,0,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,17,1,0,0,0,79,77,1,0,0,0,6,23,
        30,47,64,75,77
    ]

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
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65828) != 0):
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
        __slots__ = 'parser'

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
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assignacio()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.condicional()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.bucle()
                pass
            elif token in [2]:
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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        __slots__ = 'parser'

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(exprsParser.NUM)
                pass
            elif token in [16]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(exprsParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 67
                        self.match(exprsParser.T__9)
                        self.state = 68
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 70
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.ExpressioBinariaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 73
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(4)
                        pass

             
                self.state = 79
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




