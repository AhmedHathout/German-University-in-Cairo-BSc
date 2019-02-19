// Generated from task_2_1.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link task_2_1Parser}.
 */
public interface task_2_1Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link task_2_1Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(task_2_1Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link task_2_1Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(task_2_1Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link task_2_1Parser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(task_2_1Parser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link task_2_1Parser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(task_2_1Parser.StartContext ctx);
}