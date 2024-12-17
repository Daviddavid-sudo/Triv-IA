from players import Player

board_game=["YELLOW CAMEMBERT" ,"BLUE", "BLUE CAMEMBERT", "YELLOW"]


player = Player("player1")

player.move()
if player.position == 2:
    card1 = Card(blue)
    card1.blue_question()
    response = input()
    if response == card1.blue_response():
         player.add_blue_camembert()