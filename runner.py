from disk import Disk
from game import Game
from minimax_player.min_max_player import MinimaxPlayer
from minimax_player.min_max_player_2 import MinimaxPlayer2
from minimax_player.min_max_player_3 import MinimaxPlayer3
from qplayer.q_player import QPlayer

d_win = 0
l_win = 0
for i in range(50):
    game1 = Game.default_start()
    winner = game1.play_game()
    if winner == Disk.DARK:
        d_win+=1
    elif winner == Disk.LIGHT:
        l_win+=1
    print("i", i)

print("\nGame 1 \n","dark -", d_win, "light -",l_win,"\n\n")
