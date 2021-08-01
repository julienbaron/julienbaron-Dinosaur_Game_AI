import pygame as pg

from Controller.Enum.Img import Img

class Button(object):
    """description of class"""
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale 
        self.image = pg.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def is_clicked(self):
        action = False 
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image = pg.transform.scale(Img.REGULAR_ONCLICK.value, (int(self.width * self.scale), int(self.height * self.scale)))
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True 
                action = True 

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
