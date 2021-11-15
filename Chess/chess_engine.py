"""
This class is responsible for storing info of current state of a chess game.
Also responsible for determining the valid moves at current state.
It will also keep a move log.
"""


class GameState:
    """
    Board is an 8x8 2 dimensional list. each element of the list has 2 characters.
    The first character represents the color of the piece. "b" for black, "w" for white.
    The second character represents the type of the piece ('R' rook, 'N' knight, 'B' bishop, 'Q' queen, 'K' king, 'P' pawn
    The string '--' represents and empty space with no piece.
    """
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]  # board state. numpy would be more efficient. Ints might be more efficient.
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):
        """ advance the board state to post-move state."""
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)  # log the move
        self.white_to_move = not self.white_to_move  # clever way to swap


class Move():
    """Class to store and tack moves in a game."""

    """
    Rank File Notation in chess. The chessboard is divided into ranks (numbers) and files (letters).
    This is used as an identifier for when the players move their chess pieces.
    
    8
    7
    ..
    2
    1
     a  b  ..  g  h
    """

    # key: value mapping to/from our (rows, cols) to (ranks, files)
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board):
        # instructor found it easier to name elements in list. No sure why he went with named variable instead of dict.
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, row, col):
        """helper function to translate our row, col numbers to rank, file notation."""
        return self.cols_to_files[col] + self.rows_to_ranks[row]