"""Testing web scraping with beautifulsoup"""
import urllib.request
import numpy as np
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

def get_tactic_urls(tactic_id, page):
    """returns the urls for the given page with given id"""
    url = "https://www.chess.com/tactics/problems?tagId=" + str(tactic_id)
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    table_of_tactics = soup.find("table").find_all('tr')
    url_array = np.array([])
    counter = 0
    while counter < len(table_of_tactics):
        t_url = "stub"
        t_rating = "stub"
        t_moves = "stub"
        if t_rating < 1200 and t_moves < 2:
            url_array = np.append(url_array, t_url)
        counter += 1
    return url_array

if __name__ == "__main__":
    test = get_tactic_urls(11,20)
    print(test)
    print("Hi world")
