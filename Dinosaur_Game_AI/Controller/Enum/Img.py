from enum import Enum

import os 
import pygame as pg 

class Img(Enum):
    #Button design for normal game mode
    REGULAR_IMG = pg.image.load(os.path.join("Sprites","regular_btn.png"))
    
    #Button design for the AI mode of the game
    AI_IMG = pg.image.load(os.path.join("Sprites", "Ai.PNG"))
    
    #On click button design for normal game mode
    REGULAR_ONCLICK = pg.image.load(os.path.join("Sprites","regular_onclick.PNG"))

    #On click button design for Ai game mode
    AI_ONCLICK = pg.image.load(os.path.join("Sprites","Ai_onclick.PNG"))

    #Menu title design 
    TITLE_IMG = pg.image.load(os.path.join("Sprites","Title.PNG"))

    #
    BASE_IMG = pg.image.load(os.path.join("Sprites","Base_2.PNG"))

    #
    BIRD_IMG_1 = pg.image.load(os.path.join("Sprites","Bird_1.PNG"))

    #
    BIRD_IMG_2 = pg.image.load(os.path.join("Sprites","Bird_2.PNG"))

    #
    CLOUD_IMG = pg.image.load(os.path.join("Sprites","Cloud.PNG"))

    #
    STAY_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_1.PNG"))

    #
    CRAWL_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_5.PNG"))

    #
    DEAD_DINOSAUR_IMG = pg.image.load(os.path.join("Sprites","Dinosaur_4.PNG"))

    #
    RUN_DINOSAUR_IMG = [pg.image.load(os.path.join("Sprites","Dinosaur_2.PNG")), pg.image.load(os.path.join("Sprites","Dinosaur_3.PNG"))]
