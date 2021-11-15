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
    """let us access image from dict like > IMAGES['wP']. transform.scale is required to make it into a screen object
    for screen.blit. My first impression is that this is a little clunky."""
    pieces =["wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


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
    square_selected = ()  # No square is selected, tuple to keep track of the last click of the user.
    player_clicks = []  # keep track of player clicks for clicking "piece from" and "piece to" -->
                        # two tuples: [(6,4),(4,4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x,y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if square_selected == (row, col):  # check if we're re-clicking square.
                    square_selected = ()  # not selected
                    player_clicks = []  # reset clicks
                else:
                    square_selected = (row, col)
                    player_clicks.append(square_selected)  # append for both 1st and 2nd click
                if len(player_clicks) == 2:  # after 2nd click, move the piece.
                    player_clicks = []

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_board(screen):
    """draw squares
    top left square is always light/white
    simpler solution: https://youtu.be/EnYui0e73Rs?t=2129 """
    # TODO: let users pick colors.
    wx = 0
    bx = SQ_SIZE
    y = 0
    even_odd = 0
    light_color = "wheat"
    dark_color = "gray30"
    for i in range(DIMENSION):
        p.draw.rect(screen, light_color, [wx, y, SQ_SIZE, SQ_SIZE])
        p.draw.rect(screen, dark_color, [bx, y, SQ_SIZE, SQ_SIZE])
        for j in range(DIMENSION):
            y += SQ_SIZE
            if even_odd == 0:
                even_odd = 1
                p.draw.rect(screen, dark_color, [wx, y, SQ_SIZE, SQ_SIZE])
                p.draw.rect(screen, light_color, [bx, y, SQ_SIZE, SQ_SIZE])
            elif even_odd == 1:
                even_odd = 0
                p.draw.rect(screen, light_color, [wx, y, SQ_SIZE, SQ_SIZE])
                p.draw.rect(screen, dark_color, [bx, y, SQ_SIZE, SQ_SIZE])
        y = 0
        wx += SQ_SIZE * 2
        bx += SQ_SIZE * 2


def draw_simpler_demo():
    """bones of the logic that let's you use modulo to get even odd, rather than setting a flag"""
    colors = ["white" , "black"]
    for row in range(DIMENSION):
        for column in range (DIMENSION):
            print("row column:", row, column)
            even_odd = (row + column) % 2
            print("even_odd:", even_odd)
            print("color:", colors[even_odd])

def draw_pieces(screen, board):
    """draw pieces using current GameState.board"""
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":  # not an empty square
                screen.blit(IMAGES[piece], p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, gs):
    """
    Responsible to render game-state graphics.
    """
    draw_board(screen)  # draw the sqares on the board.
    # TODO: add in piece highlighting or movie suggestions
    draw_pieces(screen, gs.board)  # draw pieces on top of those squares


if __name__ == "__main__":
    main()
