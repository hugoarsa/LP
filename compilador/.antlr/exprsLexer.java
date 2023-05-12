// Generated from /home/tortilla/Escritorio/LP/compilador/exprs.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class exprsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, NUM=13, ID=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "NUM", "ID", "WS"
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


	public exprsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "exprs.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21V\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3"+
		"\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3"+
		"\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\6\16G\n"+
		"\16\r\16\16\16H\3\17\6\17L\n\17\r\17\16\17M\3\20\6\20Q\n\20\r\20\16\20"+
		"R\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r"+
		"\31\16\33\17\35\20\37\21\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2X"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5$\3\2"+
		"\2\2\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21\61\3"+
		"\2\2\2\23\66\3\2\2\2\25:\3\2\2\2\27<\3\2\2\2\31?\3\2\2\2\33F\3\2\2\2\35"+
		"K\3\2\2\2\37P\3\2\2\2!\"\7<\2\2\"#\7?\2\2#\4\3\2\2\2$%\7`\2\2%\6\3\2\2"+
		"\2&\'\7,\2\2\'\b\3\2\2\2()\7\61\2\2)\n\3\2\2\2*+\7-\2\2+\f\3\2\2\2,-\7"+
		"/\2\2-\16\3\2\2\2./\7k\2\2/\60\7h\2\2\60\20\3\2\2\2\61\62\7v\2\2\62\63"+
		"\7j\2\2\63\64\7g\2\2\64\65\7p\2\2\65\22\3\2\2\2\66\67\7g\2\2\678\7p\2"+
		"\289\7f\2\29\24\3\2\2\2:;\7?\2\2;\26\3\2\2\2<=\7>\2\2=>\7@\2\2>\30\3\2"+
		"\2\2?@\7y\2\2@A\7t\2\2AB\7k\2\2BC\7v\2\2CD\7g\2\2D\32\3\2\2\2EG\t\2\2"+
		"\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\34\3\2\2\2JL\t\3\2\2KJ\3\2"+
		"\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\36\3\2\2\2OQ\t\4\2\2PO\3\2\2\2QR\3"+
		"\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\20\2\2U \3\2\2\2\6\2HMR\3\b\2"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}