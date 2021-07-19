import pygame as pg 


class KeyManager():
    @staticmethod
    def keyPressed(event, dino):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP or pg.K_SPACE and dino.get_jump == False:
                dino.setIsJump(True)
            elif event.key == pg.K_DOWN:
                dino.setIsCrawling(True)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                if dino.get_jump() == 10 : 
                    dino.setIsJump(False)
            elif event.key == pg.K_DOWN:
                dino.setIsCrawling(False)
           
