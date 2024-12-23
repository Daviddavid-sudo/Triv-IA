from players_app import Player
from cards import *
import random

board_game=["bleu_camembert", "jaune", "vert", "violet", "rose", "bleu", "blanc", "orange_camembert", "violet", "bleu", "jaune", "orange",
            "rose", "blanc", "vert_camembert", "violet", "jaune", "rose", "orange", "vert",
            "blanc", "violet_camembert", "rose", "bleu", "orange", "jaune", "vert", "blanc",
            "rose_camembert", "violet", "vert", "orange", "jaune", "bleu", "blanc", "jaune_camembert",
            "vert", "bleu", "violet", "rose", "orange", "blanc"]


def choose_card(couleur):
    with Session(engine) as session:
        question_list = select(Card).where(Card.category == couleur).where(Card.seen == "False")
        results = session.exec(question_list).all()
        if results == []:
            refresh_seen()
            question_list = select(Card).where(Card.category == couleur).where(Card.seen == "False")
            results = session.exec(question_list).all()
            choose_question = random.choice(results)
            choose_question.seen = "True"
            session.add(choose_question)
            session.commit()
            session.refresh(choose_question)
            return choose_question
            
        else:
            choose_question = random.choice(results)
            choose_question.seen = "True"
            session.add(choose_question)
            session.commit()
            session.refresh(choose_question)
            return choose_question




def played_card(choiced_card):

    choice_response = {
        "A":choiced_card.response1,
        "B":choiced_card.response2,
        "C":choiced_card.response3,
        "D":choiced_card.response4}
    # afficher questions
    print(choiced_card.question)
    # afficher choix de reponses
    print("Choix de réponse 😊")
    print(f"réponse A: " + choice_response["A"])
    print(f"réponse B: " + choice_response["B"])
    print(f"réponse C: " + choice_response["C"])
    print(f"réponse D: " + choice_response["D"])


    # recuperer reponses
    # print('écrivez votre réponse')

    # response = input("veuillez entrez votre réponse: ").upper()
    # est ce que c'est la bonne reponse

    # if choiced_card.correct == "A":
    #     print("bonne réponse")
    #     return True

    # else:
    #     print("mauvaise réponse")
    #     return False


def refresh_seen():
    with Session(engine) as session:
        cards = session.exec(select(Card)).all()
        for card in cards:
            card.seen = "False"
            session.add(card)
            session.commit()









# player = Player("player1")
# board_game = [board_game[i].upper() if i == player.position else board_game[i].lower() for i in range(len(board_game)) ]
# print(board_game)
# refresh_seen()
# while player.camemberts != [1,1,1]:

#     print("Score du joueur: " + str(player.camemberts))
#     print("Nombre de tours: " + str(player.nb_of_turns))

#     dice = random.randint(1,6)
#     print("Valeur du dés: " + str(dice))
#     player.move(dice)
#     board_game = [board_game[i].upper() if i == player.position else board_game[i].lower() for i in range(len(board_game)) ]
#     print(board_game)
#     case = board_game[player.position].split("_")

#     is_correct = played_card(choose_card(case[0].lower()))
#     if is_correct:
#         if len(case) > 1:
#             if case[0].lower() == "bleu":
#                 player.add_blue_camembert()
#             elif case[0].lower() == "jaune":
#                 player.add_yellow_camembert()
#             elif case[0].lower() == "vert":
#                 player.add_green_camembert()
#             # add function green color
#     else:
#         player.nb_of_turns += 1
#     print('='*25)


