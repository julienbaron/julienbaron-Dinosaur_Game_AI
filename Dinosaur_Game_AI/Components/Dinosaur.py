import pygame as pg 

from Controller.Enum.Img import Img

class Dinosaur():
    """description of class"""

    def __init__(self, x, y):
        self.RUN_DINOSAUR_IMG = Img.RUN_DINOSAUR_IMG.value
        self._x = x 
        self._y = y
        self.image_count = 0
        self.img = self.RUN_DINOSAUR_IMG[0]
        self._is_jump = False
        self._jump_count = 10
        self.ANIMATION_TIME = 7
        self._is_crawling = False
        self._is_dead = False

    def jump(self):
        if self._is_jump == True: 
            if self._jump_count >= -10:
                self._y -= (self._jump_count * abs(self._jump_count)) * 0.5
                self._jump_count -= 0.5
            else:
                self._jump_count = 10
                self._is_jump = False

    def crawl(self):
        if self._is_jump == False and self._is_crawling == True: 
            self._y += 60 if self._y < 450 else 0 
        elif self._is_jump == False and self._is_crawling == False:
            self._y = 390

    def draw(self, win):
        if self._is_jump == True:
            self.img = Img.STAY_DINOSAUR_IMG.value
        elif self._is_crawling == True:
            self.img = Img.CRAWL_DINOSAUR_IMG.value
        elif self._is_dead == True:
            self.img = Img.DEAD_DINOSAUR_IMG.value
            self._y = 390
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
    
    @property
    def jump_count(self):
        return self._jump_count

    @jump_count.setter
    def jump_count(self, value):
        self._jump_count = value
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def is_jump(self):
        return self._is_jump

    @is_jump.setter
    def is_jump(self, value):
        self._is_jump = value

    @property
    def is_crawling(self):
        return self._is_crawling

    @is_crawling.setter
    def is_crawling(self, value):
        self._is_crawling = value

    @property
    def is_dead(self):
        return self._is_dead

    @is_dead.setter
    def is_dead(self, value:bool):
        self._is_dead = value
       

