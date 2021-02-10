import pygame as pg 
import os 
import random 

from Dinosaur_Game_AI.Components.Dinosaur import Dinosaur

class Bird(object):
    """description of class"""
    BIRD_IMG = [pg.image.load(os.path.join("Sprites","Base_1.PNG")), pg.image.load(os.path.join("Sprites","Base_1.PNG"))]
    ANIMATION_TIME = 3

    def __init__(self, x, vel):
        self.x  = x 
        self.y = random.randrange(20, 30)
        self.img = BIRD_IMG[0]
        self.vel = vel
        self.img_count = 0

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = BIRD_IMG[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = BIRD_IMG[1]
            self.img_count = 0

        win.blit(self.img, (self.x, self.y))

    def collide_bird(self):
        dinosaur_mask = Dinosaur.get_mask()
        bird_mask = pg.mask.from_surface(self.img)


    

