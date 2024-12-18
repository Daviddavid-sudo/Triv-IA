import pygame as pg
import math
import time
import random
from players import Player

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

test = piece()

def move_piece(direction, position, new_position, die):
    if direction == "LEFT":
        for coordinates in test[position:new_position]:
            screen.blit(pg.transform.scale(image_token, (50,50)), (coordinates[0]-25, coordinates[1]-25))
            pg.time.Clock().tick(10)
            pg.display.flip()
            screen.blit(image,(0,0))
            pg.time.Clock().tick(5)
        

def finished_moving_piece(new_position):
    screen.blit(pg.transform.scale(image_token, (50,50)), (test[new_position][0]-25, test[new_position][1]-25))
    pg.time.Clock().tick(1)


def fashion_grid(camberts):
    block_size = 50
    grid_width = 3
    grid_height = 2
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pg.Rect(1800-x*block_size, y*block_size+5, block_size, block_size)
            pg.draw.rect(screen, (255,255,255), rect,1)

    if camemberts[0] == 1:
        pg.draw.rect(screen, (255,0,0), rect)
    if camemberts[1] == 1:
        pg.draw.rect(screen, (255,255,0), rect)
            

def dice():
    dice = random.randint(1,6)
    text = smallfont.render(str(dice) , True , white)
    screen.blit(text,(screen_width-200,screen_height/2-140))
    return dice


player1 = Player("player1")
camemberts = [0,1]

while True:
    screen.blit(image,(0,0))
    pg.display.update()
    mouse = pg.mouse.get_pos()
    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2,140,40]) 
    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2+40,140,40])
    screen.blit(text3 , (screen_width+50-200,screen_height/2+5))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+45))

    for ev in pg.event.get(): 
        if ev.type == pg.QUIT: 
            pg.quit()     

        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40 and ev.type == pg.MOUSEBUTTONDOWN:

            screen.blit(text3 , (screen_width+50-200,screen_height/2+5))
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                die = dice()
                position = player1.position
                player1.move(die)
                new_position = player1.position
                fashion_grid(camemberts)
                move_piece("LEFT", position, new_position, die)
                finished_moving_piece(new_position)
                camemberts = player1.camemberts
                fashion_grid(camemberts)
            else:
                time.sleep(100)
                

        #if the mouse is clicked on the button the game is terminated 
        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80 and ev.type == pg.MOUSEBUTTONDOWN:
            pg.quit()
