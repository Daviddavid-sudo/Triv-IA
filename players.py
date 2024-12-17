import random

class Player:
    def __init__(self, name, position = 0, camemberts = [0,0], nb_of_turns = 0) -> None:
        self.name = name
        self.position = position
        self.camemberts = camemberts
        self.nb_of_turns = nb_of_turns

    def move(self):
        dice = random.randint(1,6)
        # choice = input(f"dice={dice}chose left or right")
        choice = "left"
        if choice == "left":
            #to change later -> 4
            self.position = (self.position - dice) % 4
        else:
            self.position = (self.position + dice) % 4

    
    def add_yellow_camembert(self):
        self.camemberts[0] = 1
        if self.camemberts == [1,1]:
            print("win")

    def add_blue_camembert(self):
        self.camemberts[1] = 1
        if self.camemberts == [1,1]:
            print("win")
    
    def add_turn(self):
        self.nb_of_turns += 1

