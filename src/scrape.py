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

def get_tactic_urls(tactic_id, num_tactics):
    """returns the urls for the given # of tactics with given id"""
    url = "https://www.chess.com/tactics/problems?tagId=" + str(tactic_id)
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    table_of_tactics = soup.find("table", class_="table with-row-highlight table-tactics problems")
    url_array = np.array([])
    counter = 1
    while np.size(url_array) < num_tactics:
        if table_of_tactics[counter]:
            url_array = np.append(url_array, url)
        print("wahoo")
        counter += 1
    return url_array

if __name__ == "__main__":
    get_tactic_urls(11,20)
    print("Hi world")
