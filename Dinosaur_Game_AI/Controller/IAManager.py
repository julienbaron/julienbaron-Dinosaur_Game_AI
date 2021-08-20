import os 
import neat 
import config
import pygame as pg 
import random
import time

from Controller.Enum.Img import Img
from Components.Dinosaur import Dinosaur
from Components.Base import Base
from Components.Bird import Bird
from Components.Cloud import Cloud 
from Controller.Manager import Manager
from View.GameView import GameView

class IAManager():
    """description of class"""
    def __init__(self):
        self.gen = 0 

    def manager(self, genomes, generation):
        nets = []
        ge = []
        dinos = []
        cloud_list = []
        obstacleList = []
        score = 0 
        run = True 
        self.gen += 1
        for _,g in genomes:
            net  = neat.nn.FeedForwardNetwork.create(g, generation)
            nets.append(net)
            dinos.append(Dinosaur(config.DINO_WIDTH, config.DINO_HEIGHT))
            g.fitness = 0
            ge.append(g)
        base = Base(480)
        bird = Bird(base.getVel())
        win = pg.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        pg.display.set_caption('Dinosaur_Game_AI')
        while run :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False 
                    pg.quit()
                    return False 
            for index, dino in enumerate(dinos):
                #ge[index] + 1 
                if len(obstacleList) > 0:
                    output = nets[index].activate((dino.get_y(), abs(obstacleList[0].x), abs(obstacleList[0].y)))
                    #print(dino.get_y())
                    #print(abs(obstacleList[0].x))
                    #print(abs(obstacleList[0].y))
                    #print('-------------------------------------')
                    dino.setIsJump(True) if output[0] > 0 else dino.setIsJump(False)
                    dino.setIsCrawling(True) if output [0] < 0 else dino.setIsCrawling(False)
            if random.randrange(0, 150) == 1 and len(cloud_list) <= 3 :
                new_cloud = Cloud(cloud_list)
                if new_cloud.is_collide == True:
                    cloud_list.append(Cloud(cloud_list)) 
            last_obstacle = obstacleList[-1] if len(obstacleList) != 0 else None
            if len(obstacleList) <= 3: 
                if last_obstacle == None or last_obstacle.x < 500:
                    generate_random_obstacle = random.randrange(0,5)
                    if generate_random_obstacle %2 == 0:
                        obstacleList.append(Bird(base.getVel()))
                        [g.fitness + 1.5 for g in ge ]
            for obs in obstacleList:
                for index, x in enumerate(dinos):
                    if obs.collide_bird(x) == True:
                        ge[index].fitness -= 1 
                        x.set_dead(True)
                        x.setIsJump(False)
                        x.setIsCrawling(False)
                        dinos.pop(index)
                        manage_highscore = Manager()
                        manage_highscore.manage_highscore(score)
            if len(dinos) > 0 :
                score +=1 
            else:
                print(score)
                return False 
            base.move()
            [d.jump() for d in dinos]
            [d.crawl() for d in dinos]
            method_list = Manager()
            cloud_list = method_list.manage_list(cloud_list)
            obstacleList = method_list.manage_list(obstacleList)
            GameView.DrawWindow(obstacleList, dinos, base, cloud_list, win, score)

    def run(self):
        global GEN
        local_dir = os.getcwd()
        config_neat = os.path.join(local_dir, 'Config_Neat.txt')
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                                config_neat)
        p = neat.Population(config)

        winner = p.run(self.manager,10000)


