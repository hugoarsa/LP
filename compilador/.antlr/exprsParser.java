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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, NUM=15, ID=16, WS=17;
	public static final int
		RULE_root = 0, RULE_instruccions = 1, RULE_instruccio = 2, RULE_assignacio = 3, 
		RULE_write = 4, RULE_condicio = 5, RULE_condicional = 6, RULE_bucle = 7, 
		RULE_expr = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "instruccions", "instruccio", "assignacio", "write", "condicio", 
			"condicional", "bucle", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':='", "'write'", "'='", "'<>'", "'if'", "'then'", "'end'", "'while'", 
			"'do'", "'^'", "'*'", "'/'", "'+'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "NUM", "ID", "WS"
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
		public InstruccionsContext instruccions() {
			return getRuleContext(InstruccionsContext.class,0);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			instruccions();
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

	public static class InstruccionsContext extends ParserRuleContext {
		public List<InstruccioContext> instruccio() {
			return getRuleContexts(InstruccioContext.class);
		}
		public InstruccioContext instruccio(int i) {
			return getRuleContext(InstruccioContext.class,i);
		}
		public InstruccionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccions; }
	}

	public final InstruccionsContext instruccions() throws RecognitionException {
		InstruccionsContext _localctx = new InstruccionsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruccions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << T__7) | (1L << ID))) != 0)) {
				{
				{
				setState(20);
				instruccio();
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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
		public BucleContext bucle() {
			return getRuleContext(BucleContext.class,0);
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
		enterRule(_localctx, 4, RULE_instruccio);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				assignacio();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				condicional();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(28);
				bucle();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 4);
				{
				setState(29);
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
		enterRule(_localctx, 6, RULE_assignacio);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(ID);
			setState(33);
			match(T__0);
			setState(34);
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

	public static class WriteContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(T__1);
			setState(37);
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
			setState(47);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new IgualtatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				expr(0);
				setState(40);
				match(T__2);
				setState(41);
				expr(0);
				}
				break;
			case 2:
				_localctx = new DesigualtatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				expr(0);
				setState(44);
				match(T__3);
				setState(45);
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

	public static class CondicionalContext extends ParserRuleContext {
		public CondicioContext condicio() {
			return getRuleContext(CondicioContext.class,0);
		}
		public InstruccionsContext instruccions() {
			return getRuleContext(InstruccionsContext.class,0);
		}
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(T__4);
			setState(50);
			condicio();
			setState(51);
			match(T__5);
			setState(52);
			instruccions();
			setState(53);
			match(T__6);
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

	public static class BucleContext extends ParserRuleContext {
		public CondicioContext condicio() {
			return getRuleContext(CondicioContext.class,0);
		}
		public InstruccionsContext instruccions() {
			return getRuleContext(InstruccionsContext.class,0);
		}
		public BucleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bucle; }
	}

	public final BucleContext bucle() throws RecognitionException {
		BucleContext _localctx = new BucleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_bucle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(T__7);
			setState(56);
			condicio();
			setState(57);
			match(T__8);
			setState(58);
			instruccions();
			setState(59);
			match(T__6);
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
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				{
				_localctx = new NumeroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(62);
				match(NUM);
				}
				break;
			case ID:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(63);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(75);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(66);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(67);
						match(T__9);
						setState(68);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(69);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(70);
						_la = _input.LA(1);
						if ( !(_la==T__10 || _la==T__11) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(71);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExpressioBinariaContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(72);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(73);
						_la = _input.LA(1);
						if ( !(_la==T__12 || _la==T__13) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(74);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23S\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3"+
		"\7\3\30\n\3\f\3\16\3\33\13\3\3\4\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\62\n\7\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nC\n\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\7\nN\n\n\f\n\16\nQ\13\n\3\n\2\3\22\13\2\4\6\b\n"+
		"\f\16\20\22\2\4\3\2\r\16\3\2\17\20\2R\2\24\3\2\2\2\4\31\3\2\2\2\6 \3\2"+
		"\2\2\b\"\3\2\2\2\n&\3\2\2\2\f\61\3\2\2\2\16\63\3\2\2\2\209\3\2\2\2\22"+
		"B\3\2\2\2\24\25\5\4\3\2\25\3\3\2\2\2\26\30\5\6\4\2\27\26\3\2\2\2\30\33"+
		"\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\31\3\2\2\2\34!\5"+
		"\b\5\2\35!\5\16\b\2\36!\5\20\t\2\37!\5\n\6\2 \34\3\2\2\2 \35\3\2\2\2 "+
		"\36\3\2\2\2 \37\3\2\2\2!\7\3\2\2\2\"#\7\22\2\2#$\7\3\2\2$%\5\22\n\2%\t"+
		"\3\2\2\2&\'\7\4\2\2\'(\5\22\n\2(\13\3\2\2\2)*\5\22\n\2*+\7\5\2\2+,\5\22"+
		"\n\2,\62\3\2\2\2-.\5\22\n\2./\7\6\2\2/\60\5\22\n\2\60\62\3\2\2\2\61)\3"+
		"\2\2\2\61-\3\2\2\2\62\r\3\2\2\2\63\64\7\7\2\2\64\65\5\f\7\2\65\66\7\b"+
		"\2\2\66\67\5\4\3\2\678\7\t\2\28\17\3\2\2\29:\7\n\2\2:;\5\f\7\2;<\7\13"+
		"\2\2<=\5\4\3\2=>\7\t\2\2>\21\3\2\2\2?@\b\n\1\2@C\7\21\2\2AC\7\22\2\2B"+
		"?\3\2\2\2BA\3\2\2\2CO\3\2\2\2DE\f\7\2\2EF\7\f\2\2FN\5\22\n\7GH\f\6\2\2"+
		"HI\t\2\2\2IN\5\22\n\7JK\f\5\2\2KL\t\3\2\2LN\5\22\n\6MD\3\2\2\2MG\3\2\2"+
		"\2MJ\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\23\3\2\2\2QO\3\2\2\2\b\31"+
		" \61BMO";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}