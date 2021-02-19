import pygame as pg
from time import sleep

pg.init()

black = (0, 0, 0)
white = (255, 255, 255)

width = 1000
height = 500
pg.display.set_caption('A really bad Pong')
screen = pg.display.set_mode((width, height))


def screen_text(text, x_coord, y_coord, color, size, font, r=0):
    msg = pg.font.SysFont(font, size).render(str(text), True, color)
    screen.blit(msg, msg.get_rect(center=(x_coord, y_coord)))
    if r:
        return msg.get_rect(center=(x_coord, y_coord))
print(pg.font.get_fonts())

def game_loop():
    i = 0
    game_over = False
    while not game_over:
        screen.fill(black)
        screen_text("Testando fonte", width/2, 100, white, 30, pg.font.get_fonts()[i])
        screen_text(pg.font.get_fonts()[i], width/2, 200, white, 30, pg.font.get_fonts()[i])
        i += 1
        sleep(0.5)
        pg.display.update()


game_loop()
