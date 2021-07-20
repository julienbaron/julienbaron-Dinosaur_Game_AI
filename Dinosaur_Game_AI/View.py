import pygame as pg 
import os

class View():
    """description of class"""
    @staticmethod
    def DrawWindow(obstacleList, dinosaurs, base, cloudList, win):
        BACKGROUND_IMG = pg.transform.scale2x(pg.image.load(os.path.join("Sprites","Background_2.PNG")))
        win.blit(BACKGROUND_IMG,(0,0))
        base.draw(win)
        #for cloud in cloudList:
        #    cloud.draw(win)
        [cloud.draw(win) for cloud in cloudList]
        #for bird in birds:
        #    bird.draw(win)
        #for dinosaur in dinosaurs:
        #    dinosaur.draw(win)
        #pg.display.update()
        print(len(obstacleList))
        [obstacle.draw(win) for obstacle in obstacleList]
        dinosaurs.draw(win)
        pg.display.update()


