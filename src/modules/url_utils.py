"""python module for web scraping chess tactics with beautifulsoup"""
import csv
import urllib.request
from bs4 import BeautifulSoup

def open_as_firefox(url):
    """adds headers when using urllib.request.URLopener to avoid 403 error. Code from:
    https://stackoverflow.com/questions/22877619/python3-urllib-error-httperror-http-error-403-forbidden"""
    #u_obj = urllib.request.URLopener() # Python 3: urllib.request.URLOpener
    u_obj = urllib.request.Request(url)
    u_obj.addheaders = []
    # u_obj.addheader('User-Agent', 'Mozilla/5.0')
    # u_obj.addheader('Accept-Language', 'de-DE,de;q=0.9,en;q=0.8')
    # u_obj.addheader('Accept', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png,\
    # image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1')
    
    u_obj.add_header('User-Agent', 'Mozilla/5.0')
    u_obj.add_header('Accept-Language', 'de-DE,de;q=0.9,en;q=0.8')
    u_obj.add_header('Accept', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png,\
    image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1')
    #file_from_url = u_obj.open(url)
    file_from_url = urllib.request.urlopen(u_obj)
    res = file_from_url.read()
    file_from_url.close()
    return res

def get_tactic_urls(tactic_id, page):
    """returns the urls for the given page with given id"""
    url = "https://www.chess.com/tactics/problems?tagId=" + str(tactic_id) + "&page=" + str(page)
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    table_of_tactics = soup.find("table").find_all('tr')
    counter = 0
    url_list = []

    while counter < len(table_of_tactics):
        t_url = table_of_tactics[counter].find('a').get('href')
        t_rating = int(table_of_tactics[counter].find_all('td')[1].get_text())
        t_moves = int(table_of_tactics[counter].find_all('td')[4].get_text())
        if t_rating < 1200 and t_moves < 2:
            url_list.append(t_url)
        counter += 1

    # check for empty page
    if len(table_of_tactics) == 0:
        return -1

    return url_list

def get_n_tactic_urls(tactic_id, n_urls):
    """returns n tactics with the given id number"""
    count = 1
    url_list = []
    while len(url_list) < n_urls:
        #url_list.append(get_tactic_urls(tactic_id, count))
        new_urls = get_tactic_urls(tactic_id, count)
        if new_urls == -1:
            return url_list
        url_list = url_list + new_urls
        #url_list = url_list + get_tactic_urls(tactic_id, count)
        count += 1
    #return np.array(url_list).flatten()
    return url_list

def get_fen_mover(fen):
    """from fen string, get the simple fen and the mover separately"""
    res = fen.replace('\\', '').split(' ')
    res[1] = "white" if res[1] == 'w' else "black"
    return res

def get_moves(mvs):
    """from string of moves, get each move"""
    res = mvs.replace('\\', '').replace('.', '').split()
    if len(res) > 3:
        return [res[1], res[3]]
    else:
        return [res[1], res[2]]


def fen_scrape(url, t_type):
    """take a chess.com tactic url and scrape fen and moves"""
    content = open_as_firefox(url)
    soup = BeautifulSoup(content, "html.parser")
    # figure out what's in the soup and what we need from it
    long_str = soup.find(class_="chess-board-container").get('ng-init').split('"')
    fen_id = long_str.index("initialFen") # returns 13, so we want 15
    fen_str = long_str[fen_id + 2]
    clean_fen = get_fen_mover(fen_str)
    moves_id = long_str.index(']\\n[FULL \\')
    moves_str = long_str[moves_id + 1]
    clean_moves = get_moves(moves_str)
    res_arr = [clean_fen[0], clean_moves[0], clean_moves[1], clean_fen[1], t_type]
    return res_arr

def write_tactic_csv(fname, tactic_url_array, t_type):
    """takes as input name of file and the array of tactic urls
    and writes fens from url line by line to a .csv"""
    with open(fname, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["FEN", "First Move", "Second Move", "Who Moved", "Tactic"])
        for u in tactic_url_array:
            csv_writer.writerow(fen_scrape(u, t_type))


if __name__ == "__main__":
    # Here we just test getting the fens from the urls and writing to a csv
    FORKS = get_n_tactic_urls(11, 15)
    SKEWERS = get_n_tactic_urls(26, 15)
    TRAPPED = get_n_tactic_urls(29, 15)

    write_tactic_csv("../../data/fork.csv", FORKS, "fork")
    write_tactic_csv("../../data/skewer.csv", SKEWERS, "skewer")
    write_tactic_csv("../../data/trapped.csv", TRAPPED, "trapped")
