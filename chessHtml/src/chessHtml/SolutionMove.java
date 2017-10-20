package chessHtml;

public class SolutionMove {

	public static String search(String htmlSourceCode) throws Exception, Exception {
		String move = "";


		// finding the solution move index

		int i = htmlSourceCode.indexOf("[MOVES");
		//need to remove "(int)."	"..."	"."		"&quot;" <--semicolons 
		move = htmlSourceCode.substring(i - 25, i -10);
		move = move.replaceAll("[0-9]+\\.", "");
		move = move.replaceAll("[a-z]+\\;", "");
		move = move.replaceAll("\\.+", "");
		move = move.replaceAll("\\&", "");
		move = move.trim();
		return move;
	}

}
