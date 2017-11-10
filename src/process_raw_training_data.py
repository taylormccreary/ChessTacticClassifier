"""Uses the data in the csv of fens, moves and tactics
to create features that we use to train on"""
import pandas as pd
import chess
import taylor_functions

def get_is_check(fen):
    """uses the chess module to determine if a fen represents a position in check"""
    board = chess.Board(fen)
    return board.is_check()

def is_tactic_check(df_elem):
    """with the row of the df, determines if the move is a check"""
    board = chess.Board(df_elem[["tactic_fen"]][0])
    board.push_san(df_elem[["move"]][0])
    return board.is_check()

if __name__ == "__main__":
    df_data = pd.read_csv('..\\data\\training_data_unprocessed.csv')
    df_features = pd.DataFrame()
    df_features["tactic"] = df_data["tactic"]

    # Here are two examples of creating features to be part of df_features
    # if the feature is built using only one variable, use map()
    # if you need the whole row, use apply()
    df_features["wasInCheck"] = df_data["tactic_fen"].map(get_is_check) # if the original fen is a position in check (not a real feature we care about)
    df_features["inCheck"] = df_data.apply(is_tactic_check, axis=1)
    print(df_features)
    