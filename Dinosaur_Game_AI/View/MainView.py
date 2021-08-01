import pygame as pg 
import os 

class MainView():
    """description of class"""
    def draw_window(win, component, regular):
        BACKGROUND_IMG = pg.transform.scale2x(pg.image.load(os.path.join("Sprites","Background_2.PNG")))
        win.blit(BACKGROUND_IMG,(0,0))
        [comp.draw(win) for comp in component]
        regular.draw(win)
        pg.display.update()





