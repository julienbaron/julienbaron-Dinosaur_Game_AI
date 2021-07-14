import pygame as pg 
import config
from View import View
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Bird import Bird 

GEN = 0

class Controller(object):
    """description of class"""
    @staticmethod
    def Controller():
        #global GEN 
        #base = Base(50)
        #win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        #run = True 
        #while run :
        #    for event in pg.event.get():
        #        if event.type == pg.QUIT:
        #            run = False 
        #            pg.quit()
        #            break

        #View.DrawWindow(win, base)
        dino = Dinosaur(100,100)
        base = Base(50)
        birds= [Bird(10, 1)]
        rem = []
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        clock = pg.time.Clock()
        run = True 
        while run :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False 
                    pg.quit()
                    break

            for bird in birds:
                if bird.collide_bird(dino):
                    pass 
                if bird.x + bird.img.get_width() < 0:
                    rem.append(bird)
            bird.move()
            base.move()
            View.DrawWindow(birds, dino, base, win)


