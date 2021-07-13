import os 
from Controller import Controller
def run(config_path_neat):
    Controller.Controller()

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "test")
