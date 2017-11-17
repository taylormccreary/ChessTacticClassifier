"""Uses the data in the csv of fens, moves and tactics
to create features that we use to train on"""
import pandas as pd
import chess
from sklearn import tree
import graphviz


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

def get_attacked_squares(df_elem):
    """from a python-chess board and move, get the squares that are attacked
    by the piece that moves"""
    board = chess.Board(df_elem[["tactic_fen"]][0])
    board.push_san(df_elem[["move"]][0])
    move = board.peek()
    squares = board.attacks(move.to_square)
    return squares

def get_move_square(df_elem):
    """from a python-chess board and str move, get the destination square of
    the move"""
    board = chess.Board(df_elem[["tactic_fen"]][0])
    board.push_san(df_elem[["move"]][0])
    move = board.peek()
    return move.to_square

def num_piece_attacked(df_elem, piece_id):
    """from a python-chess board and move, get the # pieces attacked
    by the piece that moves.\n
    1 - pawn\n
    2 - knight\n
    3 - bishop\n
    4 - rook\n
    5 - queen\n
    6 - king"""
    squares = get_attacked_squares(df_elem)
    board = chess.Board(df_elem[["tactic_fen"]][0])

    total = 0
    for sqr in squares:
        if board.piece_type_at(sqr) == piece_id:
            total += 1
    return total

def get_attacked_value(df_elem):
    """get the total value of all the attacked pieces"""
    total_value = 0
    total_value += num_piece_attacked(df_elem, 1) # pawn
    total_value += num_piece_attacked(df_elem, 2) * 3 # knight
    total_value += num_piece_attacked(df_elem, 3) * 3 # bishop
    total_value += num_piece_attacked(df_elem, 4) * 5 # rook
    total_value += num_piece_attacked(df_elem, 5) * 9 # queen
    return total_value

# def is_tactic_check(df_elem):
#     """with the row of the df, determines if the move is a check"""
#     board = chess.Board(df_elem[["tactic_fen"]][0])
#     board.push_san(df_elem[["move"]][0])
#     return board.is_check()

def get_number_pieces(fen):
    """returns number of pieces on the board"""
    output = 0
    temp = fen.split(' ')
    for c in temp[0]:
        if c.isalpha():
            output += 1
    return output

def is_check(move):
    """check if move captured a piece"""
    if "+" in move:
        return True
    else:
        return False

def is_capture(move):
    """check if move captured a piece"""
    if "x" in move:
        return True
    else:
        return False

if __name__ == "__main__":
    #df_data = pd.read_csv('..\\data\\training_data_unprocessed.csv') Windows version
    df_data = pd.read_csv('../data/training_data_unprocessed.csv')   #Mac version
    df_features = pd.DataFrame()

    # This might be useful info, but it's not really in a good format for a decision tree
    # or some such model right now, it creates lists of varying lengths
    # df_features["squares_attacked"] = df_data.apply(get_attacked_squares, axis=1)
    df_features["pawns_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(1,))
    df_features["knights_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(2,))
    df_features["bishops_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(3,))
    df_features["rooks_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(4,))
    df_features["queens_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(5,))
    df_features["value_attacked"] = df_data.apply(get_attacked_value, axis=1)
    # df_features["was_piece_taken"] = df_data["first_move"].map(check_piece_taken_on_move)
    df_features["piece_to_be_taken"] = df_data["move"].map(is_capture)
    df_features["pieces_on_board"] = df_data["tactic_fen"].map(get_number_pieces)

    df_features["tactic"] = df_data["tactic"]
    # # Here are two examples of creating features to be part of df_features
    # # if the feature is built using only one variable, use map()
    # # if you need the whole row, use apply()
    # df_features["wasInCheck"] = df_data["tactic_fen"].map(get_is_check)
    # df_features["inCheck"] = df_data.apply(is_tactic_check, axis=1)


    features = list(df_features.columns[:8])
    X = df_features[features]
    Y = df_features.tactic.values
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("picture")
# print(df_features)
    
