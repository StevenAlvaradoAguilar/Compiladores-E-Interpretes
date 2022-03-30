// Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link miniPythonParser}.
 */
public interface miniPythonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code programMP}
	 * labeled alternative in {@link miniPythonParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgramMP(miniPythonParser.ProgramMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code programMP}
	 * labeled alternative in {@link miniPythonParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgramMP(miniPythonParser.ProgramMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code statementMP}
	 * labeled alternative in {@link miniPythonParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatementMP(miniPythonParser.StatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code statementMP}
	 * labeled alternative in {@link miniPythonParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatementMP(miniPythonParser.StatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code defStatementMP}
	 * labeled alternative in {@link miniPythonParser#defStatement}.
	 * @param ctx the parse tree
	 */
	void enterDefStatementMP(miniPythonParser.DefStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code defStatementMP}
	 * labeled alternative in {@link miniPythonParser#defStatement}.
	 * @param ctx the parse tree
	 */
	void exitDefStatementMP(miniPythonParser.DefStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code argListMP}
	 * labeled alternative in {@link miniPythonParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgListMP(miniPythonParser.ArgListMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code argListMP}
	 * labeled alternative in {@link miniPythonParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgListMP(miniPythonParser.ArgListMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code moreArgsMP}
	 * labeled alternative in {@link miniPythonParser#moreArgs}.
	 * @param ctx the parse tree
	 */
	void enterMoreArgsMP(miniPythonParser.MoreArgsMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code moreArgsMP}
	 * labeled alternative in {@link miniPythonParser#moreArgs}.
	 * @param ctx the parse tree
	 */
	void exitMoreArgsMP(miniPythonParser.MoreArgsMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStatementMP}
	 * labeled alternative in {@link miniPythonParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatementMP(miniPythonParser.IfStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStatementMP}
	 * labeled alternative in {@link miniPythonParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatementMP(miniPythonParser.IfStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStatementMP}
	 * labeled alternative in {@link miniPythonParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatementMP(miniPythonParser.WhileStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStatementMP}
	 * labeled alternative in {@link miniPythonParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatementMP(miniPythonParser.WhileStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forStatementMP}
	 * labeled alternative in {@link miniPythonParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatementMP(miniPythonParser.ForStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forStatementMP}
	 * labeled alternative in {@link miniPythonParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatementMP(miniPythonParser.ForStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnStatementMP}
	 * labeled alternative in {@link miniPythonParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatementMP(miniPythonParser.ReturnStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnStatementMP}
	 * labeled alternative in {@link miniPythonParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatementMP(miniPythonParser.ReturnStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStatementMP}
	 * labeled alternative in {@link miniPythonParser#printStatement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatementMP(miniPythonParser.PrintStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStatementMP}
	 * labeled alternative in {@link miniPythonParser#printStatement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatementMP(miniPythonParser.PrintStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignStatementMP}
	 * labeled alternative in {@link miniPythonParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStatementMP(miniPythonParser.AssignStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignStatementMP}
	 * labeled alternative in {@link miniPythonParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStatementMP(miniPythonParser.AssignStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionCallStatementMP}
	 * labeled alternative in {@link miniPythonParser#functionCallStatement}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallStatementMP(miniPythonParser.FunctionCallStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionCallStatementMP}
	 * labeled alternative in {@link miniPythonParser#functionCallStatement}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallStatementMP(miniPythonParser.FunctionCallStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionStatementMP}
	 * labeled alternative in {@link miniPythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatementMP(miniPythonParser.ExpressionStatementMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionStatementMP}
	 * labeled alternative in {@link miniPythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatementMP(miniPythonParser.ExpressionStatementMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sequenceMP}
	 * labeled alternative in {@link miniPythonParser#sequence}.
	 * @param ctx the parse tree
	 */
	void enterSequenceMP(miniPythonParser.SequenceMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sequenceMP}
	 * labeled alternative in {@link miniPythonParser#sequence}.
	 * @param ctx the parse tree
	 */
	void exitSequenceMP(miniPythonParser.SequenceMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code moreStatementsMP}
	 * labeled alternative in {@link miniPythonParser#moreStatements}.
	 * @param ctx the parse tree
	 */
	void enterMoreStatementsMP(miniPythonParser.MoreStatementsMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code moreStatementsMP}
	 * labeled alternative in {@link miniPythonParser#moreStatements}.
	 * @param ctx the parse tree
	 */
	void exitMoreStatementsMP(miniPythonParser.MoreStatementsMPContext ctx);
	/**
	 * Enter a parse tree produced by {@link miniPythonParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(miniPythonParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniPythonParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(miniPythonParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparisonMP}
	 * labeled alternative in {@link miniPythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparisonMP(miniPythonParser.ComparisonMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparisonMP}
	 * labeled alternative in {@link miniPythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparisonMP(miniPythonParser.ComparisonMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code additionExpressionMP}
	 * labeled alternative in {@link miniPythonParser#additionExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditionExpressionMP(miniPythonParser.AdditionExpressionMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code additionExpressionMP}
	 * labeled alternative in {@link miniPythonParser#additionExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditionExpressionMP(miniPythonParser.AdditionExpressionMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code additionFactorMP}
	 * labeled alternative in {@link miniPythonParser#additionFactor}.
	 * @param ctx the parse tree
	 */
	void enterAdditionFactorMP(miniPythonParser.AdditionFactorMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code additionFactorMP}
	 * labeled alternative in {@link miniPythonParser#additionFactor}.
	 * @param ctx the parse tree
	 */
	void exitAdditionFactorMP(miniPythonParser.AdditionFactorMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multiplicationExpressionMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicationExpressionMP(miniPythonParser.MultiplicationExpressionMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multiplicationExpressionMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicationExpressionMP(miniPythonParser.MultiplicationExpressionMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multiplicationFactorMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationFactor}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicationFactorMP(miniPythonParser.MultiplicationFactorMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multiplicationFactorMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationFactor}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicationFactorMP(miniPythonParser.MultiplicationFactorMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code elementExpressionMP}
	 * labeled alternative in {@link miniPythonParser#elementExpression}.
	 * @param ctx the parse tree
	 */
	void enterElementExpressionMP(miniPythonParser.ElementExpressionMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code elementExpressionMP}
	 * labeled alternative in {@link miniPythonParser#elementExpression}.
	 * @param ctx the parse tree
	 */
	void exitElementExpressionMP(miniPythonParser.ElementExpressionMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code elementAccessMP}
	 * labeled alternative in {@link miniPythonParser#elementAccess}.
	 * @param ctx the parse tree
	 */
	void enterElementAccessMP(miniPythonParser.ElementAccessMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code elementAccessMP}
	 * labeled alternative in {@link miniPythonParser#elementAccess}.
	 * @param ctx the parse tree
	 */
	void exitElementAccessMP(miniPythonParser.ElementAccessMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionListMP}
	 * labeled alternative in {@link miniPythonParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void enterExpressionListMP(miniPythonParser.ExpressionListMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionListMP}
	 * labeled alternative in {@link miniPythonParser#expressionList}.
	 * @param ctx the parse tree
	 */
	void exitExpressionListMP(miniPythonParser.ExpressionListMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code moreExpressionsMP}
	 * labeled alternative in {@link miniPythonParser#moreExpressions}.
	 * @param ctx the parse tree
	 */
	void enterMoreExpressionsMP(miniPythonParser.MoreExpressionsMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code moreExpressionsMP}
	 * labeled alternative in {@link miniPythonParser#moreExpressions}.
	 * @param ctx the parse tree
	 */
	void exitMoreExpressionsMP(miniPythonParser.MoreExpressionsMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primitiveExpressionMP}
	 * labeled alternative in {@link miniPythonParser#primitiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveExpressionMP(miniPythonParser.PrimitiveExpressionMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primitiveExpressionMP}
	 * labeled alternative in {@link miniPythonParser#primitiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveExpressionMP(miniPythonParser.PrimitiveExpressionMPContext ctx);
	/**
	 * Enter a parse tree produced by the {@code listExpressionMP}
	 * labeled alternative in {@link miniPythonParser#listExpression}.
	 * @param ctx the parse tree
	 */
	void enterListExpressionMP(miniPythonParser.ListExpressionMPContext ctx);
	/**
	 * Exit a parse tree produced by the {@code listExpressionMP}
	 * labeled alternative in {@link miniPythonParser#listExpression}.
	 * @param ctx the parse tree
	 */
	void exitListExpressionMP(miniPythonParser.ListExpressionMPContext ctx);
}