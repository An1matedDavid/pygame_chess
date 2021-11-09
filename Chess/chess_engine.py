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
        ]  # numpy would be more efficient. Ints might be more efficient.
        self.white_to_move = True
        self.move_log = []
