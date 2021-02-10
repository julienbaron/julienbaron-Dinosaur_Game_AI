import pygame as pg 
import os 

class Dinosaur(object):
    """description of class"""

    RUN_DINOSAUR_IMG = [pg.image.load(os.path.join("Sprites","Dinosaur_2.PNG")), pg.image.load(os.path.join("Sprites","Dinosaur_3.PNG"))]
    STAY_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_1.PNG"))

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.image_count = 0
        self.img = RUN_DINOSAUR_IMG[0]
        self.is_jump = False
        self.jump_count = 4
        self.ANIMATION_TIME = 2

    def jump(self):
        if self.jump_count >= -4:
            self.is_jump = True 
            self.y -= (jump_count * abs(jump_count)) * 0.5
            self.jump_count -= 1 
        else:
            self.jump_count = 4
            self.is_jump = False

    def draw(self, win):
        if not jump():
            self.image_count += 1 
            if self.img_count < self.ANIMATION_TIME:
                self.img = RUN_DINOSAUR_IMG[0]
            elif self.img_count < self.ANIMATION_TIME*2:
                self.img = RUN_DINOSAUR_IMG[1]
                self.img_count = 0
        else: 
            self.img = self.STAY_DINOSAUR_IMG

        win.blit(self.img, (self.x , self.y))
            

    def get_mask(self):
        return pg.mask.from_surface(self.img)
        
        

