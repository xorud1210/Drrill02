from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

square = True
x = 0
y = 90
angle = 270
while True:
    if(square == True):
        while (x < 780):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 2
            delay(0.01)
        while(y < 550 and x == 780):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y+2
            delay(0.01)
        while(y == 550 and x > 20):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 2
            delay(0.01)
        while(y > 90 and x == 20):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y-2
            delay(0.01)
        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 2
            delay(0.01)
        square = False           
    elif(square == False):
        while(angle < 630):
            x = 400 + math.cos(angle / 360 * 2 * math.pi) * 240
            y = 330 + math.sin(angle / 360 * 2 * math.pi) * 240
            angle = angle + 1
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01)
        square = True
        angle = 270
        y = 90
        x = 400       
