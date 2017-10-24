package chessHtml;

public class FEN {

	public static String search(String htmlSourceCode) throws Exception, Exception {

		// finding the solution move index

		int indexStart = htmlSourceCode.indexOf("initialSetup")+15;
		int indexPointer = indexStart;
		;
		int indexEnd;

		for (int j = 0; j < 7; j++) {

			while (htmlSourceCode.charAt(indexPointer) != '/')
				indexPointer++;
			indexPointer++;
		}
		while (htmlSourceCode.charAt(indexPointer) != ' ')
			indexPointer++;
		indexEnd = indexPointer;

		//System.out.println(htmlSourceCode.substring(indexStart, indexEnd));

		return htmlSourceCode.substring(indexStart, indexEnd);
	}

}
