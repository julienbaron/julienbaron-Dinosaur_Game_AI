import pygame as pg 

class View(object):
    """description of class"""
    @staticmethod
    def DrawWindow(birds, dinosaurs, base, win):
        for bird in birds:
            bird.draw(win)
        #for dinosaur in dinosaurs:
        #    dinosaur.draw(win)
        #base.draw(win)
        #pg.display.update()
        dinosaurs.draw(win)
        pg.display.update()


