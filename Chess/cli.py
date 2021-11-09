from Chess import chess_engine

def is_exit(x):
    r = "no"
    if x == "exit":
        r = "yes"
    return r

# store: each tile
# store: each player piece on a tile
# check for "check"
# check for "checkmate"
# track player turn
# end game, print player turns
# end game, print play history
# end game, count of "checks" for each player


while True:
    my_game = chess_engine.GameState()
    print("Enter your name:")
    x = input()
    exitable = is_exit(x)
    if exitable == "yes":
        exit()
    else:
        print("Hello ", x)
        print(my_game.board)