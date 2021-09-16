import random
import config

from Controller.Enum.Img import Img
from Components.Component import Component

class Cloud(Component):

    def __init__(self, cloud_list):
        self.IMG = Img.CLOUD_IMG.value
        self.WIDTH = self.IMG.get_width()
        self.y = random.randrange(20, 275)
        self.x = config.WIN_WIDTH + self.WIDTH
        self._vel = 2
        self.is_collide = self.collide_cloud(cloud_list)

    #need to be reviewed
    def collide_cloud(self, cloud_list):
        if len(cloud_list) > 0:
            for _, cloud in enumerate(cloud_list):
                if cloud.y + config.WIN_HEIGHT < self.y:
                    return False
            return True
        else:
            return True 

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, value):
        self._vel = value 

            
