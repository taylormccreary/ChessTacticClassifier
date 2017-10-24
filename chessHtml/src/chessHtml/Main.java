package chessHtml;

public class Main {
	public static int type = 0;
	public static String fileName = "";
	
	public static void main(String[] args) throws Exception {
		
		GetHtmlLinks.search();
		CompileData.useHtmlLinks();
	}

}
