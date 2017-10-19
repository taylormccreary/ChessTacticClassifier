package chessHtml;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class GetFEN {

	public static void urlListToFEN() throws Exception {
		PrintWriter writerFEN = new PrintWriter("FEN.csv", "UTF-8");
		PrintWriter writerMove = new PrintWriter("Move.csv", "UTF-8");
		String CurrentSourceCode;
		// reading html list into a string array
		List<String> records = new ArrayList<String>();
		List<String> FENs = new ArrayList<String>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader("HtmlLinks.csv"));
			String line;
			while ((line = reader.readLine()) != null) {
				records.add(line);
			}
			reader.close();
		} catch (Exception e) {
			System.err.format("Exception occurred trying to read '%s'.", "HtmlLinks.csv");
			e.printStackTrace();
		}

		int recordIndex = 0;
		while (recordIndex < records.size()) {
			CurrentSourceCode = HtmlSourceCode.getSource(records.get(recordIndex));

			// System.out.println(records);
			writerFEN.println(FEN.search(CurrentSourceCode));
//			System.out.println(SolutionMove.search(CurrentSourceCode));
//			System.out.println(FEN.search(CurrentSourceCode));
			writerMove.println(SolutionMove.search(CurrentSourceCode));
			recordIndex++;
		}
		writerFEN.close();
		writerMove.close();
		// return null;

	}

}
