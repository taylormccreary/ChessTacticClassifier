package chessHtml;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class FEN {

	public static String search(String htmlSourceCode) throws Exception, Exception {
		// public static void search() throws Exception, Exception {

		String board = "";

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

		System.out.println(htmlSourceCode.substring(indexStart, indexEnd));

		// move = htmlSourceCode.substring(i, i -10);
		// move = move.replaceAll("[0-9]+\\.", "");
		// move = move.replaceAll("[a-z]+\\;", "");
		// move = move.replaceAll("\\.+", "");
		// move = move.replaceAll("\\&", "");
		// move = move.trim();
		return htmlSourceCode.substring(indexStart, indexEnd);
	}

}
