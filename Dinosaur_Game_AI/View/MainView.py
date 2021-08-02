import pygame as pg 
import os

import config

from Controller.Enum.Img import Img

class MainView():
    """description of class"""
    def draw_window(win, component, regular, count):
        BACKGROUND_IMG = pg.transform.scale2x(pg.image.load(os.path.join("Sprites","Background_2.PNG")))
        win.blit(BACKGROUND_IMG,(0,0)) 
        if  5 <= count <= 20 :
            win.blit(Img.TITLE_IMG.value,(config.WIN_WIDTH / 2 - 230, 100))
        [comp.draw(win) for comp in component]
        regular.draw(win)
        pg.display.update()





