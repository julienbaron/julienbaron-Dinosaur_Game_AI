import pygame as pg 
import config
import neat
import pdb
import time 
import random
import os

from View.GameView import GameView
from Components.Base import Base
from Components.Dinosaur import Dinosaur
from Components.Bird import Bird 
from Components.Cloud import Cloud
from Controller.KeyManager import KeyManager
from Controller.Encryption import Encryption
from Model.JsonMethod import JsonMethod
from Controller.RandomizeEvent import RandomizeEvent

class Manager():
    
    def __init__(self, game_mode):
        self.game_mode = game_mode 
        self.dinos = []
        self.gen = 0
        self.base = Base(config.BASE_HEIGHT)
        self.bird = Bird(self.base.vel)
        self.cloud_list = []
        self.obsctacle_list = []
        self.win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        pg.display.set_caption('Dinosaur_Game_AI')
        self.score = 0
        self.run = True

    def start(self):
        if self.game_mode == 0: self.dinos.append(Dinosaur(config.DINO_WIDTH, config.DINO_HEIGHT))
        while self.run == True:
            for _,event in enumerate(pg.event.get()):
                if event.type == pg.QUIT:
                    self.run = False
                    pg.quit()
                    return False
                self.key_manager(event.type, event) if self.game_mode == 0 else None
            self.randomize_cloud()
            #self.regular_manager() if self.game_mode == 0 else self.AI_manager()
            if len(self.dinos) > 0: self.score += 1
            self.base.move()
            [d.jump() for d in self.dinos]
            [d.crawl() for d in self.dinos]
            cloud_list = self.manage_list(self.cloud_list)
            obstacleList = self.manage_list(self.obsctacle_list)
            GameView.DrawWindow(self.obsctacle_list, self.dinos, self.base, self.cloud_list, self.win, self.score)

    def AI_manager(self, genomes, generation):
        self.nets = []
        self.ge = []
        self.gen += 1 
        for index,g in enumerate(genomes):
            net = neat.nn.FeedForwardNetwork.create(g, generation)
            nets.append(net)
            self.dinos.append(Dinosaur(config.DINO_WIDTH, config.DINO_HEIGHT))
            self.g.fitness = 0
            self.ge.append(g)

        for index, dino in enumerate(dinos):
            if len(self.obsctacle_list) >0:
                output = nets[index].activate(dino.y(), dino.x, abs(obstacleList[0].x), abs(obstacleList[0].y))
                print(output)
                dino.is_jump(True) if output[0] > 0.5 else dino.is_jump(False)
                dino.is_crawling(True) if output[0] < 0.5 else dino.is_crawling(False)
        
        self.AI_manager()
        self.obstacle_collide_AI()

    def key_manager(self, event_type, event):
        if event_type != pg.QUIT:
            KeyManager.keyPressed(event, self.dinos[0])

    def regular_manager(self):
        random_cloud = RandomizeEvent(120, self.cloud_list, config.WIN_WIDTH)
        self.obstacle_collide_regular()

    def manage_component_list(self, list_component):
        for index, object in enumerate(list_component):
            object.x = object.move(object.x, object.vel)
            if object.x + object.WIDTH < 0:
                del list_component[index]
        return list_component 

    def wrapper_collide(func):
        def obstacle_collide(self):
            for obs in self.obsctacle_list:
                for index, x in (dino for index, dino in enumerate(self.dinos) if obs.collide_bird(self.dinos[index]) == True):
                    func()

    @wrapper_collide
    def obstacle_collide_regular(self):
            self.dinos[index].is_dead = True 
            self.dinos[index].is_jump = False 
            self.dinos[index].is_crawling = False 
            GameView.DrawWindow(self.obstacleList, self.dinos, self.base, self.cloud_list, self.win, self.score)
            time.sleep(1)
            self.manage_highscore(score)
            return False 

    @wrapper_collide
    def obstacle_collide_AI(self):
        self.ge[index].fitness -= 1
        x.is_dead = True 
        x.is_jump = False
        x.is_crawling = False 
        dinos.pop(index)
        self.manage_highscore(score)

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

    def manage_list(self, list):
        for index, object in enumerate(list):
            object.x = object.move(object.x, object.vel)
            if object.x + object.WIDTH < 0:
                del list[index]
        return list 
               
    def run_neat(self):
        local_dir = os.getcwd()
        config_neat = os.path.join(local_dir, 'Config_Neat.txt')
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                                config_neat)
        p = neat.Population(config)

        winner = p.run(self.AI_manager, 10000)


        

#class Manager(object):
#    """description of class"""
#    def manageGame(self):
#        dino = [Dinosaur(100,390)]
#        base = Base(480)
#        bird= Bird(base.vel)
#        cloud_list = []
#        obstacleList = []
#        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
#        pg.display.set_caption('Dinosaur_Game_AI')
#        score = 0 
#        run = True 
#        while run :
#            for event in pg.event.get():
#                if event.type == pg.QUIT:
#                    run = False 
#                    pg.quit()
#                    return False 
#                else:
#                    KeyManager.KeyManager.keyPressed(event, dino[0])
#            if random.randrange(0, 120) == 2 and len(cloud_list) <= 3 :
#                if len(cloud_list) == 0 or cloud_list[-1].x < config.WIN_WIDTH and len(cloud_list) > 0: 
#                    cloud_list.append(Cloud(cloud_list))
#                else:
#                    print('False')
#            last_obstacle = obstacleList[-1] if len(obstacleList) != 0 else None
#            if len(obstacleList) <= 3: 
#                if last_obstacle == None or last_obstacle.x < 500:
#                    generate_random_obstacle = random.randrange(0,5)
#                    if generate_random_obstacle %2 == 0:
#                        obstacleList.append(Bird(base.vel))
#            for obs in obstacleList:
#                if obs.collide_bird(dino[0]) == True:
#                    dino[0].is_dead = True
#                    dino[0].is_jump = False 
#                    dino[0].is_crawling = False 
#                    GameView.DrawWindow(obstacleList, dino, base, cloud_list, win, score)
#                    time.sleep(1)
#                    self.manage_highscore(score)
#                    return False 
#            score += 1
#            base.move()
#            [d.jump() for d in dino]
#            [d.crawl() for d in dino]
#            cloud_list = self.manage_list(cloud_list)
#            obstacleList = self.manage_list(obstacleList)
#            GameView.DrawWindow(obstacleList, dino, base, cloud_list, win, score)
   
#    def manage_list(self, list):
#        for index, object in enumerate(list):
#            object.x = object.move(object.x, object.vel)
#            if object.x + object.WIDTH < 0:
#                del list[index]
#        return list 

#    def manage_highscore(self, actual_score):
#        existing_data = JsonMethod.check_json()
#        #key = Encryption.get_key()
#        if existing_data == True:
#            json_data = JsonMethod.read_json('storage', existing_data)
#            #json_data = Encryption.decrypt(data, key)
#        else:
#           json_data = 0
#        if int(json_data) < actual_score:
#            JsonMethod.write_json('storage', actual_score)