from players import Player
from cards import *
import random
import copy

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

    # demander la direction choisie
    print("Souhaitez-vous aller à gauche ou à droite ?")

    # Simulation de direction
    position_player = copy.copy(player.position)

    value_dice = copy.copy(dice)

    print("Dans quelle direction souhaitez-vous aller ?")
    print()

    # simulation de la direction gauche
    board_test_left = copy.copy(board_game)

    # mettre la position actuelle du joueur en minuscule
    board_test_left[position_player] = board_test_left[position_player].lower()

    value_index = copy.copy(position_player) - value_dice

    if value_index < 0:
        value_index = value_index + len(board_test_left)

    board_test_left[value_index] = board_test_left[value_index].upper()
    print("1 - GAUCHE")
    print("Vous vous retrouverez ici:")
    print(board_test_left)
    # board_test_left[value_index] = board_test_left[value_index].lower()

    print()

    # Simulation de la direction droite
    board_test_right = copy.copy(board_game)

    # mettre la position actuelle du joueur en minuscule
    board_test_right[position_player] = board_test_right[position_player].lower()

    value_index2 = copy.copy(position_player) + value_dice

    if value_index2 > len(board_test_right) - 1:
        value_index2 = value_index2 - len(board_test_right)

    board_test_right[value_index2] = board_test_right[value_index2].upper()
    print("2 - DROITE")
    print("Vous vous retrouverez ici:")
    print(board_test_right)


    # Récupérer le choix de direction
    conversion_not_ok = True
    number_direction_choice = ""
    conversion_choice = ""

    # Convertir la réponse en direction
    while conversion_not_ok:
        number_direction_choice = input("Saisissez votre réponse entre 1 et 2: ")
        if number_direction_choice == "1":
            conversion_choice = "left"
            conversion_not_ok = False
        elif number_direction_choice == "2":
            conversion_choice = "right"
            conversion_not_ok = False
        else:
            print("Saisissez une valeur correcte")

    #ajout de la direction en paramètre de la fonction move()
    player.move(conversion_choice, dice)
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
