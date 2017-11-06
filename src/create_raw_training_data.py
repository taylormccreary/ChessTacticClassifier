"""Takes the data in the csv files that was scraped from chess.com
and cleans it, outputting it into a csv file of training data.
This data can then be used to create features."""
import pandas as pd
import chess


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
    f_array = pd.read_csv('..\\data\\fork.csv')
    s_array = pd.read_csv('..\\data\\skewer.csv')
    t_array = pd.read_csv('..\\data\\trapped.csv')
    frames = [f_array, s_array, t_array]
    tactics_array = pd.concat(frames)
    tactics_array["FEN"] = tactics_array.apply(get_full_fen, axis=1)
    tactics_array["tactic_fen"] = tactics_array.apply(update_fen, axis=1)
    tactics_array["move"] = tactics_array["Second Move"]
    tactics_array[['tactic_fen', 'move', 'Tactic']].to_csv(
        '../data/training_data_unprocessed.csv', index=False)
