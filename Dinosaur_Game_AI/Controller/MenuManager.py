import config
import pygame as pg 

from View.MainView import MainView
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Button import Button
from Controller.Enum.Img import Img
from Controller.Manager import Manager

class MenuManager():
    """description of class"""
    def __init__(self):
        #self.base = Base(config.BASE_HEIGHT)
        #self.dino = Dinosaur(config.DINO_WIDTH, config.DINO_HEIGHT)
        self.component_list = [Base(config.BASE_HEIGHT), Dinosaur(config.DINO_WIDTH, config.DINO_HEIGHT)]
        self.start = False

    def menu_view(self):
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        pg.display.set_caption('Dinosaur_Game_AI')
        counter = 0
        while self.start == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False 
                    pg.quit()
                    return False 
            regular = Button(100,230, Img.REGULAR_IMG.value, 0.7)
            if regular.is_clicked():
                manage = Manager()
                manage.manageGame()
            [x.move() for x in self.component_list if isinstance(x, Base)]
            counter += 1 if counter <= 21 else -20
            MainView.draw_window(win, self.component_list, regular, counter)

            

                



