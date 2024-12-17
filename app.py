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
image_token = pg.image.load('Trivialpursuit_Token2.png')
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

def move_piece(direction, dice):
    if direction == "LEFT":
        for coordinates in test[0:dice]:
            screen.blit(pg.transform.scale(image_token, (50,50)), (coordinates[0]-25, coordinates[1]-25))
            pg.time.Clock().tick(10)
            pg.display.flip()
            screen.blit(image,(0,0))
            pg.time.Clock().tick(10)


def finished_moving_piece(dice):
    screen.blit(pg.transform.scale(image_token, (50,50)), (test[dice][0]-25, test[dice][1]-25))
    pg.time.Clock().tick(1)

def fashion_grid():
    block_size = 50
    grid_width = 3
    grid_height = 2
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pg.Rect(1800-x*block_size, y*block_size+5, block_size, block_size)
            pg.draw.rect(screen, (255,255,255), rect,1)
            if (x,y) == (0,1):
                pg.draw.rect(screen, (255,0,0), rect)
            # if (x,y) in list_positions_fish:
            #     pg.draw.rect(screen, color=,rect ,1)
            #     screen.blit(nemo,(x*block_size+150,y*block_size+5))
            # elif (x,y) in list_positions_shark:
            #     shark = pygame.transform.scale(shark,(25,25))
            #     screen.blit(shark,(x*block_size+150,y*block_size+5))
            # else:
            #     pass
            # pygame.draw.rect(screen, blue_grid, rect,1)

# def dice():

police = pg.font.Font(None,24)
text_color = (0,0,0)


while True:
    screen.blit(image,(0,0))
    pg.display.update()
    mouse = pg.mouse.get_pos() 

    # nombre_camemberts = police.render("Nombre de camemberts", True, text_color)
    # nombre_camemberts_var = police.render(f'{mean_age_fishes}', True, text_color)


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
                fashion_grid()
                move_piece(5)
                finished_moving_piece(5)
            #if the mouse is clicked on the button the game is terminated 
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                pg.quit()


average_fish_age_display = police.render(f"Average fish age:", True, text_color)
average_fish_age_var_display = police.render(f'{mean_age_fishes}', True, text_color)
average_shark_age_display = police.render(f"Average shark age:", True, text_color)
average_shar_age_var_display = police.render(f'{mean_age_sharks}', True, text_color)


screen.blit(fish_number, (1050,100))
screen.blit(shark_number, (1050,150))