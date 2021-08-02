from enum import Enum

import os 
import pygame as pg 

class Img(Enum):

    REGULAR_IMG = pg.image.load(os.path.join("Sprites","regular_btn.png"))
    AI_IMG = pg.image.load(os.path.join("Sprites", "Ai.PNG"))
    REGULAR_ONCLICK = pg.image.load(os.path.join("Sprites","regular_onclick.PNG"))
    AI_ONCLICK = pg.image.load(os.path.join("Sprites","Ai_onclick.PNG"))
    TITLE_IMG = pg.image.load(os.path.join("Sprites","Title.PNG"))


