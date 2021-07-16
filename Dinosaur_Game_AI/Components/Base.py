import pygame as pg 
import os 

class Base(object):
    """description of class"""
    def __init__(self, y):
        self.BASE_IMG = pg.image.load(os.path.join("Sprites","Base_2.PNG"))
        self.WIDTH = self.BASE_IMG.get_width()
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.vel = 3

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel 

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

        #self.vel += 0.1

    def draw(self, win):
        win.blit(self.BASE_IMG, (self.x1, self.y))
        win.blit(self.BASE_IMG, (self.x2, self.y))


