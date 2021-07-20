import pygame as pg 
import os 

class Dinosaur(object):
    """description of class"""

    
    STAY_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_1.PNG"))
    CRAWL_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_5.PNG"))

    def __init__(self, x, y):
        self.RUN_DINOSAUR_IMG = [pg.image.load(os.path.join("Sprites","Dinosaur_2.PNG")), pg.image.load(os.path.join("Sprites","Dinosaur_3.PNG"))] 
        self.x = x 
        self.y = y
        self.image_count = 0
        self.img = self.RUN_DINOSAUR_IMG[0]
        self.is_jump = False
        self.jump_count = 10
        self.ANIMATION_TIME = 7
        self.is_crawling = False 

    def jump(self):
        if self.is_jump == True: 
            if self.jump_count >= -10:
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 0.7
            else:
                self.jump_count = 10
                self.is_jump = False

    def crawl(self):
        if self.is_jump == False and self.is_crawling == True: 
            self.y += 60 if self.y < 450 else 0 
        elif self.is_jump == False and self.is_crawling == False:
            self.y = 390

    def draw(self, win):
        if self.is_jump == True:
            self.img = self.STAY_DINOSAUR_IMG
        elif self.is_crawling == True:
            self.img = self.CRAWL_DINOSAUR_IMG
        else:
            self.image_count += 1 
            if self.image_count < self.ANIMATION_TIME:
                self.img = self.RUN_DINOSAUR_IMG[0]
            elif self.image_count < self.ANIMATION_TIME*2:
                self.img = self.RUN_DINOSAUR_IMG[1]
            elif self.image_count < self.ANIMATION_TIME*3:
                self.image_count = 0
        win.blit(self.img, (self.x , self.y))
            
    def get_mask(self):
        return pg.mask.from_surface(self.img)
    
    def get_jump(self):
        return self.jump_count
    
    def setIsJump(self, value:bool):
        self.is_jump = value 
        
    def setIsCrawling(self, value:bool):
        self.is_crawling = value

