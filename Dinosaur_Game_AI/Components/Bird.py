import pygame as pg 
import os 
import random 
import config

class Bird(object):
    """description of class"""
    def __init__(self, vel):
        self.BIRD_IMG = [pg.image.load(os.path.join("Sprites","Bird_1.PNG")), pg.image.load(os.path.join("Sprites","Bird_2.PNG"))]
        self.y = random.randrange(350, 450)
        self.img = self.BIRD_IMG[0]
        self.WIDTH = self.img.get_width()
        self.vel = vel + 6.5
        self.x = config.WIN_WIDTH + self.WIDTH
        self.img_count = 0
        self.animationTime = 10

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.animationTime:
            self.img = self.BIRD_IMG[0]
        elif self.img_count < self.animationTime*2:
            self.img = self.BIRD_IMG[1]
        elif self.img_count < self.animationTime*3:
            self.img_count = 0

        win.blit(self.img, (self.x, self.y))

    def collide_bird(self, dinausor):
        dinosaur_mask = dinausor.get_mask()
        bird_mask = pg.mask.from_surface(self.img)
 
        calculate_coordonate = (round(self.x) - dinausor.x, self.y - round(dinausor.y))
        collide_point = dinosaur_mask.overlap(bird_mask, calculate_coordonate)

        if collide_point != None:
            return True 

        return False 


    

