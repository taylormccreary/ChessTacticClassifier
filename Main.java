package chessHtml;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		
//		Scanner reader = new Scanner(System.in);
//		System.out.println("Enter webpage in the form	https://www.chess.com/tactics/problems?tagId=11&page= ");
//		String urlInput = reader.nextLine();
//		reader.close();
//		
		
		ChessWebScraper.webScrapeUrlList();
		GetFEN.urlListToFEN();
	}

		
		
	

}
