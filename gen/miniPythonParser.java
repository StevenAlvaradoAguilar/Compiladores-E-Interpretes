// Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miniPythonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMA=1, PyCOMA=2, ASIGN=3, PIZQ=4, PDER=5, CIZQ=6, CDER=7, VIR=8, DOSPUNT=9, 
		MAS=10, MULT=11, MEN=12, DIV=13, POT=14, MOD=15, MENQUE=16, MAYQUE=17, 
		MENQUEEQUAL=18, MAYQUEEQUAL=19, EQUALEQUAL=20, MASEQUAL=21, MENEQUAL=22, 
		MULTEQUAL=23, DIVEQUAL=24, IF=25, THEN=26, ELSE=27, WHILE=28, DO=29, LET=30, 
		IN=31, BEGIN=32, END=33, DEF=34, LEN=35, FOR=36, RETURN=37, PRINT=38, 
		INTEGER=39, IDENTIFIER=40, STRING=41, FLOAT=42, CHARCONTS=43, COMENTLINEA=44, 
		COMENTMULTILINEA=45, NEWLINE=46, WS=47, INDENT=48, DEDENT=49;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_defStatement = 2, RULE_argList = 3, 
		RULE_moreArgs = 4, RULE_ifStatement = 5, RULE_whileStatement = 6, RULE_forStatement = 7, 
		RULE_returnStatement = 8, RULE_printStatement = 9, RULE_assignStatement = 10, 
		RULE_functionCallStatement = 11, RULE_expressionStatement = 12, RULE_sequence = 13, 
		RULE_moreStatements = 14, RULE_expression = 15, RULE_comparison = 16, 
		RULE_additionExpression = 17, RULE_additionFactor = 18, RULE_multiplicationExpression = 19, 
		RULE_multiplicationFactor = 20, RULE_elementExpression = 21, RULE_elementAccess = 22, 
		RULE_expressionList = 23, RULE_moreExpressions = 24, RULE_primitiveExpression = 25, 
		RULE_listExpression = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "defStatement", "argList", "moreArgs", "ifStatement", 
			"whileStatement", "forStatement", "returnStatement", "printStatement", 
			"assignStatement", "functionCallStatement", "expressionStatement", "sequence", 
			"moreStatements", "expression", "comparison", "additionExpression", "additionFactor", 
			"multiplicationExpression", "multiplicationFactor", "elementExpression", 
			"elementAccess", "expressionList", "moreExpressions", "primitiveExpression", 
			"listExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "';'", "'='", "'('", "')'", "'['", "']'", "'~'", "':'", 
			"'+'", "'*'", "'-'", "'/'", "'**'", "'%'", "'<'", "'>'", "'<='", "'>='", 
			"'=='", "'+='", "'-='", "'*='", "'/='", "'if'", "'then'", "'else'", "'while'", 
			"'do'", "'let'", "'in'", "'begin'", "'end'", "'def'", "'len'", "'for'", 
			"'return'", "'print'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMA", "PyCOMA", "ASIGN", "PIZQ", "PDER", "CIZQ", "CDER", "VIR", 
			"DOSPUNT", "MAS", "MULT", "MEN", "DIV", "POT", "MOD", "MENQUE", "MAYQUE", 
			"MENQUEEQUAL", "MAYQUEEQUAL", "EQUALEQUAL", "MASEQUAL", "MENEQUAL", "MULTEQUAL", 
			"DIVEQUAL", "IF", "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
			"END", "DEF", "LEN", "FOR", "RETURN", "PRINT", "INTEGER", "IDENTIFIER", 
			"STRING", "FLOAT", "CHARCONTS", "COMENTLINEA", "COMENTMULTILINEA", "NEWLINE", 
			"WS", "INDENT", "DEDENT"
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
	public String getGrammarFileName() { return "miniPython.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public miniPythonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProgramMPContext extends ProgramContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramMPContext(ProgramContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterProgramMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitProgramMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitProgramMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			_localctx = new ProgramMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			statement();
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PIZQ) | (1L << CIZQ) | (1L << MEN) | (1L << IF) | (1L << WHILE) | (1L << DEF) | (1L << LEN) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << INTEGER) | (1L << IDENTIFIER) | (1L << STRING) | (1L << FLOAT) | (1L << CHARCONTS) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(55);
				statement();
				}
				}
				setState(60);
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

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StatementMPContext extends StatementContext {
		public DefStatementContext defStatement() {
			return getRuleContext(DefStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public PrintStatementContext printStatement() {
			return getRuleContext(PrintStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public AssignStatementContext assignStatement() {
			return getRuleContext(AssignStatementContext.class,0);
		}
		public FunctionCallStatementContext functionCallStatement() {
			return getRuleContext(FunctionCallStatementContext.class,0);
		}
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public StatementMPContext(StatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			_localctx = new StatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(61);
				defStatement();
				}
				break;
			case 2:
				{
				setState(62);
				ifStatement();
				}
				break;
			case 3:
				{
				setState(63);
				returnStatement();
				}
				break;
			case 4:
				{
				setState(64);
				printStatement();
				}
				break;
			case 5:
				{
				setState(65);
				whileStatement();
				}
				break;
			case 6:
				{
				setState(66);
				forStatement();
				}
				break;
			case 7:
				{
				setState(67);
				assignStatement();
				}
				break;
			case 8:
				{
				setState(68);
				functionCallStatement();
				}
				break;
			case 9:
				{
				setState(69);
				expressionStatement();
				}
				break;
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

	public static class DefStatementContext extends ParserRuleContext {
		public DefStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defStatement; }
	 
		public DefStatementContext() { }
		public void copyFrom(DefStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class DefStatementMPContext extends DefStatementContext {
		public TerminalNode DEF() { return getToken(miniPythonParser.DEF, 0); }
		public TerminalNode IDENTIFIER() { return getToken(miniPythonParser.IDENTIFIER, 0); }
		public TerminalNode PIZQ() { return getToken(miniPythonParser.PIZQ, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TerminalNode PDER() { return getToken(miniPythonParser.PDER, 0); }
		public TerminalNode DOSPUNT() { return getToken(miniPythonParser.DOSPUNT, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public DefStatementMPContext(DefStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterDefStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitDefStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitDefStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DefStatementContext defStatement() throws RecognitionException {
		DefStatementContext _localctx = new DefStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_defStatement);
		try {
			_localctx = new DefStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(DEF);
			setState(73);
			match(IDENTIFIER);
			setState(74);
			match(PIZQ);
			setState(75);
			argList();
			setState(76);
			match(PDER);
			setState(77);
			match(DOSPUNT);
			setState(78);
			sequence();
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

	public static class ArgListContext extends ParserRuleContext {
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	 
		public ArgListContext() { }
		public void copyFrom(ArgListContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ArgListMPContext extends ArgListContext {
		public TerminalNode IDENTIFIER() { return getToken(miniPythonParser.IDENTIFIER, 0); }
		public MoreArgsContext moreArgs() {
			return getRuleContext(MoreArgsContext.class,0);
		}
		public ArgListMPContext(ArgListContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterArgListMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitArgListMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitArgListMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_argList);
		try {
			_localctx = new ArgListMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(80);
				match(IDENTIFIER);
				setState(81);
				moreArgs();
				}
				break;
			case PDER:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class MoreArgsContext extends ParserRuleContext {
		public MoreArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreArgs; }
	 
		public MoreArgsContext() { }
		public void copyFrom(MoreArgsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MoreArgsMPContext extends MoreArgsContext {
		public List<TerminalNode> COMA() { return getTokens(miniPythonParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(miniPythonParser.COMA, i);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(miniPythonParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(miniPythonParser.IDENTIFIER, i);
		}
		public MoreArgsMPContext(MoreArgsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterMoreArgsMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitMoreArgsMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitMoreArgsMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MoreArgsContext moreArgs() throws RecognitionException {
		MoreArgsContext _localctx = new MoreArgsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_moreArgs);
		int _la;
		try {
			_localctx = new MoreArgsMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(85);
				match(COMA);
				setState(86);
				match(IDENTIFIER);
				}
				}
				setState(91);
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

	public static class IfStatementContext extends ParserRuleContext {
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	 
		public IfStatementContext() { }
		public void copyFrom(IfStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IfStatementMPContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(miniPythonParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> DOSPUNT() { return getTokens(miniPythonParser.DOSPUNT); }
		public TerminalNode DOSPUNT(int i) {
			return getToken(miniPythonParser.DOSPUNT, i);
		}
		public List<SequenceContext> sequence() {
			return getRuleContexts(SequenceContext.class);
		}
		public SequenceContext sequence(int i) {
			return getRuleContext(SequenceContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(miniPythonParser.ELSE, 0); }
		public IfStatementMPContext(IfStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterIfStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitIfStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitIfStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ifStatement);
		try {
			_localctx = new IfStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(92);
				match(IF);
				setState(93);
				expression();
				setState(94);
				match(DOSPUNT);
				setState(95);
				sequence();
				setState(96);
				match(ELSE);
				setState(97);
				match(DOSPUNT);
				setState(98);
				sequence();
				}
				break;
			case 2:
				{
				setState(100);
				match(IF);
				setState(101);
				expression();
				setState(102);
				match(DOSPUNT);
				setState(103);
				sequence();
				}
				break;
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

	public static class WhileStatementContext extends ParserRuleContext {
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	 
		public WhileStatementContext() { }
		public void copyFrom(WhileStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class WhileStatementMPContext extends WhileStatementContext {
		public TerminalNode WHILE() { return getToken(miniPythonParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DOSPUNT() { return getToken(miniPythonParser.DOSPUNT, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public WhileStatementMPContext(WhileStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterWhileStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitWhileStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitWhileStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_whileStatement);
		try {
			_localctx = new WhileStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(WHILE);
			setState(108);
			expression();
			setState(109);
			match(DOSPUNT);
			setState(110);
			sequence();
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

	public static class ForStatementContext extends ParserRuleContext {
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	 
		public ForStatementContext() { }
		public void copyFrom(ForStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ForStatementMPContext extends ForStatementContext {
		public TerminalNode FOR() { return getToken(miniPythonParser.FOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode IN() { return getToken(miniPythonParser.IN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode DOSPUNT() { return getToken(miniPythonParser.DOSPUNT, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public ForStatementMPContext(ForStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterForStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitForStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitForStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forStatement);
		try {
			_localctx = new ForStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(FOR);
			setState(113);
			expression();
			setState(114);
			match(IN);
			setState(115);
			expressionList();
			setState(116);
			match(DOSPUNT);
			setState(117);
			sequence();
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

	public static class ReturnStatementContext extends ParserRuleContext {
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	 
		public ReturnStatementContext() { }
		public void copyFrom(ReturnStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ReturnStatementMPContext extends ReturnStatementContext {
		public TerminalNode RETURN() { return getToken(miniPythonParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miniPythonParser.NEWLINE, 0); }
		public ReturnStatementMPContext(ReturnStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterReturnStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitReturnStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitReturnStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_returnStatement);
		try {
			_localctx = new ReturnStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(RETURN);
			setState(120);
			expression();
			setState(121);
			match(NEWLINE);
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

	public static class PrintStatementContext extends ParserRuleContext {
		public PrintStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStatement; }
	 
		public PrintStatementContext() { }
		public void copyFrom(PrintStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintStatementMPContext extends PrintStatementContext {
		public TerminalNode PRINT() { return getToken(miniPythonParser.PRINT, 0); }
		public TerminalNode PIZQ() { return getToken(miniPythonParser.PIZQ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PDER() { return getToken(miniPythonParser.PDER, 0); }
		public TerminalNode NEWLINE() { return getToken(miniPythonParser.NEWLINE, 0); }
		public PrintStatementMPContext(PrintStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterPrintStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitPrintStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitPrintStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrintStatementContext printStatement() throws RecognitionException {
		PrintStatementContext _localctx = new PrintStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_printStatement);
		try {
			_localctx = new PrintStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(PRINT);
			setState(124);
			match(PIZQ);
			setState(125);
			expression();
			setState(126);
			match(PDER);
			setState(127);
			match(NEWLINE);
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

	public static class AssignStatementContext extends ParserRuleContext {
		public AssignStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStatement; }
	 
		public AssignStatementContext() { }
		public void copyFrom(AssignStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignStatementMPContext extends AssignStatementContext {
		public TerminalNode IDENTIFIER() { return getToken(miniPythonParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miniPythonParser.NEWLINE, 0); }
		public TerminalNode ASIGN() { return getToken(miniPythonParser.ASIGN, 0); }
		public TerminalNode MASEQUAL() { return getToken(miniPythonParser.MASEQUAL, 0); }
		public TerminalNode MENEQUAL() { return getToken(miniPythonParser.MENEQUAL, 0); }
		public AssignStatementMPContext(AssignStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterAssignStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitAssignStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitAssignStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignStatementContext assignStatement() throws RecognitionException {
		AssignStatementContext _localctx = new AssignStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignStatement);
		int _la;
		try {
			_localctx = new AssignStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(IDENTIFIER);
			setState(130);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ASIGN) | (1L << MASEQUAL) | (1L << MENEQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(131);
			expression();
			setState(132);
			match(NEWLINE);
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

	public static class FunctionCallStatementContext extends ParserRuleContext {
		public FunctionCallStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallStatement; }
	 
		public FunctionCallStatementContext() { }
		public void copyFrom(FunctionCallStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FunctionCallStatementMPContext extends FunctionCallStatementContext {
		public PrimitiveExpressionContext primitiveExpression() {
			return getRuleContext(PrimitiveExpressionContext.class,0);
		}
		public TerminalNode PIZQ() { return getToken(miniPythonParser.PIZQ, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode PDER() { return getToken(miniPythonParser.PDER, 0); }
		public TerminalNode NEWLINE() { return getToken(miniPythonParser.NEWLINE, 0); }
		public FunctionCallStatementMPContext(FunctionCallStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterFunctionCallStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitFunctionCallStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitFunctionCallStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionCallStatementContext functionCallStatement() throws RecognitionException {
		FunctionCallStatementContext _localctx = new FunctionCallStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_functionCallStatement);
		try {
			_localctx = new FunctionCallStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			primitiveExpression();
			setState(135);
			match(PIZQ);
			setState(136);
			expressionList();
			setState(137);
			match(PDER);
			setState(138);
			match(NEWLINE);
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

	public static class ExpressionStatementContext extends ParserRuleContext {
		public ExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStatement; }
	 
		public ExpressionStatementContext() { }
		public void copyFrom(ExpressionStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExpressionStatementMPContext extends ExpressionStatementContext {
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miniPythonParser.NEWLINE, 0); }
		public ExpressionStatementMPContext(ExpressionStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterExpressionStatementMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitExpressionStatementMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitExpressionStatementMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionStatementContext expressionStatement() throws RecognitionException {
		ExpressionStatementContext _localctx = new ExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expressionStatement);
		try {
			_localctx = new ExpressionStatementMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			expressionList();
			setState(141);
			match(NEWLINE);
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

	public static class SequenceContext extends ParserRuleContext {
		public SequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence; }
	 
		public SequenceContext() { }
		public void copyFrom(SequenceContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SequenceMPContext extends SequenceContext {
		public TerminalNode INDENT() { return getToken(miniPythonParser.INDENT, 0); }
		public MoreStatementsContext moreStatements() {
			return getRuleContext(MoreStatementsContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(miniPythonParser.DEDENT, 0); }
		public SequenceMPContext(SequenceContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterSequenceMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitSequenceMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitSequenceMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SequenceContext sequence() throws RecognitionException {
		SequenceContext _localctx = new SequenceContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_sequence);
		try {
			_localctx = new SequenceMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(INDENT);
			setState(144);
			moreStatements();
			setState(145);
			match(DEDENT);
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

	public static class MoreStatementsContext extends ParserRuleContext {
		public MoreStatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreStatements; }
	 
		public MoreStatementsContext() { }
		public void copyFrom(MoreStatementsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MoreStatementsMPContext extends MoreStatementsContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MoreStatementsMPContext(MoreStatementsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterMoreStatementsMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitMoreStatementsMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitMoreStatementsMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MoreStatementsContext moreStatements() throws RecognitionException {
		MoreStatementsContext _localctx = new MoreStatementsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_moreStatements);
		int _la;
		try {
			_localctx = new MoreStatementsMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(148); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(147);
				statement();
				}
				}
				setState(150); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PIZQ) | (1L << CIZQ) | (1L << MEN) | (1L << IF) | (1L << WHILE) | (1L << DEF) | (1L << LEN) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << INTEGER) | (1L << IDENTIFIER) | (1L << STRING) | (1L << FLOAT) | (1L << CHARCONTS) | (1L << NEWLINE))) != 0) );
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

	public static class ExpressionContext extends ParserRuleContext {
		public AdditionExpressionContext additionExpression() {
			return getRuleContext(AdditionExpressionContext.class,0);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			additionExpression();
			setState(153);
			comparison();
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

	public static class ComparisonContext extends ParserRuleContext {
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	 
		public ComparisonContext() { }
		public void copyFrom(ComparisonContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ComparisonMPContext extends ComparisonContext {
		public List<AdditionExpressionContext> additionExpression() {
			return getRuleContexts(AdditionExpressionContext.class);
		}
		public AdditionExpressionContext additionExpression(int i) {
			return getRuleContext(AdditionExpressionContext.class,i);
		}
		public List<TerminalNode> MENQUE() { return getTokens(miniPythonParser.MENQUE); }
		public TerminalNode MENQUE(int i) {
			return getToken(miniPythonParser.MENQUE, i);
		}
		public List<TerminalNode> MAYQUE() { return getTokens(miniPythonParser.MAYQUE); }
		public TerminalNode MAYQUE(int i) {
			return getToken(miniPythonParser.MAYQUE, i);
		}
		public List<TerminalNode> MENQUEEQUAL() { return getTokens(miniPythonParser.MENQUEEQUAL); }
		public TerminalNode MENQUEEQUAL(int i) {
			return getToken(miniPythonParser.MENQUEEQUAL, i);
		}
		public List<TerminalNode> MAYQUEEQUAL() { return getTokens(miniPythonParser.MAYQUEEQUAL); }
		public TerminalNode MAYQUEEQUAL(int i) {
			return getToken(miniPythonParser.MAYQUEEQUAL, i);
		}
		public List<TerminalNode> MULTEQUAL() { return getTokens(miniPythonParser.MULTEQUAL); }
		public TerminalNode MULTEQUAL(int i) {
			return getToken(miniPythonParser.MULTEQUAL, i);
		}
		public List<TerminalNode> DIVEQUAL() { return getTokens(miniPythonParser.DIVEQUAL); }
		public TerminalNode DIVEQUAL(int i) {
			return getToken(miniPythonParser.DIVEQUAL, i);
		}
		public List<TerminalNode> EQUALEQUAL() { return getTokens(miniPythonParser.EQUALEQUAL); }
		public TerminalNode EQUALEQUAL(int i) {
			return getToken(miniPythonParser.EQUALEQUAL, i);
		}
		public ComparisonMPContext(ComparisonContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterComparisonMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitComparisonMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitComparisonMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_comparison);
		int _la;
		try {
			_localctx = new ComparisonMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MENQUE) | (1L << MAYQUE) | (1L << MENQUEEQUAL) | (1L << MAYQUEEQUAL) | (1L << EQUALEQUAL) | (1L << MULTEQUAL) | (1L << DIVEQUAL))) != 0)) {
				{
				{
				setState(155);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MENQUE) | (1L << MAYQUE) | (1L << MENQUEEQUAL) | (1L << MAYQUEEQUAL) | (1L << EQUALEQUAL) | (1L << MULTEQUAL) | (1L << DIVEQUAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(156);
				additionExpression();
				}
				}
				setState(161);
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

	public static class AdditionExpressionContext extends ParserRuleContext {
		public AdditionExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additionExpression; }
	 
		public AdditionExpressionContext() { }
		public void copyFrom(AdditionExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AdditionExpressionMPContext extends AdditionExpressionContext {
		public MultiplicationExpressionContext multiplicationExpression() {
			return getRuleContext(MultiplicationExpressionContext.class,0);
		}
		public AdditionFactorContext additionFactor() {
			return getRuleContext(AdditionFactorContext.class,0);
		}
		public AdditionExpressionMPContext(AdditionExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterAdditionExpressionMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitAdditionExpressionMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitAdditionExpressionMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AdditionExpressionContext additionExpression() throws RecognitionException {
		AdditionExpressionContext _localctx = new AdditionExpressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_additionExpression);
		try {
			_localctx = new AdditionExpressionMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			multiplicationExpression();
			setState(163);
			additionFactor();
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

	public static class AdditionFactorContext extends ParserRuleContext {
		public AdditionFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additionFactor; }
	 
		public AdditionFactorContext() { }
		public void copyFrom(AdditionFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AdditionFactorMPContext extends AdditionFactorContext {
		public List<MultiplicationExpressionContext> multiplicationExpression() {
			return getRuleContexts(MultiplicationExpressionContext.class);
		}
		public MultiplicationExpressionContext multiplicationExpression(int i) {
			return getRuleContext(MultiplicationExpressionContext.class,i);
		}
		public List<TerminalNode> MAS() { return getTokens(miniPythonParser.MAS); }
		public TerminalNode MAS(int i) {
			return getToken(miniPythonParser.MAS, i);
		}
		public List<TerminalNode> MEN() { return getTokens(miniPythonParser.MEN); }
		public TerminalNode MEN(int i) {
			return getToken(miniPythonParser.MEN, i);
		}
		public AdditionFactorMPContext(AdditionFactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterAdditionFactorMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitAdditionFactorMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitAdditionFactorMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AdditionFactorContext additionFactor() throws RecognitionException {
		AdditionFactorContext _localctx = new AdditionFactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_additionFactor);
		int _la;
		try {
			_localctx = new AdditionFactorMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MAS || _la==MEN) {
				{
				{
				setState(165);
				_la = _input.LA(1);
				if ( !(_la==MAS || _la==MEN) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(166);
				multiplicationExpression();
				}
				}
				setState(171);
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

	public static class MultiplicationExpressionContext extends ParserRuleContext {
		public MultiplicationExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicationExpression; }
	 
		public MultiplicationExpressionContext() { }
		public void copyFrom(MultiplicationExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultiplicationExpressionMPContext extends MultiplicationExpressionContext {
		public ElementExpressionContext elementExpression() {
			return getRuleContext(ElementExpressionContext.class,0);
		}
		public MultiplicationFactorContext multiplicationFactor() {
			return getRuleContext(MultiplicationFactorContext.class,0);
		}
		public MultiplicationExpressionMPContext(MultiplicationExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterMultiplicationExpressionMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitMultiplicationExpressionMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitMultiplicationExpressionMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MultiplicationExpressionContext multiplicationExpression() throws RecognitionException {
		MultiplicationExpressionContext _localctx = new MultiplicationExpressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_multiplicationExpression);
		try {
			_localctx = new MultiplicationExpressionMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			elementExpression();
			setState(173);
			multiplicationFactor();
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

	public static class MultiplicationFactorContext extends ParserRuleContext {
		public MultiplicationFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicationFactor; }
	 
		public MultiplicationFactorContext() { }
		public void copyFrom(MultiplicationFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultiplicationFactorMPContext extends MultiplicationFactorContext {
		public List<ElementExpressionContext> elementExpression() {
			return getRuleContexts(ElementExpressionContext.class);
		}
		public ElementExpressionContext elementExpression(int i) {
			return getRuleContext(ElementExpressionContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(miniPythonParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(miniPythonParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(miniPythonParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(miniPythonParser.DIV, i);
		}
		public MultiplicationFactorMPContext(MultiplicationFactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterMultiplicationFactorMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitMultiplicationFactorMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitMultiplicationFactorMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MultiplicationFactorContext multiplicationFactor() throws RecognitionException {
		MultiplicationFactorContext _localctx = new MultiplicationFactorContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_multiplicationFactor);
		int _la;
		try {
			_localctx = new MultiplicationFactorMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(175);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(176);
				elementExpression();
				}
				}
				setState(181);
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

	public static class ElementExpressionContext extends ParserRuleContext {
		public ElementExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementExpression; }
	 
		public ElementExpressionContext() { }
		public void copyFrom(ElementExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ElementExpressionMPContext extends ElementExpressionContext {
		public PrimitiveExpressionContext primitiveExpression() {
			return getRuleContext(PrimitiveExpressionContext.class,0);
		}
		public ElementAccessContext elementAccess() {
			return getRuleContext(ElementAccessContext.class,0);
		}
		public ElementExpressionMPContext(ElementExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterElementExpressionMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitElementExpressionMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitElementExpressionMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ElementExpressionContext elementExpression() throws RecognitionException {
		ElementExpressionContext _localctx = new ElementExpressionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_elementExpression);
		try {
			_localctx = new ElementExpressionMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(182);
				primitiveExpression();
				setState(183);
				elementAccess();
				}
				break;
			case 2:
				{
				setState(185);
				primitiveExpression();
				}
				break;
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

	public static class ElementAccessContext extends ParserRuleContext {
		public ElementAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementAccess; }
	 
		public ElementAccessContext() { }
		public void copyFrom(ElementAccessContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ElementAccessMPContext extends ElementAccessContext {
		public List<TerminalNode> CIZQ() { return getTokens(miniPythonParser.CIZQ); }
		public TerminalNode CIZQ(int i) {
			return getToken(miniPythonParser.CIZQ, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CDER() { return getTokens(miniPythonParser.CDER); }
		public TerminalNode CDER(int i) {
			return getToken(miniPythonParser.CDER, i);
		}
		public ElementAccessMPContext(ElementAccessContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterElementAccessMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitElementAccessMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitElementAccessMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ElementAccessContext elementAccess() throws RecognitionException {
		ElementAccessContext _localctx = new ElementAccessContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_elementAccess);
		int _la;
		try {
			_localctx = new ElementAccessMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(192); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(188);
				match(CIZQ);
				setState(189);
				expression();
				setState(190);
				match(CDER);
				}
				}
				setState(194); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CIZQ );
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

	public static class ExpressionListContext extends ParserRuleContext {
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
	 
		public ExpressionListContext() { }
		public void copyFrom(ExpressionListContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExpressionListMPContext extends ExpressionListContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public MoreExpressionsContext moreExpressions() {
			return getRuleContext(MoreExpressionsContext.class,0);
		}
		public ExpressionListMPContext(ExpressionListContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterExpressionListMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitExpressionListMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitExpressionListMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expressionList);
		try {
			_localctx = new ExpressionListMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PIZQ:
			case CIZQ:
			case MEN:
			case LEN:
			case INTEGER:
			case IDENTIFIER:
			case STRING:
			case FLOAT:
			case CHARCONTS:
				{
				setState(196);
				expression();
				setState(197);
				moreExpressions();
				}
				break;
			case PDER:
			case CDER:
			case DOSPUNT:
			case NEWLINE:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class MoreExpressionsContext extends ParserRuleContext {
		public MoreExpressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreExpressions; }
	 
		public MoreExpressionsContext() { }
		public void copyFrom(MoreExpressionsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MoreExpressionsMPContext extends MoreExpressionsContext {
		public List<TerminalNode> COMA() { return getTokens(miniPythonParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(miniPythonParser.COMA, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MoreExpressionsMPContext(MoreExpressionsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterMoreExpressionsMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitMoreExpressionsMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitMoreExpressionsMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MoreExpressionsContext moreExpressions() throws RecognitionException {
		MoreExpressionsContext _localctx = new MoreExpressionsContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_moreExpressions);
		int _la;
		try {
			_localctx = new MoreExpressionsMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(202);
				match(COMA);
				setState(203);
				expression();
				}
				}
				setState(208);
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

	public static class PrimitiveExpressionContext extends ParserRuleContext {
		public PrimitiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveExpression; }
	 
		public PrimitiveExpressionContext() { }
		public void copyFrom(PrimitiveExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrimitiveExpressionMPContext extends PrimitiveExpressionContext {
		public TerminalNode INTEGER() { return getToken(miniPythonParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(miniPythonParser.FLOAT, 0); }
		public TerminalNode CHARCONTS() { return getToken(miniPythonParser.CHARCONTS, 0); }
		public TerminalNode STRING() { return getToken(miniPythonParser.STRING, 0); }
		public TerminalNode IDENTIFIER() { return getToken(miniPythonParser.IDENTIFIER, 0); }
		public TerminalNode PIZQ() { return getToken(miniPythonParser.PIZQ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PDER() { return getToken(miniPythonParser.PDER, 0); }
		public ListExpressionContext listExpression() {
			return getRuleContext(ListExpressionContext.class,0);
		}
		public TerminalNode LEN() { return getToken(miniPythonParser.LEN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode MEN() { return getToken(miniPythonParser.MEN, 0); }
		public PrimitiveExpressionMPContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterPrimitiveExpressionMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitPrimitiveExpressionMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitPrimitiveExpressionMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrimitiveExpressionContext primitiveExpression() throws RecognitionException {
		PrimitiveExpressionContext _localctx = new PrimitiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_primitiveExpression);
		int _la;
		try {
			_localctx = new PrimitiveExpressionMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==MEN) {
					{
					setState(209);
					match(MEN);
					}
				}

				setState(212);
				match(INTEGER);
				}
				break;
			case 2:
				{
				setState(214);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==MEN) {
					{
					setState(213);
					match(MEN);
					}
				}

				setState(216);
				match(FLOAT);
				}
				break;
			case 3:
				{
				setState(217);
				match(CHARCONTS);
				}
				break;
			case 4:
				{
				setState(218);
				match(STRING);
				}
				break;
			case 5:
				{
				setState(219);
				match(IDENTIFIER);
				setState(225);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
				case 1:
					{
					setState(220);
					match(PIZQ);
					setState(221);
					expressionList();
					setState(222);
					match(PDER);
					}
					break;
				case 2:
					{
					}
					break;
				}
				}
				break;
			case 6:
				{
				setState(227);
				match(PIZQ);
				setState(228);
				expression();
				setState(229);
				match(PDER);
				}
				break;
			case 7:
				{
				setState(231);
				listExpression();
				}
				break;
			case 8:
				{
				setState(232);
				match(LEN);
				setState(233);
				match(PIZQ);
				setState(234);
				expression();
				setState(235);
				match(PDER);
				}
				break;
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

	public static class ListExpressionContext extends ParserRuleContext {
		public ListExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listExpression; }
	 
		public ListExpressionContext() { }
		public void copyFrom(ListExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ListExpressionMPContext extends ListExpressionContext {
		public TerminalNode CIZQ() { return getToken(miniPythonParser.CIZQ, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode CDER() { return getToken(miniPythonParser.CDER, 0); }
		public ListExpressionMPContext(ListExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).enterListExpressionMP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof miniPythonListener ) ((miniPythonListener)listener).exitListExpressionMP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof miniPythonVisitor ) return ((miniPythonVisitor<? extends T>)visitor).visitListExpressionMP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListExpressionContext listExpression() throws RecognitionException {
		ListExpressionContext _localctx = new ListExpressionContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_listExpression);
		try {
			_localctx = new ListExpressionMPContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(CIZQ);
			setState(240);
			expressionList();
			setState(241);
			match(CDER);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u00f6\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\7\2;\n\2\f\2\16\2>\13\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3I\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\5\5V\n\5\3\6\3\6\7\6Z\n\6\f\6\16\6]\13\6\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7l\n\7\3\b\3\b\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\20\6\20\u0097\n\20\r\20\16\20\u0098\3\21\3\21\3\21\3\22\3"+
		"\22\7\22\u00a0\n\22\f\22\16\22\u00a3\13\22\3\23\3\23\3\23\3\24\3\24\7"+
		"\24\u00aa\n\24\f\24\16\24\u00ad\13\24\3\25\3\25\3\25\3\26\3\26\7\26\u00b4"+
		"\n\26\f\26\16\26\u00b7\13\26\3\27\3\27\3\27\3\27\5\27\u00bd\n\27\3\30"+
		"\3\30\3\30\3\30\6\30\u00c3\n\30\r\30\16\30\u00c4\3\31\3\31\3\31\3\31\5"+
		"\31\u00cb\n\31\3\32\3\32\7\32\u00cf\n\32\f\32\16\32\u00d2\13\32\3\33\5"+
		"\33\u00d5\n\33\3\33\3\33\5\33\u00d9\n\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\5\33\u00e4\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\5\33\u00f0\n\33\3\34\3\34\3\34\3\34\3\34\2\2\35\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2\6\4\2\5\5\27\30\4\2"+
		"\22\26\31\32\4\2\f\f\16\16\4\2\r\r\17\17\2\u00f8\28\3\2\2\2\4H\3\2\2\2"+
		"\6J\3\2\2\2\bU\3\2\2\2\n[\3\2\2\2\fk\3\2\2\2\16m\3\2\2\2\20r\3\2\2\2\22"+
		"y\3\2\2\2\24}\3\2\2\2\26\u0083\3\2\2\2\30\u0088\3\2\2\2\32\u008e\3\2\2"+
		"\2\34\u0091\3\2\2\2\36\u0096\3\2\2\2 \u009a\3\2\2\2\"\u00a1\3\2\2\2$\u00a4"+
		"\3\2\2\2&\u00ab\3\2\2\2(\u00ae\3\2\2\2*\u00b5\3\2\2\2,\u00bc\3\2\2\2."+
		"\u00c2\3\2\2\2\60\u00ca\3\2\2\2\62\u00d0\3\2\2\2\64\u00ef\3\2\2\2\66\u00f1"+
		"\3\2\2\28<\5\4\3\29;\5\4\3\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2="+
		"\3\3\2\2\2><\3\2\2\2?I\5\6\4\2@I\5\f\7\2AI\5\22\n\2BI\5\24\13\2CI\5\16"+
		"\b\2DI\5\20\t\2EI\5\26\f\2FI\5\30\r\2GI\5\32\16\2H?\3\2\2\2H@\3\2\2\2"+
		"HA\3\2\2\2HB\3\2\2\2HC\3\2\2\2HD\3\2\2\2HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2"+
		"I\5\3\2\2\2JK\7$\2\2KL\7*\2\2LM\7\6\2\2MN\5\b\5\2NO\7\7\2\2OP\7\13\2\2"+
		"PQ\5\34\17\2Q\7\3\2\2\2RS\7*\2\2SV\5\n\6\2TV\3\2\2\2UR\3\2\2\2UT\3\2\2"+
		"\2V\t\3\2\2\2WX\7\3\2\2XZ\7*\2\2YW\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2"+
		"\2\2\\\13\3\2\2\2][\3\2\2\2^_\7\33\2\2_`\5 \21\2`a\7\13\2\2ab\5\34\17"+
		"\2bc\7\35\2\2cd\7\13\2\2de\5\34\17\2el\3\2\2\2fg\7\33\2\2gh\5 \21\2hi"+
		"\7\13\2\2ij\5\34\17\2jl\3\2\2\2k^\3\2\2\2kf\3\2\2\2l\r\3\2\2\2mn\7\36"+
		"\2\2no\5 \21\2op\7\13\2\2pq\5\34\17\2q\17\3\2\2\2rs\7&\2\2st\5 \21\2t"+
		"u\7!\2\2uv\5\60\31\2vw\7\13\2\2wx\5\34\17\2x\21\3\2\2\2yz\7\'\2\2z{\5"+
		" \21\2{|\7\60\2\2|\23\3\2\2\2}~\7(\2\2~\177\7\6\2\2\177\u0080\5 \21\2"+
		"\u0080\u0081\7\7\2\2\u0081\u0082\7\60\2\2\u0082\25\3\2\2\2\u0083\u0084"+
		"\7*\2\2\u0084\u0085\t\2\2\2\u0085\u0086\5 \21\2\u0086\u0087\7\60\2\2\u0087"+
		"\27\3\2\2\2\u0088\u0089\5\64\33\2\u0089\u008a\7\6\2\2\u008a\u008b\5\60"+
		"\31\2\u008b\u008c\7\7\2\2\u008c\u008d\7\60\2\2\u008d\31\3\2\2\2\u008e"+
		"\u008f\5\60\31\2\u008f\u0090\7\60\2\2\u0090\33\3\2\2\2\u0091\u0092\7\62"+
		"\2\2\u0092\u0093\5\36\20\2\u0093\u0094\7\63\2\2\u0094\35\3\2\2\2\u0095"+
		"\u0097\5\4\3\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2"+
		"\2\2\u0098\u0099\3\2\2\2\u0099\37\3\2\2\2\u009a\u009b\5$\23\2\u009b\u009c"+
		"\5\"\22\2\u009c!\3\2\2\2\u009d\u009e\t\3\2\2\u009e\u00a0\5$\23\2\u009f"+
		"\u009d\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2"+
		"\2\2\u00a2#\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5(\25\2\u00a5\u00a6"+
		"\5&\24\2\u00a6%\3\2\2\2\u00a7\u00a8\t\4\2\2\u00a8\u00aa\5(\25\2\u00a9"+
		"\u00a7\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2"+
		"\2\2\u00ac\'\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\5,\27\2\u00af\u00b0"+
		"\5*\26\2\u00b0)\3\2\2\2\u00b1\u00b2\t\5\2\2\u00b2\u00b4\5,\27\2\u00b3"+
		"\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2"+
		"\2\2\u00b6+\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5\64\33\2\u00b9\u00ba"+
		"\5.\30\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\5\64\33\2\u00bc\u00b8\3\2\2\2"+
		"\u00bc\u00bb\3\2\2\2\u00bd-\3\2\2\2\u00be\u00bf\7\b\2\2\u00bf\u00c0\5"+
		" \21\2\u00c0\u00c1\7\t\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00be\3\2\2\2\u00c3"+
		"\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5/\3\2\2\2"+
		"\u00c6\u00c7\5 \21\2\u00c7\u00c8\5\62\32\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb"+
		"\3\2\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\61\3\2\2\2\u00cc"+
		"\u00cd\7\3\2\2\u00cd\u00cf\5 \21\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2"+
		"\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\63\3\2\2\2\u00d2\u00d0"+
		"\3\2\2\2\u00d3\u00d5\7\16\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2"+
		"\u00d5\u00d6\3\2\2\2\u00d6\u00f0\7)\2\2\u00d7\u00d9\7\16\2\2\u00d8\u00d7"+
		"\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00f0\7,\2\2\u00db"+
		"\u00f0\7-\2\2\u00dc\u00f0\7+\2\2\u00dd\u00e3\7*\2\2\u00de\u00df\7\6\2"+
		"\2\u00df\u00e0\5\60\31\2\u00e0\u00e1\7\7\2\2\u00e1\u00e4\3\2\2\2\u00e2"+
		"\u00e4\3\2\2\2\u00e3\u00de\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00f0\3\2"+
		"\2\2\u00e5\u00e6\7\6\2\2\u00e6\u00e7\5 \21\2\u00e7\u00e8\7\7\2\2\u00e8"+
		"\u00f0\3\2\2\2\u00e9\u00f0\5\66\34\2\u00ea\u00eb\7%\2\2\u00eb\u00ec\7"+
		"\6\2\2\u00ec\u00ed\5 \21\2\u00ed\u00ee\7\7\2\2\u00ee\u00f0\3\2\2\2\u00ef"+
		"\u00d4\3\2\2\2\u00ef\u00d8\3\2\2\2\u00ef\u00db\3\2\2\2\u00ef\u00dc\3\2"+
		"\2\2\u00ef\u00dd\3\2\2\2\u00ef\u00e5\3\2\2\2\u00ef\u00e9\3\2\2\2\u00ef"+
		"\u00ea\3\2\2\2\u00f0\65\3\2\2\2\u00f1\u00f2\7\b\2\2\u00f2\u00f3\5\60\31"+
		"\2\u00f3\u00f4\7\t\2\2\u00f4\67\3\2\2\2\23<HU[k\u0098\u00a1\u00ab\u00b5"+
		"\u00bc\u00c4\u00ca\u00d0\u00d4\u00d8\u00e3\u00ef";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}