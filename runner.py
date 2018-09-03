from disk import Disk
from game import Game
from minimax_player.min_max_player import MinimaxPlayer
from minimax_player.min_max_player_2 import MinimaxPlayer2
from minimax_player.min_max_player_3 import MinimaxPlayer3
from qplayer.q_player import QPlayer

d_win = 0
l_win = 0
for i in range(500):
    game1 = Game.default_start()
    winner = game1.play_game()
    if winner == Disk.DARK:
        d_win+=1
    elif winner == Disk.LIGHT:
        l_win+=1
    print("i", i)

print("\nGame 1 \n","dark -", d_win, "light -",l_win,"\n\n")


for i in range(500):
    Game.computer_player1_class = MinimaxPlayer2
    game2 = Game.default_start()
    winner = game2.play_game()
    if winner == Disk.DARK:
        d_win += 1
    elif winner == Disk.LIGHT:
        l_win += 1
    print("i", i)

print("\nGame 2 \n", "dark -", d_win, "light -", l_win, "\n\n")
#
# for i in range(50):
#     Game.computer_player1_class = MinimaxPlayer3
#     game3 = Game.default_start()
#     winner = game1.play_game()
#     if winner == Disk.DARK:
#         d_win+=1
#     elif winner == Disk.LIGHT:
#         l_win+=1
#     print("i", i)
#
# print("\nGame 3 \n","dark -", d_win, "light -",l_win,"\n\n")
#
# for i in range(50):
#     Game.computer_player2_class = QPlayer
#     Game.computer_player1_class = MinimaxPlayer2
#     game4 = Game.default_start()
#     winner = game1.play_game()
#     if winner == Disk.DARK:
#         d_win+=1
#     elif winner == Disk.LIGHT:
#         l_win+=1
#     print("i", i)
#
# print("\nGame 4 \n","dark -", d_win, "light -",l_win,"\n\n")