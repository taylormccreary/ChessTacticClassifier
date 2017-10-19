package chessHtml;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class SolutionMove {

	public static String search(String htmlSourceCode) throws Exception, Exception {
		// public static void search() throws Exception, Exception {

		//StringBuilder htmlSourceCode = new StringBuilder();
		URL url;
		BufferedReader br;
		String line;
		String move = "";
		InputStream is = null;
		int arraySize = 0;
		// int pageCount = 0;
		String solMoveIndex[] = new String[arraySize];
//
//		// you can change the name to .csv, or .txt, whatever format you want
//		PrintWriter writer = new PrintWriter("SolLinks.txt", "UTF-8");
//
//		// getting html source code and throwing it into a stringbuilder
//		try {
//			url = new URL(currentUrl);
//			HttpURLConnection httpcon = (HttpURLConnection) url.openConnection();
//			httpcon.addRequestProperty("User-Agent", "Mozilla/4.0");
//
//			is = httpcon.getInputStream();
//			br = new BufferedReader(new InputStreamReader(is));
//
//			while ((line = br.readLine()) != null) {
//				htmlSourceCode = htmlSourceCode.append(line);
//			}
//		} catch (IOException e) {
//			String error = e.toString();
//			throw new RuntimeException(e);
//		}

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
