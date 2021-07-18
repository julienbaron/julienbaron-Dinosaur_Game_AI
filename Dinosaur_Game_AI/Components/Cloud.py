import pygame as pg
import os
import random
import config
class Cloud(object):
    def __init__(self):
        self.IMG = pg.image.load(os.path.join("Sprites","Cloud.PNG"))
        self.WIDTH = self.IMG.get_width()
        self.y = random.randrange(20, 275)
        self.x = config.WIN_WIDTH + self.WIDTH
        self.vel = 2
    
    def move(self):
        self.x -= self.vel 

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

            
