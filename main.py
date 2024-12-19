from players import Player
from cards import *
import random

# ajouter des joueurs
list_players = []
# number_players = input("Combien de joueurs")

# for number in range(int(number_players)):
#     name= input("quel est ton nom")
#     list_players.append([Player(name),🧝])
                         
# Ajouter des joueurs

list_players = []
emoji_player = ['🧝', '😱', '🧛', '🦹']

number_players = int(input("Combien de joueurs ? "))
for i in range(number_players):
    name = input(f"Nom du joueur {i + 1} : ")
    emoji = emoji_player[i]
    list_players.append(Player(name, emoji))

print("\nJoueurs inscrits :")
for player in list_players:
    print(f"- {player.name} ({player.emoji})")

# Plateau de jeu
board_game = [...]
player_positions = {player: 0 for player in list_players}



# Plateau de jeu sous forme de carré 8x8
board_game = [
    "bleu", "jaune", "vert", "bleu_camembert", "bleu", "jaune", "vert", "jaune_camembert",
    "bleu_camembert", "", "", "", "", "", "", "bleu",
    "vert", "", "", "", "", "", "", "jaune",
    "jaune", "", "", "", "", "", "", "vert",
    "bleu", "", "", "", "", "", "", "vert_camembert",
    "vert_camembert", "", "", "", "", "", "", "bleu",
    "vert", "", "", "", "", "", "", "jaune",
    "jaune", "bleu", "jaune_camembert", "vert", "jaune", "bleu", "bleu_camembert", "vert"
]

# lien pour les couleurs
emoji_map = {
    "bleu": " 🔵 ",
    "jaune": " 🟡 ",
    "vert": " 🟢 ",
    "bleu_camembert": " 🟦 ",
    "jaune_camembert": " 🟨 ",
    "vert_camembert": " 🟩 ",
    "": "    "  
}


# player = Player("player1", emoji_player[0])

# fonction pour afficher le plateau
def display_board(board, player):
    print("\nPlateau de jeu :")
    for i in range(8): 
        for j in range(8): 
            index = i * 8 + j
            if index == player.position:
                print([player.emoji], end=" ")  
            else:
                print(f"[{emoji_map[board[index]]}]", end=" ")
        print("")  
    print("\n")

# fonction qui va me permettre de rester dans mon cadre
def move_on_edges(position, dice_roll):
    edge_positions = [
        0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56,
        48, 40, 32, 24, 16, 8
    ]
    current_index = edge_positions.index(position)
    next_index = current_index + dice_roll

    if next_index >= len(edge_positions):
        next_index -= len(edge_positions)

    return edge_positions[next_index]



player.position = 0
display_board(board_game, player)
refresh_seen()

while player.camemberts != [1, 1, 1]:
    for player in list_players:
        print(f"\nTour de {player.name} ({player.emoji})")
        print("Score du joueur: " + str(player.camemberts))
        print("Nombre de tours: " + str(player.nb_of_turns))
        good_response = True
        while good_response:
            # Lancer le dé
            dice = random.randint(1, 6)
            print("Valeur du dé: " + str(dice))
            # player.position = player.position+dice
            # Déplacer le joueur sur les bords
            player.position = move_on_edges(player.position, dice)
            # Afficher le plateau
            display_board(board_game, player)
            print(board_game[player.position])



            # Identifier la case où le joueur est arrivé
            case = board_game[player.position].split("_")

            # Jouer une carte selon la case
            is_correct = played_card(choose_card(case[0].lower()))
            if is_correct:
                if len(case) > 1:
                    if case[0].lower() == "bleu":
                        player.add_blue_camembert()
                    elif case[0].lower() == "jaune":
                        player.add_yellow_camembert()
                    elif case[0].lower() == "vert":
                        player.add_green_camembert()
                print("=" *100)    
            else:
                player.nb_of_turns += 1
                good_response = False
                print("*" *100) 

   


