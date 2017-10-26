package chessHtml;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class testing {
	public static void main(String[] args) throws Exception, Exception {

		System.out.println(HtmlSourceCode.getSource("https://www.chess.com/analysis-board-editor"));
		
		
		
	}
}
