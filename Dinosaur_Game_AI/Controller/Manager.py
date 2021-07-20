import pygame as pg 
import config
from View import View
import pdb
import random
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Bird import Bird 
from Components.Cloud import Cloud
from Controller import KeyManager

GEN = 0

class Manager(object):
    """description of class"""
    @staticmethod
    def manageGame():
        dino = Dinosaur(100,390)
        base = Base(480)
        bird= Bird(base.getVel())
        cloudList = []
        obstacleList = []
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        clock = pg.time.Clock()
        run = True 
        while run :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False 
                    pg.quit()
                    return False 
                else:
                    KeyManager.KeyManager.keyPressed(event, dino)
            if random.randrange(0, 200) == 2 and len(cloudList) <= 3 :
                cloudList.append(Cloud())
            last_obstacle = obstacleList[-1] if len(obstacleList) != 0 else None
            if len(obstacleList) <= 3: 
                if last_obstacle == None or last_obstacle.x < 500:
                    generate_random_obstacle = random.randrange(0,5)
                    if generate_random_obstacle %2 == 0:
                        obstacleList.append(Bird(base.getVel()))
            #for bird in birds:
            #    if bird.collide_bird(dino):
            #        pass 
            #    if bird.x + bird.img.get_width() < 0:
            #        #rem.append(bird)
            #        pass
            base.move()
            dino.jump()
            dino.crawl()
            for index,cloud in enumerate(cloudList): 
                cloud.move()
                if cloud.x + cloud.WIDTH == 0:
                    del cloudList[index]
            for index, obs in enumerate(obstacleList): 
                obs.move()
                if obs.x + obs.WIDTH <= 0:
                    del obstacleList[index]
                print(obs.x)
            View.DrawWindow(obstacleList, dino, base, cloudList, win)
       


