"""Testing web scraping with beautifulsoup"""
import pandas as pd
import numpy as np
import url_utils

if __name__ == "__main__":
    FORKS = url_utils.get_n_tactic_urls(11, 15)
    SKEWERS = url_utils.get_n_tactic_urls(26, 15)
    TRAPPED = url_utils.get_n_tactic_urls(29, 15)

    # alternatively, to load urls from csv:
    # ARR = pd.read_csv("C:\\Users\\Taylor McCreary\\OneDrive\\Classes\\Data Science\\ChessTacticClassifier\\src\\web_scraping\\urls.csv", header=None)
    # FORKS = np.array(ARR[0])

    url_utils.write_tactic_csv("../../data/fork.csv", FORKS, "fork")
    url_utils.write_tactic_csv("../../data/skewer.csv", SKEWERS, "skewer")
    url_utils.write_tactic_csv("../../data/trapped.csv", TRAPPED, "trapped")
