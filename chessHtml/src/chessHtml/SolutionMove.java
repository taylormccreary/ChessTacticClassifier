package chessHtml;

public class SolutionMove {

	public static String search(String htmlSourceCode) throws Exception, Exception {
		String move = "";
		String blackOrWhite = "white";

		// finding the solution move index

		int i = htmlSourceCode.indexOf("[MOVES");
		// removing "(int)." "..." "." "&quot;" <--semicolons
		move = htmlSourceCode.substring(i - 25, i - 10);
		move = move.replaceAll("[0-9]+\\.", "");
		move = move.replaceAll("[a-z]+\\;", "");
		move = move.replaceAll("\\&", "");

		// checking to see if the first move is black or white
		if (move.contains("...")) {
			move = move.replaceAll("\\.+", "");
			blackOrWhite = "black";
		} else
			// removing extra . when its white
			move = move.replaceAll("\\.+", "");
		move = move.trim();

		// adding a comma in between moves
		move = move.replace("  ", ", ");
		move = move.trim();
		move = move.replace(",", "");
		move = move.replace(" ", ", ");

		// adding the first players color
		move = move + ", " + blackOrWhite;
		return move;
	}

}
