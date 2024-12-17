import pygame as pg
import math
import time

(width,height) = (1920,1080)
screen = pg.display.set_mode((width, height))
screen_width = screen.get_width()
screen_height = screen.get_height()
white = (255,255,255)
colour_dark = (100,100,100)
pg.init()
fps = pg.time.Clock()

image = pg.image.load('trivial_plateau.png')
smallfont = pg.font.SysFont('Corbel',35)
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
text3 = smallfont.render('graph' , True , white)
text4 = smallfont.render('return' , True , white)

def piece():
    test = []
    pg.draw.circle(image, (255,255,255), (515, 510), 400)
    center = (screen_width/2-450, screen_height/2-18)
    radius = 455
    cases= 45

    angle = 0
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    test.append((x,y))

    for i in range(1,7):
        angle = (2 * math.pi / cases) * i
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 8) - 0.08
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(9,15):
        angle = ((2 * math.pi / cases) * i) - 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 15) 
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(16,22):
        angle = ((2 * math.pi / cases) * i) + 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 22) + 0.08
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(24,30):
        angle = ((2 * math.pi / cases) * i)
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 30) 
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(31,37):
        angle = ((2 * math.pi / cases) * i) + 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    angle = ((2 * math.pi / cases) * 38) - 0.05
    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))
    test.append((x,y))
    pg.draw.circle(image, (100,100,100), (x, y), 25)
    
    for i in range(39,45):
        angle = ((2 * math.pi / cases) * i) - 0.05
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        test.append((x,y))
        pg.draw.circle(image, (100,100,100), (x, y), 25)

    return test

def move_piece():
    test = piece()
    for coordinates in test:
        pg.draw.circle(image, (100,100,100), coordinates, 25)
        fps.tick(10)

while True:
    screen.blit(image,(0,0))
    pg.display.update()
    mouse = pg.mouse.get_pos() 

    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2,140,40]) 
    pg.draw.rect(screen,colour_dark,[screen_width-200,screen_height/2+40,140,40]) 
    screen.blit(text1 , (screen_width+50-200,screen_height/2+5))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+45))

    for ev in pg.event.get(): 
        if ev.type == pg.QUIT: 
            pg.quit()     
        #check if a mouse is clicked 
        if ev.type == pg.MOUSEBUTTONDOWN: 
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                move_piece()
            #if the mouse is clicked on the button the game is terminated 
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                pg.quit()