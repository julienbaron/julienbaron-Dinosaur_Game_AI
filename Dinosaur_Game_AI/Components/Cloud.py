import pygame as pg
import os
import random
import config
class Cloud(object):
    def __init__(self, cloud_list):
        self.IMG = pg.image.load(os.path.join("Sprites","Cloud.PNG"))
        self.WIDTH = self.IMG.get_width()
        self.y = random.randrange(20, 275)
        self.x = config.WIN_WIDTH + self.WIDTH
        self.vel = 2
        self.is_collide = self.collide_cloud(cloud_list)

    def collide_cloud(self, cloud_list):
        if len(cloud_list) > 0:
            for _, cloud in enumerate(cloud_list):
                if cloud.y + config.WIN_HEIGHT < self.y:
                    return False
            return True
        else:
            return True 

    def move(self):
        self.x -= self.vel 

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

            
