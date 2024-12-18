import random


board_game=["bleu", "jaune", "vert", "bleu_camembert", "bleu", "jaune", "vert", "jaune_camembert", "bleu", "jaune", "vert", "vert_camembert"]

class Player:
    def __init__(self, name, position = 0, camemberts = [0,0,0,0,0,0], nb_of_turns = 0) -> None:
        self.name = name
        self.position = position
        self.camemberts = camemberts
        self.nb_of_turns = nb_of_turns

    def move(self, direction, dice):
        # dice = random.randint(1,6)
        # choice = input(f"dice={dice}chose left or right")
        choice = "left"
        if choice == "left":
            self.position = (self.position + dice) % 42
        else:
            self.position = (self.position - dice) % 42


    def add_yellow_camembert(self):
        self.camemberts[1] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False

    def add_blue_camembert(self):
        self.camemberts[0] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False

    def add_green_camembert(self):
        self.camemberts[2] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False
        
    def add_pink_camembert(self):
        self.camemberts[3] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False

    def add_orange_camembert(self):
        self.camemberts[4] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False
        
    def add_purple_camembert(self):
        self.camemberts[5] = 1
        if self.camemberts == [1,1,1,1,1,1]:
            print("win")
            return False
    
    def add_turn(self):
        self.nb_of_turns += 1
    

