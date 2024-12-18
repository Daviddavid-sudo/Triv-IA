from players import Player
from cards import *
import random

board_game=["bleu", "jaune", "vert", "bleu_camembert", "bleu", "jaune", "vert", "jaune_camembert", "bleu", "jaune", "vert", "vert_camembert"]



player = Player("player1")

while player.camemberts != [1,1,1]:
    print(board_game)
    print("Score du joueur: " + player.camemberts)
    print("Nombre de tours: " + player.nb_of_turns)

    dice = random.randint(1,6)
    print("Valeur du dés: " + dice)
    player.move(dice)

    case = board_game[player.position].split("_")

    is_correct = played_card(choose_card(case[0]))

    if is_correct:
        if len(case) > 1:
            if case[0] == "bleu":
                player.add_blue_camembert
            elif case[0] == "jaune":
                player.add_yellow_camembert
            # add function green color
    else:
        player.nb_of_turns += 1
