import pygame as pg 
import config
from View import View
import pdb
import time 
import random
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Bird import Bird 
from Components.Cloud import Cloud
from Controller import KeyManager



class Manager(object):
    """description of class"""
    def manageGame(self):
        dino = Dinosaur(100,390)
        base = Base(480)
        bird= Bird(base.getVel())
        cloudList = []
        obstacleList = []
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        score = 0 
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
            for obs in obstacleList:
                if obs.collide_bird(dino) == True:
                    dino.set_dead(True)
                    dino.setIsJump(False)
                    dino.setIsCrawling(False)
                    View.DrawWindow(obstacleList, dino, base, cloudList, win, score)
                    time.sleep(1)
                    return False 
            score += 1
            base.move()
            dino.jump()
            dino.crawl()
            cloudList = self.manage_list(cloudList)
            obstacleList = self.manage_list(obstacleList)
            View.DrawWindow(obstacleList, dino, base, cloudList, win, score)
   
    def manage_list(self, list):
        for index, object in enumerate(list):
            object.move()
            if object.x + object.WIDTH == 0:
                del list[index]
        return list 