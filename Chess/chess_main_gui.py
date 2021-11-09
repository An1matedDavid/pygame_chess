"""
gui user input and displaying current GameState object
"""

import pygame as p
from Chess.chess_engine import GameState

WIDTH = 512
HEIGHT = 512
DIMENSION = 8  # chess board dimension is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # frames per sec, for animation
IMAGES = {}

"""
loading images into pygame is an expensive operation. Try to load images into game only once. 
*DC: can it be cached in some way? read more efficiently? is this a case against pygame?
Initialize a global dictionary of images. This will be called 1x in main()
"""

def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
              "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    for piece in pieces:
        # note we are loading images into a dict
        IMAGES[piece] = p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE)


def main():
    """
    The main driver for our code. This will handle the user input and updating the graphics
    """
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    # could add move log here.
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_board(screen):
    """draw squares
    top left square is always light/white"""
    # TODO: let users pick colors.
    # wx= 0
    # bx=20
    # for i in range(10):
    #     print(wx, bx)
    #     wx+=20
    #     bx+=20
    print("SQ_SIZE:", SQ_SIZE)
    p.draw.rect(screen, "green", [0, 20, 20, 20])
    p.draw.rect(screen, "gray", [20, 20, SQ_SIZE, SQ_SIZE])
    p.draw.rect(screen, "green", [40, 20, SQ_SIZE, SQ_SIZE])
    p.draw.rect(screen, "gray", [50, 20, SQ_SIZE, SQ_SIZE])

def draw_pieces(screen, board):
    """draw pieces using current GameState.board"""
    pass

def draw_game_state(screen, gs):
    """
    Responsible to render game-state graphics.
    """
    draw_board(screen)  # draw the sqares on the board.
    # TODO: add in piece highlighing or movie suggestions
    draw_pieces(screen, gs.board)  # draw pieces on top of those squares


if __name__ == "__main__":
    main()
