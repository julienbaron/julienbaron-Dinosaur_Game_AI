import pygame as pg 
import os 
import random 

class Bird(object):
    """description of class"""
    def __init__(self, x, vel):
        self.BIRD_IMG = [pg.image.load(os.path.join("Sprites","Base_1.PNG")), pg.image.load(os.path.join("Sprites","Base_1.PNG"))]
        self.x  = x 
        self.y = random.randrange(20, 30)
        self.img = self.BIRD_IMG[0]
        self.vel = vel
        self.img_count = 0
        self.animationTime = 3

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.animationTime:
            self.img = self.BIRD_IMG[0]
        elif self.img_count < self.animationTime*2:
            self.img = self.BIRD_IMG[1]
            self.img_count = 0

        win.blit(self.img, (self.x, self.y))

    def collide_bird(self, dinausor):
        dinosaur_mask = dinausor.get_mask()
        bird_mask = pg.mask.from_surface(self.img)

        calculate_coordonate = (self.x - dinausor.x, self.y - round(dinausor.y))

        collide_point = dinosaur_mask.overlap(bird_mask, calculate_coordonate)

        if self.collide_bird:
            return True 

        return False 


    

