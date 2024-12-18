import random
from models import Card
from create_db import *
from sqlmodel import SQLModel, Session, select


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
    print('écrivez votre réponse')
    response = input("veuillez entrez votre réponse: ").upper()
    # est ce que c'est la bonne reponse

    if choiced_card.correct == response:
        print("bonne réponse")
        return True

    else:
        print("mauvaise réponse")
        return False


def refresh_seen():
    with Session(engine) as session:
        cards = session.exec(select(Card)).all()
        for card in cards:
            card.seen = "False"
            session.add(card)
            session.commit()



