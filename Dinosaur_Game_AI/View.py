import pygame as pg 
import os

class View():
    """description of class"""
    @staticmethod
    def DrawWindow(birds, dinosaurs, base, win):
        BACKGROUND_IMG = pg.image.load(os.path.join("Sprites","Background.PNG"))
        win.blit(BACKGROUND_IMG,(0,0))
        for bird in birds:
            bird.draw(win)
        #for dinosaur in dinosaurs:
        #    dinosaur.draw(win)
        #base.draw(win)
        #pg.display.update()
        dinosaurs.draw(win)
        pg.display.update()


