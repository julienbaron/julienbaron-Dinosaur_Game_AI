import os 
from Controller.Manager import Manager
from Controller.MenuManager import MenuManager
#from Controller.Encryption import Encryption

if __name__ == "__main__":
    game_loop = Manager()
    menu_loop = MenuManager()
    menu_loop.menu_view()
    #Encryption.generate_key()
    #game_loop.manageGame()


