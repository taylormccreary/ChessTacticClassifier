"""Takes the data in the csv files that was scraped from chess.com
and cleans it, outputting it into a csv file of training data.
This data can then be used to create features."""
import pandas as pd
import chess
import web_scraping.url_utils as url
import create_features as feat


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


if __name__ == "__main__":
    #f_array = pd.read_csv('..\\data\\fork.csv') Windows version
    #s_array = pd.read_csv('..\\data\\skewer.csv')
    #t_array = pd.read_csv('..\\data\\trapped.csv')
    # f_array = pd.read_csv('../data/fork.csv')   #Mac Version
    # s_array = pd.read_csv('../data/skewer.csv')
    # t_array = pd.read_csv('../data/trapped.csv')
    # frames = [f_array, s_array, t_array]
    # tactics_array = pd.concat(frames)
    # tactics_array["FEN"] = tactics_array.apply(get_full_fen, axis=1)
    # tactics_array["tactic_fen"] = tactics_array.apply(update_fen, axis=1)
    # tactics_array["move"] = tactics_array["Second Move"]
    # tactics_array["tactic"] = tactics_array["Tactic"]
    # tactics_array[['tactic_fen', 'move', 'tactic']].to_csv(
    #     '../data/training_data_unprocessed.csv', index=False)

    # Step 1:
    # Scrape urls from chess.com
    NUM_TACTICS = 20 # set how many tactics of each type to scrape
    FORKS = url.get_n_tactic_urls(11, NUM_TACTICS)
    SKEWERS = url.get_n_tactic_urls(26, NUM_TACTICS)
    TRAPPED = url.get_n_tactic_urls(29, NUM_TACTICS)

    # Step 2:
    # Scrape FEN, first move, second move, color from each url
    FEN_DATA = []

    for t_url in FORKS:
        FEN_DATA.append(url.fen_scrape(t_url, "fork"))
    for t_url in SKEWERS:
        FEN_DATA.append(url.fen_scrape(t_url, "skewer"))
    for t_url in TRAPPED:
        FEN_DATA.append(url.fen_scrape(t_url, "trapped"))

    FEN_DF = pd.DataFrame(
        FEN_DATA,
        columns=["FEN", "First Move", "Second Move", "Who Moved", "Tactic"])

    # Step 3:
    # Update FENs to represent the position after the first move
    FEN_DF["FEN"] = FEN_DF.apply(get_full_fen, axis=1)
    FEN_DF["tactic_fen"] = FEN_DF.apply(update_fen, axis=1)
    FEN_DF["move"] = FEN_DF["Second Move"]
    FEN_DF = FEN_DF[['tactic_fen', 'move', 'Tactic']]

    # line below shows first five rows of the df
    # print(FEN_DF.iloc[1:6])

    # Step 4:
    # Process FEN data by extracting relevant features
    FEATURES = pd.DataFrame()

    FEATURES["pawns_attacked"] = FEN_DF.apply(feat.num_piece_attacked, axis=1, args=(1,))
    FEATURES["knights_attacked"] = FEN_DF.apply(feat.num_piece_attacked, axis=1, args=(2,))
    FEATURES["bishops_attacked"] = FEN_DF.apply(feat.num_piece_attacked, axis=1, args=(3,))
    FEATURES["rooks_attacked"] = FEN_DF.apply(feat.num_piece_attacked, axis=1, args=(4,))
    FEATURES["queens_attacked"] = FEN_DF.apply(feat.num_piece_attacked, axis=1, args=(5,))
    FEATURES["is_capture"] = FEN_DF["move"].map(feat.check_piece_taken_on_move)
    FEATURES["pieces_on_board"] = FEN_DF["tactic_fen"].map(feat.get_number_pieces)

    FEATURES["tactic"] = FEN_DF["Tactic"]

    # line below shows first five rows of the df
    # print(FEN_DF.iloc[1:6])

    # Step 5:
    # Write feature data to csv file
    # This will be the input to our model
    FEATURES.to_csv('../data/training_data.csv', index=False)
