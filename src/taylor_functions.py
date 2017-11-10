"""Functions to get features from data"""
import chess
import pandas as pd

def get_attacked_squares(df_elem):
    """from a python-chess board and move, get the squares that are attacked
    by the piece that moves"""
    board = chess.Board(df_elem[["tactic_fen"]][0])
    board.push_san(df_elem[["move"]][0])
    move = board.peek()
    squares = board.attacks(move.to_square)
    #print(list(squares))
    return squares

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

if __name__ == "__main__":
    df_data = pd.read_csv('..\\data\\training_data_unprocessed.csv')
    df_data["squares"] = df_data.apply(get_attacked_squares, axis=1)
    df_data["pawns_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(1,))
    df_data["knights_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(2,))
    df_data["bishops_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(3,))
    df_data["rooks_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(4,))
    df_data["queens_attacked"] = df_data.apply(num_piece_attacked, axis=1, args=(5,))
    df_data["value_attacked"] = df_data.apply(get_attacked_value, axis=1)
    #df_data["num_attacked_pieces"] = df_data.iloc[:, -5:].sum(axis=1)
    #print(df_data.corr())
    #print(df_data.iloc[1:5])

    import chess.svg
    board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
    squares = board.attacks(chess.E4)
    chess.svg.board(board=board, squares=squares)  
    