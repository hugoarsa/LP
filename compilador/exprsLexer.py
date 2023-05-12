# Generated from exprs.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\6\16G\n\16\r\16\16\16H\3\17\6\17L\n\17")
        buf.write("\r\17\16\17M\3\20\6\20Q\n\20\r\20\16\20R\3\20\3\20\2\2")
        buf.write("\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21\3\2\5\3\2\62;\4\2C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2")
        buf.write("\2\5$\3\2\2\2\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2")
        buf.write("\2\2\17.\3\2\2\2\21\61\3\2\2\2\23\66\3\2\2\2\25:\3\2\2")
        buf.write("\2\27<\3\2\2\2\31?\3\2\2\2\33F\3\2\2\2\35K\3\2\2\2\37")
        buf.write("P\3\2\2\2!\"\7<\2\2\"#\7?\2\2#\4\3\2\2\2$%\7`\2\2%\6\3")
        buf.write("\2\2\2&\'\7,\2\2\'\b\3\2\2\2()\7\61\2\2)\n\3\2\2\2*+\7")
        buf.write("-\2\2+\f\3\2\2\2,-\7/\2\2-\16\3\2\2\2./\7k\2\2/\60\7h")
        buf.write("\2\2\60\20\3\2\2\2\61\62\7v\2\2\62\63\7j\2\2\63\64\7g")
        buf.write("\2\2\64\65\7p\2\2\65\22\3\2\2\2\66\67\7g\2\2\678\7p\2")
        buf.write("\289\7f\2\29\24\3\2\2\2:;\7?\2\2;\26\3\2\2\2<=\7>\2\2")
        buf.write("=>\7@\2\2>\30\3\2\2\2?@\7y\2\2@A\7t\2\2AB\7k\2\2BC\7v")
        buf.write("\2\2CD\7g\2\2D\32\3\2\2\2EG\t\2\2\2FE\3\2\2\2GH\3\2\2")
        buf.write("\2HF\3\2\2\2HI\3\2\2\2I\34\3\2\2\2JL\t\3\2\2KJ\3\2\2\2")
        buf.write("LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\36\3\2\2\2OQ\t\4\2\2P")
        buf.write("O\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b")
        buf.write("\20\2\2U \3\2\2\2\6\2HMR\3\b\2\2")
        return buf.getvalue()


class exprsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    NUM = 13
    ID = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'^'", "'*'", "'/'", "'+'", "'-'", "'if'", "'then'", 
            "'end'", "'='", "'<>'", "'write'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUM", "ID", 
                  "WS" ]

    grammarFileName = "exprs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


