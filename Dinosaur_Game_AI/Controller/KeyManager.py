import pygame as pg 


class KeyManager(object):

    @staticmethod
    def keyPressed(event, dino):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP or pg.K_SPACE and dino.get_jump == False:
                dino.setIsJump(True)
                return True 
        elif event.type == pg.KEYUP:
             if event.key == pg.K_UP or pg.K_SPACE:
                if dino.get_jump() == 10 : 
                    dino.setIsJump(False)
                    return False
           
