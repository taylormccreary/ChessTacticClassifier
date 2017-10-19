package chessHtml;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HtmlSourceCode {
	
	public static String getSource(String CurrentUrl){
		StringBuilder sourceCode = new StringBuilder();
		
		try {
			URL url = new URL(CurrentUrl);
			HttpURLConnection httpcon = (HttpURLConnection) url.openConnection();
			httpcon.addRequestProperty("User-Agent", "Mozilla/4.0");

			InputStream is = httpcon.getInputStream();
			BufferedReader br = new BufferedReader(new InputStreamReader(is));

			String line;
			while ((line = br.readLine()) != null) {
				sourceCode = sourceCode.append(line);
			}
		} catch (IOException e) {
			String error = e.toString();
			throw new RuntimeException(e);
		}
		
		
		
		
		return sourceCode.substring(0);
	}

}
