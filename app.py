import pygame as pg
import math
import time
import random
from players_app import Player
from app_functions import *

board_game=["bleu_camembert", "jaune", "vert", "violet", "rose", "bleu", "blanc", "orange_camembert", "violet", "bleu", "jaune", "orange",
            "rose", "blanc", "vert_camembert", "violet", "jaune", "rose", "orange", "vert",
            "blanc", "violet_camembert", "rose", "bleu", "orange", "jaune", "vert", "blanc",
            "rose_camembert", "violet", "vert", "orange", "jaune", "bleu", "blanc", "jaune_camembert",
            "vert", "bleu", "violet", "rose", "orange", "blanc"]

(width,height) = (1920,1080)
screen = pg.display.set_mode((width, height))
screen_width = screen.get_width()
screen_height = screen.get_height()
white = (255,255,255)
colour_dark = (100,100,100)
pg.init()
fps = pg.time.Clock()

image = pg.image.load('trivial_plateau.png')
image_token = pg.image.load('Trivialpursuit_Token2.png')
smallsmallfont=pg.font.SysFont('Corbel',25)
smallfont = pg.font.SysFont('Corbel',35)
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
text3 = smallfont.render('roll' , True , white)
text4 = smallfont.render('left' , True , white)

def piece():
    test = []
    pg.draw.circle(image, (255,255,255), (515, 510), 400)
    center = (screen_width/2-450, screen_height/2-18)
    radius = 455
    cases= 45

    angle = 0
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    test.append((x,y))

    for i in range(1,7):
        angle = (2 * math.pi / cases) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 8) - 0.08
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(9,15):
        angle = ((2 * math.pi / cases) * i) - 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 15) 
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(16,22):
        angle = ((2 * math.pi / cases) * i) + 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 22) + 0.08
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(24,30):
        angle = ((2 * math.pi / cases) * i)
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 30) 
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(31,37):
        angle = ((2 * math.pi / cases) * i) + 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 38) - 0.05
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    # pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(39,45):
        angle = ((2 * math.pi / cases) * i) - 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        # pg.draw.circle(image, (100,100,100), (x, y), 25)

    return test


def display_question(card):
    question_text = smallsmallfont.render(card.question, True, white)
    answerA_text = smallfont.render(f"A: {card.response1}", True, white)
    answerB_text = smallfont.render(f"B: {card.response2}", True, white)
    answerC_text = smallfont.render(f"C: {card.response3}", True, white)
    answerD_text = smallfont.render(f"D: {card.response4}", True, white)

    screen.blit(question_text, (screen_width-800, 150))
    screen.blit(answerA_text, (screen_width-800,200))
    screen.blit(answerB_text, (screen_width-800, 250))
    screen.blit(answerC_text, (screen_width-800, 300))
    screen.blit(answerD_text, (screen_width-800, 350))

    return card.correct


test = piece()

def move_piece(direction, position, new_position, die):
    if direction == "LEFT":
        if new_position<position:
            for coordinates in test[position:]:
                screen.blit(pg.transform.scale(image_token, (50,50)), (coordinates[0]-25, coordinates[1]-25))
                pg.time.Clock().tick(10)
                pg.display.flip()
                screen.blit(image,(0,0))
                pg.time.Clock().tick(5)
            for coordinates in test[:new_position+1]:
                screen.blit(pg.transform.scale(image_token, (50,50)), (coordinates[0]-25, coordinates[1]-25))
                pg.time.Clock().tick(10)
                pg.display.flip()
                screen.blit(image,(0,0))
                pg.time.Clock().tick(5)

        else: 
            for coordinates in test[position:new_position+1]:
                screen.blit(pg.transform.scale(image_token, (50,50)), (coordinates[0]-25, coordinates[1]-25))
                pg.time.Clock().tick(10)
                pg.display.flip()
                screen.blit(image,(0,0))
                pg.time.Clock().tick(5)
        

# def finished_moving_piece(new_position):
#     screen.blit(pg.transform.scale(image_token, (50,50)), (test[new_position][0]-25, test[new_position][1]-25))
#     pg.time.Clock().tick(1)


def fashion_grid(camemberts):
    block_size = 50
    grid_width = 3
    grid_height = 2
    rect_blue=pg.Rect(1800, 800, block_size, block_size)
    rect_yellow=pg.Rect(1800-1*block_size, 800-0*block_size, block_size, block_size)
    rect_green=pg.Rect(1800-2*block_size, 800-0*block_size, block_size, block_size)
    rect_pink=pg.Rect(1800-0*block_size, 800-1*block_size, block_size, block_size)
    rect_orange=pg.Rect(1800-1*block_size, 800-1*block_size, block_size, block_size)
    rect_purple=pg.Rect(1800-2*block_size, 800-1*block_size, block_size, block_size)
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pg.Rect(1800-x*block_size, 800-y*block_size, block_size, block_size)
            pg.draw.rect(screen, (255,255,255), rect,1)
    if camemberts[0] == 1:
        pg.draw.rect(screen, (0,0,255), rect_blue)
    if camemberts[1] == 1:
        pg.draw.rect(screen, (255,255,0), rect_yellow)
    if camemberts[2] == 1:
        pg.draw.rect(screen, (0,255,0), rect_green)
    if camemberts[3] == 1:
        pg.draw.rect(screen, (255,0,255), rect_pink)
    if camemberts[4] == 1:
        pg.draw.rect(screen, (255,128,0), rect_orange)
    if camemberts[5] == 1:
        pg.draw.rect(screen, (238,130,238), rect_purple)
            

def dice():
    dice = random.randint(1,6)
    text = smallfont.render(str(dice) , True , white)
    pg.draw.rect(screen,(0,0,0),[screen_width-200,screen_height/2-140,140,40])
    screen.blit(text,(screen_width-200,screen_height/2-140))
    return dice

def turn_display():
    text = smallfont.render(f"nombre de tours : {player1.nb_of_turns}" , True , white)
    pg.draw.rect(screen,(0,0,0),[screen_width-300,screen_height/2-40,240,40])
    screen.blit(text,(screen_width-300,screen_height/2-40))


def check_camembert(case):
    if len(case)>1:
        if case[0]=="bleu":
            player1.add_blue_camembert()
        if case[0]=="jaune":
            player1.add_yellow_camembert()
        if case[0]=="vert":
            player1.add_green_camembert()
        if case[0]=="rose":
            player1.add_pink_camembert()
        if case[0]=="orange":
            player1.add_orange_camembert()
        if case[0]=="violet":
            player1.add_purple_camembert()    




player1 = Player("player1")
screen.blit(image,(0,0))

while True:
    # screen.blit(image,(0,0))
    pg.display.update()
    mouse = pg.mouse.get_pos()
    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2,140,40]) 
    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2+40,140,40])

    screen.blit(text3 , (screen_width+50-200,screen_height/2+5))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
    # screen.blit(pg.transform.scale(image_token, (50,50)), (450, 450))
    keys = pg.key.get_pressed()
    for ev in pg.event.get():

        if ev.type == pg.QUIT: 
            pg.quit()     

        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40 and ev.type == pg.MOUSEBUTTONDOWN:
        
            screen.blit(text3 , (screen_width+50-200,screen_height/2+5))
            die = dice()
            turn_display()
            position = player1.position
            player1.move("left", die)
            new_position = player1.position
            camemberts = player1.camemberts
            fashion_grid(camemberts)
            move_piece("LEFT", position, new_position, die)
            case = board_game[player1.position].split("_")
            if case[0] != "blanc":
                reponse = display_question(choose_card(case[0].lower()))
            screen.blit(pg.transform.scale(image_token, (50,50)), (test[new_position][0]-25, test[new_position][1]-25))
            

        if keys[pg.K_a]:
            pg.draw.rect(screen,(0,0,0),[1100,0,900,400])
            if reponse == "A":
                check_camembert(case)                   
            else:
                player1.add_turn()
                print("mauvaise réponse")
        if keys[pg.K_b]:
            pg.draw.rect(screen,(0,0,0),[1100,0,900,400])
            if reponse == "B":
                check_camembert(case)                   
            else:
                player1.add_turn()

        if keys[pg.K_c]:
            pg.draw.rect(screen,(0,0,0),[1100,0,900,400])    
            if reponse == "C":
                check_camembert(case)                   
            else:
                player1.add_turn()

        if keys[pg.K_d]:
            pg.draw.rect(screen,(0,0,0),[1100,0,900,400])
            if reponse == "D":
                check_camembert(case)                   
            else:
                player1.add_turn()


        #if the mouse is clicked on the button the game is terminated 
        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80 and ev.type == pg.MOUSEBUTTONDOWN:
            pg.quit()
