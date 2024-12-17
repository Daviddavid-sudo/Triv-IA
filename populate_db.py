from models import Card
from create_db import *
import json

with open('blue.json', 'r') as file:
    data = json.load(file)


def create_cards():
    with Session(engine) as session:
        for card_dict in data:
            card = Card(
                category=card_dict["category"],
                question=card_dict["question"],
                response1=card_dict["response1"],
                response2=card_dict["response2"],
                response3=card_dict["response3"],
                response4=card_dict["response4"],
                correct=card_dict["correct"],
                seen=card_dict["seen"]
            )

            session.add(card)
        session.commit()

create_cards()