import os 
from Controller.Manager import Manager

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    print(local_dir)
    #config_path = os.path.join(local_dir, "test")
    game_loop = Manager()
    game_loop.manageGame()


