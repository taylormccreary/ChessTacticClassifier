"""python module for web scraping with beautifulsoup"""
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
    url = "https://www.chess.com/tactics/problems?tagId=" + str(tactic_id) + "&page=" + str(page)
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    table_of_tactics = soup.find("table").find_all('tr')
    url_array = np.array([])
    counter = 0
    while counter < len(table_of_tactics):
        t_url = table_of_tactics[counter].find('a').get('href')
        t_rating = int(table_of_tactics[counter].find_all('td')[1].get_text())
        t_moves = int(table_of_tactics[counter].find_all('td')[4].get_text())
        if t_rating < 1200 and t_moves < 2:
            url_array = np.append(url_array, t_url)
        counter += 1
    return url_array

def get_n_tactic_urls(tactic_id, n_urls):
    """returns n tactics with the given id number"""
    count = 1
    url_array = np.array([])
    while len(url_array) < n_urls:
        url_array = np.append(url_array, get_tactic_urls(tactic_id, count))
        count += 1
    return url_array

def fen_scrape(url):
    """take a chess.com tactic url and scrape fen and moves"""
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    res_string = "stub"
    return res_string

if __name__ == "__main__":
    #forks_array = get_n_tactic_urls(11, 15)
    #print(forks_array)
    tactic_url = "https://www.chess.com/tactics/31043"
    tactic_str = fen_scrape(tactic_url)
    print(tactic_str)
    print("Hi world")
