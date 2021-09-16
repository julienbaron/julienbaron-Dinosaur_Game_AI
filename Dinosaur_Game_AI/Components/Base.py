from Controller.Enum.Img import Img
from Components.Component import Component

class Base(Component):
    """This class contains the functions necessary for the ground management in the game """

    def __init__(self, y):
        self.BASE_IMG = Img.BASE_IMG.value
        self.WIDTH = self.BASE_IMG.get_width()
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self._vel = 3

    def move(self):
        self.x1 -= self._vel
        self.x2 -= self._vel 

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

        #self.vel += 0.1

    def draw(self, win):
        win.blit(self.BASE_IMG, (self.x1, self.y))
        win.blit(self.BASE_IMG, (self.x2, self.y))

    @property
    def vel(self):
        return self._vel

    @vel.setter 
    def vel(self, value):
        self._vel = value


