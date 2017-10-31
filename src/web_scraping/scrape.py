"""Testing web scraping with beautifulsoup"""
import pandas as pd
import numpy as np
import url_utils

if __name__ == "__main__":
    FORKS = url_utils.get_n_tactic_urls(11, 15)

    # alternatively, to load urls from csv:
    #forks_array = pd.read_csv("C:\\Users\\Taylor McCreary\\OneDrive\\Classes\\Data Science\\ChessTacticClassifier\\src\\web_scraping\\urls.csv", header=None)
    #FORKS = np.array(forks_array[0])

    url_utils.write_tactic_csv("forks.csv", FORKS, "fork")
