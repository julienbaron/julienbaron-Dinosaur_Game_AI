import pygame as pg 


class KeyManager():
    @staticmethod
    def keyPressed(event, dino):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP or pg.K_SPACE and dino.get_jump == False:
                dino.is_jump(True)
            elif event.key == pg.K_DOWN:
                dino.is_crawling(True)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                if dino.is_jump() == 10 : 
                    dino.is_jump(False)
            elif event.key == pg.K_DOWN:
                dino.is_crawling(False)
           
