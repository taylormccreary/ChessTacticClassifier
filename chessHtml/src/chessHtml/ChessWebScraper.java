package chessHtml;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.lang.StringBuilder;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Scanner;

public class ChessWebScraper {

	// public static void main(String[] args) throws Exception, Exception {

	public static void webScrapeUrlList() throws Exception, Exception {

		// StringBuilder word = new StringBuilder();
		StringBuilder word = new StringBuilder();
		URL url;
		BufferedReader br;
		String line;
		InputStream is = null;
		int arraySize = 0;
		int pageCount = 0;
		String onePositionList[] = new String[arraySize];

		// you can change the name to .csv, or .txt, whatever format you want
		PrintWriter writer = new PrintWriter("HtmlLinks.csv", "UTF-8");

		// asking how many web pages you want to read
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter a number of web pages you want: ");
		int numberOfPages = reader.nextInt();
		reader.close();

		while (pageCount < numberOfPages) {
			pageCount++;
			System.out.println(pageCount);

			 // getting html source code and throwing it into a stringbuilder
			 try {
			 url = new
			 URL("https://www.chess.com/tactics/problems?tagId=11&page=" +
			 pageCount);
			 HttpURLConnection httpcon = (HttpURLConnection)
			 url.openConnection();
			 httpcon.addRequestProperty("User-Agent", "Mozilla/4.0");
			
			 is = httpcon.getInputStream();
			 br = new BufferedReader(new InputStreamReader(is));
			
			 while ((line = br.readLine()) != null) {
			 word = word.append(line);
			 }
			 } catch (IOException e) {
			 String error = e.toString();
			 throw new RuntimeException(e);
			 }
		//	word = HtmlSourceCode.getSource("https://www.chess.com/tactics/problems?tagId=11&page=" + pageCount);

			// finding the 1 indexes, and storing into a string array
			// could change this array to an integer array, would clean up the
			// code a bit
			int i = word.indexOf(">1</a>");
			while (i >= 0) {
				// System.out.println(i);
				arraySize++;
				onePositionList = Arrays.copyOf(onePositionList, arraySize);
				onePositionList[arraySize - 1] = Integer.toString(i);
				// System.out.println(Arrays.toString(onePositionList));
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
		System.out.println("Finished");
	}

}
