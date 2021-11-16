import datetime


def save_to_txt_file(gs):
    st = str(datetime.datetime.now()).split('.')[0].replace(" ", "_").replace(":", "-")
    f = open("game_history/my_game_" + st + ".txt", "w")
    game_in_notation = []
    for hist_move in gs.move_log:
        hist_pretty = {
            "piece_moved": hist_move.piece_moved,
            "chess note:": hist_move.get_chess_notation(),
            "piece_captured": hist_move.piece_captured
        }
        hist_pretty = str(hist_pretty) + '\n'
        game_in_notation.append(hist_pretty)
    for pretty_hist_move in game_in_notation:
        f.write(str(pretty_hist_move))
    f.close()