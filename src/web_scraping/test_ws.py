"""this is just to test url_utils"""
from url_utils import *


if __name__ == "__main__":
    # forks_array = get_n_tactic_urls(11, 15)
    # df_urls = pd.DataFrame(forks_array)
    # df_urls.to_csv('urls.csv', index=False, header=["Tactic URL"])
    forks_array = pd.read_csv("urls.csv")
    print(forks_array)
    t_array = pd.DataFrame(columns=["FEN", "move1", "move2", "firstMover", "tacticType"])
    print(t_array)
    for f in forks_array:
        df = fen_scrape(f, "fork")
        print("This is the row to add: ", df)
        t_array = t_array.append(df)
        print("wahoo")
        print(t_array)
        #t_array = np.append(t_array, fen_scrape(f, "fork"))
    #df = pd.DataFrame(t_array)
    t_array.to_csv("forks.csv")
    # #write_tactic_csv('test.csv', t_array)
    # # # tactic_url = "https://www.chess.com/tactics/31043"
    # # tactic_str = fen_scrape(tactic_url)
    # # print(tactic_str)
    # print("Hi world")