package chessHtml;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class CompileData {

	public static void useHtmlLinks() throws Exception {
		
		
		PrintWriter writerCsv = new PrintWriter(Main.fileName, "UTF-8");
		//PrintWriter writerMove = new PrintWriter("Move.csv", "UTF-8");
		String CurrentSourceCode;

		// reading html list into a string array
		List<String> records = new ArrayList<String>();
		//List<String> FENs = new ArrayList<String>();
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
		writerCsv.println("FEN,firstMove,secondMove, whoFirst");
		while (recordIndex < records.size()) {
			
			//loading...
			System.out.println(records.size() - recordIndex);
			CurrentSourceCode = HtmlSourceCode.getSource(records.get(recordIndex));

			writerCsv.print(FEN.search(CurrentSourceCode) + ", ");
			writerCsv.println(SolutionMove.search(CurrentSourceCode));
			recordIndex++;
		}
		writerCsv.close();
		//writerMove.close();
		// return null;
		System.out.println("Finished");

	}

}
