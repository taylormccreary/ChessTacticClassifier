"""this is just to test url_utils"""
from url_utils import *

def simple_test(url, extrastr):
    """just to test apply"""
    print("yahoo" + url + "yahoo" + extrastr)

if __name__ == "__main__":
    # forks_array = get_n_tactic_urls(11, 15)
    # df = pd.DataFrame(forks_array)
    # df.to_csv("fork_urls.csv", header=False)
    # print(forks_array)

    forks_array = pd.read_csv("C:\\Users\\Taylor McCreary\\OneDrive\\Classes\\Data Science\\ChessTacticClassifier\\src\\web_scraping\\urls.csv", header=None)
    #print(forks_array)
    # print("theres should be ", len(forks_array))
    # t_array = pd.DataFrame()
    forks_urls = np.array(forks_array[0])

    new_df = []
    for u in forks_urls:
        new_df.append(fen_scrape(u, "fork"))

    
    print(new_df)  
# new_df.to_csv("forks.csv")
    #np.apply_along_axis(fen_scrape, 0, forks_urls, ["fork"])
    #new_df = forks_urls.apply(fen_scrape, axis=1, args=(["fork"]))
    # print(new_df)
    # for index, row in t_array.iterrows():
    #     print("once")
    #     df = fen_scrape(row, "fork")
    #     t_array = t_array.append(df)

    # print(new_df)
    # new_df.to_csv("forks.csv")
    # #write_tactic_csv('test.csv', t_array)
    # # # tactic_url = "https://www.chess.com/tactics/31043"
    # # tactic_str = fen_scrape(tactic_url)
    # # print(tactic_str)
    # print("Hi world")
