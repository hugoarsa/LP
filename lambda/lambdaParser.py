# Generated from lambda.g4 by ANTLR 4.13.0
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
        4,1,6,34,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,2,4,2,30,8,2,11,2,12,2,31,1,2,0,1,2,3,0,2,4,0,0,34,0,6,1,0,0,
        0,2,19,1,0,0,0,4,29,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,6,1,-1,0,
        9,20,5,5,0,0,10,11,5,1,0,0,11,12,3,2,1,0,12,13,5,2,0,0,13,20,1,0,
        0,0,14,15,5,4,0,0,15,16,3,4,2,0,16,17,5,3,0,0,17,18,3,2,1,2,18,20,
        1,0,0,0,19,8,1,0,0,0,19,10,1,0,0,0,19,14,1,0,0,0,20,25,1,0,0,0,21,
        22,10,1,0,0,22,24,3,2,1,2,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,
        0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,1,0,0,0,28,30,5,5,0,0,29,28,
        1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,0,0,3,
        19,25,31
    ]

class lambdaParser ( Parser ):

    grammarFileName = "lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DOT", "LAMBDA", 
                      "VAR", "WS" ]

    RULE_root = 0
    RULE_terme = 1
    RULE_vars = 2

    ruleNames =  [ "root", "terme", "vars" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DOT=3
    LAMBDA=4
    VAR=5
    WS=6

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

        def terme(self):
            return self.getTypedRuleContext(lambdaParser.TermeContext,0)


        def getRuleIndex(self):
            return lambdaParser.RULE_root




    def root(self):

        localctx = lambdaParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(lambdaParser.VAR, 0)


    class TermeParentitzatContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lambdaParser.TermeContext,0)



    class AbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lambdaParser.LAMBDA, 0)
        def vars_(self):
            return self.getTypedRuleContext(lambdaParser.VarsContext,0)

        def DOT(self):
            return self.getToken(lambdaParser.DOT, 0)
        def terme(self):
            return self.getTypedRuleContext(lambdaParser.TermeContext,0)



    class AplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TermeContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TermeContext,i)




    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lambdaParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = lambdaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(lambdaParser.VAR)
                pass
            elif token in [1]:
                localctx = lambdaParser.TermeParentitzatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(lambdaParser.T__0)
                self.state = 11
                self.terme(0)
                self.state = 12
                self.match(lambdaParser.T__1)
                pass
            elif token in [4]:
                localctx = lambdaParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(lambdaParser.LAMBDA)
                self.state = 15
                self.vars_()
                self.state = 16
                self.match(lambdaParser.DOT)
                self.state = 17
                self.terme(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lambdaParser.AplicacioContext(self, lambdaParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 21
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 22
                    self.terme(2) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(lambdaParser.VAR)
            else:
                return self.getToken(lambdaParser.VAR, i)

        def getRuleIndex(self):
            return lambdaParser.RULE_vars




    def vars_(self):

        localctx = lambdaParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(lambdaParser.VAR)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

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
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




