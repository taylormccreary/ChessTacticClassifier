"""The script that uses url_utils.py functions to get tactic from
chess.com and put them into csv files"""
import url_utils

if __name__ == "__main__":
    FORKS = url_utils.get_n_tactic_urls(11, 15)
    SKEWERS = url_utils.get_n_tactic_urls(26, 15)
    TRAPPED = url_utils.get_n_tactic_urls(29, 15)

    # alternatively, to just load urls from csv:
    # import pandas as pd
    # import numpy as np
    # ARR = pd.read_csv("C:\\Users\\Taylor McCreary\\OneDrive
    # \\Classes\\Data Science\\ChessTacticClassifier\\src
    # \\web_scraping\\example_urls.csv", header=None)
    # FORKS = np.array(ARR[0])

    url_utils.write_tactic_csv("../../data/fork.csv", FORKS, "fork")
    url_utils.write_tactic_csv("../../data/skewer.csv", SKEWERS, "skewer")
    url_utils.write_tactic_csv("../../data/trapped.csv", TRAPPED, "trapped")
