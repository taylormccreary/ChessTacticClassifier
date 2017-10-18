package chessHtml;

//import java.lang.*;
import java.io.BufferedReader;
//import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
//import java.io.UnsupportedEncodingException;
import java.lang.StringBuilder;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Scanner;

public class ChessWebScraper {

	public static void main(String[] args) throws Exception, Exception {
		StringBuilder word = new StringBuilder();
		URL url;
		BufferedReader br;
		String line;
		InputStream is = null;
		int arraySize = 0;
		int pageCount = 0;
		String onePositionList[] = new String[arraySize];
		//you can change the name to .csv, or .txt, whatever format you want
		PrintWriter writer = new PrintWriter("HtmlLinks.csv", "UTF-8");

		// asking how many web pages you want to read
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter a number of web pages you want: ");
		int numberOfPages = reader.nextInt();
		reader.close();

		while (pageCount < numberOfPages) {
			pageCount++;

			// getting html source code and throwing it into a stringbuilder
			try {
				url = new URL("https://www.chess.com/tactics/problems?tagId=11&page=" + pageCount);
				HttpURLConnection httpcon = (HttpURLConnection) url.openConnection();
				httpcon.addRequestProperty("User-Agent", "Mozilla/4.0");

				is = httpcon.getInputStream();
				br = new BufferedReader(new InputStreamReader(is));

				while ((line = br.readLine()) != null) {
					word = word.append(line);
					// System.out.println(line);
				}
				// System.out.println(">1<");
				// System.out.println(word);
				// System.out.println(">2<");
			} catch (IOException e) {
				String error = e.toString();
				throw new RuntimeException(e);
			}
			// System.out.println(">3<");

			// finding the 1 indexes
			int i = word.indexOf(">1</a>");
			while (i >= 0) {
				System.out.println(i);
				arraySize++;
				onePositionList = Arrays.copyOf(onePositionList, arraySize);
				onePositionList[arraySize - 1] = Integer.toString(i);
				System.out.println(Arrays.toString(onePositionList));
				i = word.indexOf(">1</a>", i + 1);
			}

			// getting url from the 1 positions
			for (int j = 0; j < onePositionList.length; j++) {

				// fixing a edge case, with a bad url
				if (!Character.isLetter(word.charAt(Integer.parseInt(onePositionList[j]) - 23))) {
					writer.println(word.substring(Integer.parseInt(onePositionList[j]) - 55,
							Integer.parseInt(onePositionList[j]) - 20));
				}
				// System.out.println(word.substring(Integer.parseInt(onePositionList[j])-55,
				// Integer.parseInt(onePositionList[j])-20));
			}
			

			// Writing html source code to a text file
			// PrintWriter writer = new PrintWriter("the-file-name.txt",
			// "UTF-8");
			// writer.println("The first line");
			// writer.println(word);
			// writer.close();
		}
		writer.close();

	}

}
