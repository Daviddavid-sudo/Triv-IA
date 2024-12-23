from players import Player
from cards import *
import random

board_game=["bleu", "jaune", "vert", "bleu_camembert", "bleu", "jaune", "vert", "jaune_camembert", "bleu", "jaune", "vert", "vert_camembert"]



player = Player("player1")
board_game = [board_game[i].upper() if i == player.position else board_game[i].lower() for i in range(len(board_game)) ]
print(board_game)
refresh_seen()
while player.camemberts != [1,1,1]:

    print("Score du joueur: " + str(player.camemberts))
    print("Nombre de tours: " + str(player.nb_of_turns))

    dice = random.randint(1,6)
    print("Valeur du dés: " + str(dice))
    player.move(dice)
    board_game = [board_game[i].upper() if i == player.position else board_game[i].lower() for i in range(len(board_game)) ]
    print(board_game)
    case = board_game[player.position].split("_")

    is_correct = played_card(choose_card(case[0].lower()))
    if is_correct:
        if len(case) > 1:
            if case[0].lower() == "bleu":
                player.add_blue_camembert()
            elif case[0].lower() == "jaune":
                player.add_yellow_camembert()
            elif case[0].lower() == "vert":
                player.add_green_camembert()
            # add function green color
    else:
        player.nb_of_turns += 1
    print('='*25)