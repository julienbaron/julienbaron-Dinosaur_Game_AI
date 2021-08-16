import pygame as pg 
import config
from View.GameView import GameView
import pdb
import time 
import random
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Bird import Bird 
from Components.Cloud import Cloud
from Controller import KeyManager
from Controller.Encryption import Encryption
from Model.JsonMethod import JsonMethod



class Manager(object):
    """description of class"""
    def manageGame(self):
        dino = [Dinosaur(100,390)]
        base = Base(480)
        bird= Bird(base.getVel())
        cloud_list = []
        obstacleList = []
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        pg.display.set_caption('Dinosaur_Game_AI')
        score = 0 
        run = True 
        while run :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False 
                    pg.quit()
                    return False 
                else:
                    KeyManager.KeyManager.keyPressed(event, dino[0])
            if random.randrange(0, 120) == 2 and len(cloud_list) <= 3 :
                if len(cloud_list) == 0 or cloud_list[-1].x < config.WIN_WIDTH and len(cloud_list) > 0: 
                    cloud_list.append(Cloud(cloud_list))
                else:
                    print('False')
            last_obstacle = obstacleList[-1] if len(obstacleList) != 0 else None
            if len(obstacleList) <= 3: 
                if last_obstacle == None or last_obstacle.x < 500:
                    generate_random_obstacle = random.randrange(0,5)
                    if generate_random_obstacle %2 == 0:
                        obstacleList.append(Bird(base.getVel()))
            for obs in obstacleList:
                if obs.collide_bird(dino[0]) == True:
                    dino[0].set_dead(True)
                    dino[0].setIsJump(False)
                    dino[0].setIsCrawling(False)
                    GameView.DrawWindow(obstacleList, dino, base, cloud_list, win, score)
                    time.sleep(1)
                    self.manage_highscore(score)
                    return False 
            score += 1
            base.move()
            [d.jump() for d in dino]
            [d.crawl() for d in dino]
            cloud_list = self.manage_list(cloud_list)
            obstacleList = self.manage_list(obstacleList)
            GameView.DrawWindow(obstacleList, dino, base, cloud_list, win, score)
   
    def manage_list(self, list):
        for index, object in enumerate(list):
            object.move()
            if object.x + object.WIDTH < 0:
                del list[index]
        return list 

    def manage_highscore(self, actual_score):
        existing_data = JsonMethod.check_json()
        #key = Encryption.get_key()
        if existing_data == True:
            json_data = JsonMethod.read_json('storage', existing_data)
            #json_data = Encryption.decrypt(data, key)
        else:
           json_data = 0
        if int(json_data) < actual_score:
            JsonMethod.write_json('storage', actual_score)