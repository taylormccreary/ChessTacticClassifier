"""Testing web scraping with beautifulsoup"""
import url_utils

if __name__ == "__main__":
    FORKS = url_utils.get_n_tactic_urls(11, 15)
    for f in FORKS:
        print(f)
    print("Hi world")
