// Generated from /home/tortilla/Escritorio/LP/compilador/exprs.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class exprsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, NUM=13, ID=14, WS=15;
	public static final int
		RULE_root = 0, RULE_instruccio = 1, RULE_assignacio = 2, RULE_expr = 3, 
		RULE_condicional = 4, RULE_condicio = 5, RULE_write = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "instruccio", "assignacio", "expr", "condicional", "condicio", 
			"write"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':='", "'^'", "'*'", "'/'", "'+'", "'-'", "'if'", "'then'", "'end'", 
			"'='", "'<>'", "'write'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "NUM", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "exprs.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public exprsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public InstruccioContext instruccio() {
			return getRuleContext(InstruccioContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(17);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(15);
				instruccio();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(16);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstruccioContext extends ParserRuleContext {
		public AssignacioContext assignacio() {
			return getRuleContext(AssignacioContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public InstruccioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccio; }
	}

	public final InstruccioContext instruccio() throws RecognitionException {
		InstruccioContext _localctx = new InstruccioContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruccio);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				assignacio();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				condicional();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(21);
				write();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignacioContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(exprsParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignacioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignacio; }
	}

	public final AssignacioContext assignacio() throws RecognitionException {
		AssignacioContext _localctx = new AssignacioContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignacio);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(ID);
			setState(25);
			match(T__0);
			setState(26);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NumeroContext extends ExprContext {
		public TerminalNode NUM() { return getToken(exprsParser.NUM, 0); }
		public NumeroContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class VariableContext extends ExprContext {
		public TerminalNode ID() { return getToken(exprsParser.ID, 0); }
		public VariableContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressioBinariaContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExpressioBinariaContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				{
				_localctx = new NumeroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(29);
				match(NUM);
				}
				break;
			case ID:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(30);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(50);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(48);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(33);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(34);
						match(T__1);
						setState(35);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(36);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(37);
						match(T__2);
						setState(38);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(39);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(40);
						match(T__3);
						setState(41);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(42);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(43);
						match(T__4);
						setState(44);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(45);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(46);
						match(T__5);
						setState(47);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(52);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class CondicionalContext extends ParserRuleContext {
		public CondicioContext condicio() {
			return getRuleContext(CondicioContext.class,0);
		}
		public InstruccioContext instruccio() {
			return getRuleContext(InstruccioContext.class,0);
		}
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(T__6);
			setState(54);
			condicio();
			setState(55);
			match(T__7);
			setState(56);
			instruccio();
			setState(57);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicioContext extends ParserRuleContext {
		public CondicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicio; }
	 
		public CondicioContext() { }
		public void copyFrom(CondicioContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IgualtatContext extends CondicioContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public IgualtatContext(CondicioContext ctx) { copyFrom(ctx); }
	}
	public static class DesigualtatContext extends CondicioContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public DesigualtatContext(CondicioContext ctx) { copyFrom(ctx); }
	}

	public final CondicioContext condicio() throws RecognitionException {
		CondicioContext _localctx = new CondicioContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_condicio);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new IgualtatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				expr(0);
				setState(60);
				match(T__9);
				setState(61);
				expr(0);
				}
				break;
			case 2:
				_localctx = new DesigualtatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				expr(0);
				setState(64);
				match(T__10);
				setState(65);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WriteContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(exprsParser.ID, 0); }
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(T__11);
			setState(70);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 4);
		case 4:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21K\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\5\2\24\n\2\3\3"+
		"\3\3\3\3\5\3\31\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\"\n\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\63\n\5\f\5\16\5\66"+
		"\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7F\n\7"+
		"\3\b\3\b\3\b\3\b\2\3\b\t\2\4\6\b\n\f\16\2\2\2N\2\23\3\2\2\2\4\30\3\2\2"+
		"\2\6\32\3\2\2\2\b!\3\2\2\2\n\67\3\2\2\2\fE\3\2\2\2\16G\3\2\2\2\20\24\3"+
		"\2\2\2\21\24\5\4\3\2\22\24\5\b\5\2\23\20\3\2\2\2\23\21\3\2\2\2\23\22\3"+
		"\2\2\2\24\3\3\2\2\2\25\31\5\6\4\2\26\31\5\n\6\2\27\31\5\16\b\2\30\25\3"+
		"\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\7\20\2\2\33\34\7"+
		"\3\2\2\34\35\5\b\5\2\35\7\3\2\2\2\36\37\b\5\1\2\37\"\7\17\2\2 \"\7\20"+
		"\2\2!\36\3\2\2\2! \3\2\2\2\"\64\3\2\2\2#$\f\t\2\2$%\7\4\2\2%\63\5\b\5"+
		"\t&\'\f\b\2\2\'(\7\5\2\2(\63\5\b\5\t)*\f\7\2\2*+\7\6\2\2+\63\5\b\5\b,"+
		"-\f\6\2\2-.\7\7\2\2.\63\5\b\5\7/\60\f\5\2\2\60\61\7\b\2\2\61\63\5\b\5"+
		"\6\62#\3\2\2\2\62&\3\2\2\2\62)\3\2\2\2\62,\3\2\2\2\62/\3\2\2\2\63\66\3"+
		"\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\64\3\2\2\2\678\7\t"+
		"\2\289\5\f\7\29:\7\n\2\2:;\5\4\3\2;<\7\13\2\2<\13\3\2\2\2=>\5\b\5\2>?"+
		"\7\f\2\2?@\5\b\5\2@F\3\2\2\2AB\5\b\5\2BC\7\r\2\2CD\5\b\5\2DF\3\2\2\2E"+
		"=\3\2\2\2EA\3\2\2\2F\r\3\2\2\2GH\7\16\2\2HI\7\20\2\2I\17\3\2\2\2\b\23"+
		"\30!\62\64E";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}