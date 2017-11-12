
# coding: utf-8

# # Chess Tactic Classifier

# ## Introduction

# _In chess, a tactic refers to a sequence of moves that limits the opponent's options and may result in tangible gain. (Wikipedia)_
# 
# Chess players often solve many tactics of a single theme in order to improve their pattern recognition skills. In order to enable this, chess websites such as Chess.com need to assign labels to the tactics in their large databases of tactics. Often this is done manually, by users tagging tactics with the themes they believe are relevant.
# 
# Our goal with this project is to automate that process of tagging for a small subset of tactic themes.

# ## Web Scraping

# First, we need to gather the data by scraping tactic information from Chess.com. To do this we'll load a module we wrote that contains some useful functions. This module uses the BeautifulSoup package:

# In[ ]:


# %load ..\src\web_scraping\url_utils.py
"""python module for web scraping chess tactics with beautifulsoup"""
import csv
import urllib.request
import pandas as pd
import numpy as np
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
    u_obj.add_header('Accept', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png,    image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1')
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
    return url_list

def get_n_tactic_urls(tactic_id, n_urls):
    """returns n tactics with the given id number"""
    count = 1
    url_list = []
    while len(url_list) < n_urls:
        #url_list.append(get_tactic_urls(tactic_id, count))
        url_list = url_list + get_tactic_urls(tactic_id, count)
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
    and writes line by line to a .csv"""
    with open(fname, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["FEN", "First Move", "Second Move", "Who Moved", "Tactic"])
        for u in tactic_url_array:
            csv_writer.writerow(fen_scrape(u, t_type))


if __name__ == "__main__":
    # Here we just test getting the fens from the urls and writing to a csv
    # FORK_ARR = pd.read_csv("C:\\Users\\Taylor McCreary\\OneDrive\\Classes\\Data Science\\ChessTacticClassifier\\src\\web_scraping\\example_urls.csv", header=None)
    # FORK_URLS = np.array(FORK_ARR[1])
    # write_tactic_csv("forks.csv", FORK_URLS, "fork")
    test = get_n_tactic_urls(11, 10)
    print(test)


# Next, we'll use these functions to extract the urls for fork, skewer and trapped piece tactics.

# In[9]:


FORKFORKSS = get_n_tactic_urls(11, 15)
SKEWERS = get_n_tactic_urls(26, 15)
TRAPPED = get_n_tactic_urls(29, 15)

write_tactic_csv("../data/fork.csv", FORKS, "fork")
write_tactic_csv("../data/skewer.csv", SKEWERS, "skewer")
write_tactic_csv("../data/trapped.csv", TRAPPED, "trapped")


# In[14]:


import chess


# Now that we have the urls, we can go to each webpage and get the relevant information.
# 
# Chess positions are stored in a standardized format called a FEN. We'll need the FEN and the first move from each of the tactics. This information will be compose our "raw data".

# In[13]:


def get_full_fen(df_elem):
    """takes as input a row, returns full fen str"""
    color = "b"
    if df_elem[["Who Moved"]][0] == "white":
        color = "w"
    return df_elem[["FEN"]] + " " + color + " KQkq - 0 1"

def update_fen(df_elem):
    """takes as input a row with a full fen, and returns
    a new fen"""
    board = chess.Board(df_elem[["FEN"]][0])
    board.push_san(df_elem[["First Move"]][0])
    return board.fen()

f_array = pd.read_csv('..\\data\\fork.csv')
s_array = pd.read_csv('..\\data\\skewer.csv')
t_array = pd.read_csv('..\\data\\trapped.csv')
frames = [f_array, s_array, t_array]
tactics_array = pd.concat(frames)
tactics_array["FEN"] = tactics_array.apply(get_full_fen, axis=1)
tactics_array["tactic_fen"] = tactics_array.apply(update_fen, axis=1)
tactics_array["move"] = tactics_array["Second Move"]
tactics_array["tactic"] = tactics_array["Tactic"]
tactics_array[['tactic_fen', 'move', 'tactic']].to_csv(
    '../data/training_data_unprocessed.csv', index=False)

