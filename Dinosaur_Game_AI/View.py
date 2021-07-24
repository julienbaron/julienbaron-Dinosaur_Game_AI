import pygame as pg 
import os
import config
pg.font.init()

STAT_FONT = pg.font.Font("dogica.ttf", 20)
class View():
    """description of class"""

    def DrawWindow(obstacleList, dinosaurs, base, cloudList, win, score):
        BACKGROUND_IMG = pg.transform.scale2x(pg.image.load(os.path.join("Sprites","Background_2.PNG")))
        win.blit(BACKGROUND_IMG,(0,0))
        base.draw(win)
        [cloud.draw(win) for cloud in cloudList]
        [obstacle.draw(win) for obstacle in obstacleList]
        dinosaurs.draw(win)
        text = STAT_FONT.render("Score:" + str(score),1, (0,0,0))
        win.blit(text, (config.WIN_WIDTH - 10 - text.get_width(), 10))
        pg.display.update()


