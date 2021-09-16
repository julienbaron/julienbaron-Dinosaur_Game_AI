import pygame as pg 
import random 
import config

from Controller.Enum.Img import Img
from Components.Component import Component

class Bird(Component):
    """description of class"""
    def __init__(self, vel):
        self.BIRD_IMG = [Img.BIRD_IMG_1.value, Img.BIRD_IMG_2.value]
        self.y = random.randrange(350, 450)
        self.img = self.BIRD_IMG[0]
        self.WIDTH = self.img.get_width()
        self._vel = vel + 6.5
        self._x = config.WIN_WIDTH + self.WIDTH
        self.img_count = 0
        self.animationTime = 10

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.animationTime:
            self.img = self.BIRD_IMG[0]
        elif self.img_count < self.animationTime*2:
            self.img = self.BIRD_IMG[1]
        elif self.img_count < self.animationTime*3:
            self.img_count = 0

        win.blit(self.img, (self._x, self.y))

    def collide_bird(self, dinausor):
        dinosaur_mask = dinausor.get_mask()
        bird_mask = pg.mask.from_surface(self.img)
 
        calculate_coordonate = (round(self._x) - dinausor.x, self.y - round(dinausor.y))
        collide_point = dinosaur_mask.overlap(bird_mask, calculate_coordonate)

        return True if collide_point != None else False

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, value):
        self._vel = value 

    @property
    def x(self):
        print("method called")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value






    

