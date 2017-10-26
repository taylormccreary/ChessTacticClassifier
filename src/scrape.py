"""Testing web scraping with beautifulsoup"""
import urllib.request
from bs4 import BeautifulSoup

def open_as_firefox(url):
    """adds headers when using urllib.request.URLopener to avoid 403 error. Code from:
    https://stackoverflow.com/questions/22877619/python3-urllib-error-httperror-http-error-403-forbidden"""
    u_obj = urllib.request.URLopener() # Python 3: urllib.request.URLOpener
    u_obj.addheaders = []
    u_obj.addheader('User-Agent', 'Mozilla/5.0')
    u_obj.addheader('Accept-Language', 'de-DE,de;q=0.9,en;q=0.8')
    u_obj.addheader('Accept', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png,\
    image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1')
    file_from_url = u_obj.open(url)
    res = file_from_url.read()
    file_from_url.close()
    return res

if __name__ == "__main__":
    url = "https://www.chess.com/tactics/problems?tagId=11"

    content = open_as_firefox(url)

    soup = BeautifulSoup(content, "html.parser")

    trs = soup.find("table", class_="table with-row-highlight table-tactics-problems")
    print(trs.contents[1])
