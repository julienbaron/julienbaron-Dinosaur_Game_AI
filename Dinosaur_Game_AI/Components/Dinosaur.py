import pygame as pg 
import os 

class Dinosaur(object):
    """description of class"""

    
    STAY_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_1.PNG"))

    def __init__(self, x, y):
        self.RUN_DINOSAUR_IMG = [pg.image.load(os.path.join("Sprites","Dinosaur_2.PNG")), pg.image.load(os.path.join("Sprites","Dinosaur_3.PNG"))] 
        self.x = x 
        self.y = y 
        self.image_count = 0
        self.img = self.RUN_DINOSAUR_IMG[0]
        self.is_jump = False
        self.jump_count = 10
        self.ANIMATION_TIME = 7

    def jump(self):
        print(self.is_jump)
        if self.is_jump == True: 
            if self.jump_count >= -10:
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False

    def draw(self, win):
        if self.is_jump == False:
            self.image_count += 1 
            if self.image_count < self.ANIMATION_TIME:
                self.img = self.RUN_DINOSAUR_IMG[0]
            elif self.image_count < self.ANIMATION_TIME*2:
                self.img = self.RUN_DINOSAUR_IMG[1]
            elif self.image_count < self.ANIMATION_TIME*3:
                self.image_count = 0
        else: 
            self.img = self.STAY_DINOSAUR_IMG

        win.blit(self.img, (self.x , self.y))
            
    def get_mask(self):
        return pg.mask.from_surface(self.img)
    
    def get_jump(self):
        return self.jump_count
    
    def setIsJump(self, value:bool):
        self.is_jump = value 
        

