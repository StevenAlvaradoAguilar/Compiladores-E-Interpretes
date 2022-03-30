// Generated from D:/Universidad/Compiladores_e_Interpretes/Compiladores-E-Interpretes/Compiladores-E-Interpretes/mini-python\miniPython.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link miniPythonParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface miniPythonVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by the {@code programMP}
	 * labeled alternative in {@link miniPythonParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgramMP(miniPythonParser.ProgramMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code statementMP}
	 * labeled alternative in {@link miniPythonParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatementMP(miniPythonParser.StatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code defStatementMP}
	 * labeled alternative in {@link miniPythonParser#defStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefStatementMP(miniPythonParser.DefStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code argListMP}
	 * labeled alternative in {@link miniPythonParser#argList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgListMP(miniPythonParser.ArgListMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code moreArgsMP}
	 * labeled alternative in {@link miniPythonParser#moreArgs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMoreArgsMP(miniPythonParser.MoreArgsMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ifStatementMP}
	 * labeled alternative in {@link miniPythonParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatementMP(miniPythonParser.IfStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code whileStatementMP}
	 * labeled alternative in {@link miniPythonParser#whileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatementMP(miniPythonParser.WhileStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code forStatementMP}
	 * labeled alternative in {@link miniPythonParser#forStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatementMP(miniPythonParser.ForStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code returnStatementMP}
	 * labeled alternative in {@link miniPythonParser#returnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatementMP(miniPythonParser.ReturnStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code printStatementMP}
	 * labeled alternative in {@link miniPythonParser#printStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintStatementMP(miniPythonParser.PrintStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code assignStatementMP}
	 * labeled alternative in {@link miniPythonParser#assignStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignStatementMP(miniPythonParser.AssignStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code functionCallStatementMP}
	 * labeled alternative in {@link miniPythonParser#functionCallStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCallStatementMP(miniPythonParser.FunctionCallStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionStatementMP}
	 * labeled alternative in {@link miniPythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionStatementMP(miniPythonParser.ExpressionStatementMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sequenceMP}
	 * labeled alternative in {@link miniPythonParser#sequence}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSequenceMP(miniPythonParser.SequenceMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code moreStatementsMP}
	 * labeled alternative in {@link miniPythonParser#moreStatements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMoreStatementsMP(miniPythonParser.MoreStatementsMPContext ctx);
	/**
	 * Visit a parse tree produced by {@link miniPythonParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(miniPythonParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code comparisonMP}
	 * labeled alternative in {@link miniPythonParser#comparison}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparisonMP(miniPythonParser.ComparisonMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code additionExpressionMP}
	 * labeled alternative in {@link miniPythonParser#additionExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditionExpressionMP(miniPythonParser.AdditionExpressionMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code additionFactorMP}
	 * labeled alternative in {@link miniPythonParser#additionFactor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditionFactorMP(miniPythonParser.AdditionFactorMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code multiplicationExpressionMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicationExpressionMP(miniPythonParser.MultiplicationExpressionMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code multiplicationFactorMP}
	 * labeled alternative in {@link miniPythonParser#multiplicationFactor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicationFactorMP(miniPythonParser.MultiplicationFactorMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code elementExpressionMP}
	 * labeled alternative in {@link miniPythonParser#elementExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElementExpressionMP(miniPythonParser.ElementExpressionMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code elementAccessMP}
	 * labeled alternative in {@link miniPythonParser#elementAccess}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElementAccessMP(miniPythonParser.ElementAccessMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionListMP}
	 * labeled alternative in {@link miniPythonParser#expressionList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionListMP(miniPythonParser.ExpressionListMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code moreExpressionsMP}
	 * labeled alternative in {@link miniPythonParser#moreExpressions}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMoreExpressionsMP(miniPythonParser.MoreExpressionsMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code primitiveExpressionMP}
	 * labeled alternative in {@link miniPythonParser#primitiveExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitiveExpressionMP(miniPythonParser.PrimitiveExpressionMPContext ctx);
	/**
	 * Visit a parse tree produced by the {@code listExpressionMP}
	 * labeled alternative in {@link miniPythonParser#listExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListExpressionMP(miniPythonParser.ListExpressionMPContext ctx);
}