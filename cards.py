import random
from models import Card
from create_db import *
from sqlmodel import SQLModel, Session, select


def choose_card(couleur):
    with Session(engine) as session:
        question_list = select(Card).where(Card.category == couleur).where(Card.seen == "False")
        results = session.exec(question_list).all()
        choose_question = random.choice(results)
        return choose_question

choose_card = choose_card("bleu")

def played_card(choiced_card):

    choice_response = {
        "1":choiced_card.response1,
        "2":choiced_card.response2,
        "3":choiced_card.response3,
        "4":choiced_card.response4}
    # afficher questions
    print(choiced_card.question)
    # afficher choix de reponses
    print("Choix de réponse 😊")
    print(f"réponse 1: " + choice_response["1"])
    print(f"réponse 2: " + choice_response["2"])
    print(f"réponse 3: " + choice_response["3"])
    print(f"réponse 4: " + choice_response["4"])

    # recuperer reponses
    print('écrivez votre réponse')
    response = input("veuillez entrez votre réponse: ")
    # est ce que c'est la bonne reponse

    if choiced_card.correct == response:
        return True
        print("bonne réponse")
    else:
        return False
        print("mauvaise réponse")

    with Session(engine) as session:
        choiced_card.seen = "True"
        session.add(choiced_card)
        session.commit()
        session.refresh(choiced_card)

def refresh_seen():
    with Session(engine) as session:
        cards = session.exec(select(Card)).all()
        for card in cards:
            card.seen = "False"
            session.add(card)
            session.commit()
        print("Votre jeu a été réinitialisé")


refresh_seen()
