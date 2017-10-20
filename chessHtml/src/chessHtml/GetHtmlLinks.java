package chessHtml;

import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class GetHtmlLinks {
	
	public static void search() throws Exception, Exception {
		StringBuilder word = new StringBuilder();
		int arraySize = 0;
		int pageCount = 0;
		String onePositionList[] = new String[arraySize];

		// // you can change the name to .csv, or .txt, whatever format you want
		PrintWriter writer = new PrintWriter("HtmlLinks.csv", "UTF-8");

		// asking how many web pages you want to read
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter a number of web pages you want: ");
		int numberOfPages = reader.nextInt();
		reader.close();

		while (pageCount < numberOfPages) {
			pageCount++;
			word = word.append(
					HtmlSourceCode.getSource("https://www.chess.com/tactics/problems?tagId=11&page=" + pageCount));

			// finding the 1 indexes, and storing into a string array
			// could change this array to an integer array, would clean up the
			// code a bit
			int i = word.indexOf(">1</a>");
			while (i >= 0) {
				arraySize++;
				onePositionList = Arrays.copyOf(onePositionList, arraySize);
				onePositionList[arraySize - 1] = Integer.toString(i);
				i = word.indexOf(">1</a>", i + 1);
			}

			// getting url from the 1 positions
			for (int j = 0; j < onePositionList.length; j++) {

				// fixing a edge case, with a bad url
				if (!Character.isLetter(word.charAt(Integer.parseInt(onePositionList[j]) - 23))) {
					writer.println(word.substring(Integer.parseInt(onePositionList[j]) - 55,
							Integer.parseInt(onePositionList[j]) - 20));
				}
			}

		}
		writer.close();
		System.out.println("Finished loading HTML links");
	}

}
