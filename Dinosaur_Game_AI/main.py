import os 
from Controller.Manager import Manager
from Controller.Encryption import Encryption

if __name__ == "__main__":
    game_loop = Manager()
    #Encryption.generate_key()
    game_loop.manageGame()


