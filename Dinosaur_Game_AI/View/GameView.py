import pygame as pg 
import os
import config
from Model.JsonMethod import JsonMethod

pg.font.init()

STAT_FONT = pg.font.Font("dogica.ttf", 20)
class GameView():
    """description of class"""

    def DrawWindow(obstacleList, dinosaurs, base, cloudList, win, score):
        BACKGROUND_IMG = pg.transform.scale2x(pg.image.load(os.path.join("Sprites","Background_2.PNG")))
        win.blit(BACKGROUND_IMG,(0,0))
        base.draw(win)
        [cloud.draw(win) for cloud in cloudList]
        [obstacle.draw(win) for obstacle in obstacleList]
        dinosaurs.draw(win)
        actual_score = STAT_FONT.render("Score:" + str(score),1, (0,0,0))
        win.blit(actual_score, (config.WIN_WIDTH - 10 - actual_score.get_width(), 10))
        if JsonMethod.check_json() == True:
            high_score = STAT_FONT.render("High Score:" + str(JsonMethod.read_json('storage', JsonMethod.check_json())),1, (0,0,0))
            win.blit(high_score, (config.WIN_WIDTH - 20 - actual_score.get_width() - high_score.get_width(), 10))
        pg.display.update()


