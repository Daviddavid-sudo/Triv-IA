import random

class Player:
    def __init__(self, name, position, camemberts, nb_of_turns) -> None:
        self.name = name
        self.position = position
        self.camemberts = camemberts
        self.nb_of_turns = nb_of_turns

    def move(self):
        dice = random.randint(1,6)
        choice = input(f"dice={dice}chose left or right")
        if choice == "left":
            #to change later -> 4
            self.position = self.position - dice % 4
        else:
            self.position = self.position + dice % 4

    
    def add_yellow_camembert():
        pass

    def add_blue_camembert():
        pass 
    
    def add_turn():
        pass

