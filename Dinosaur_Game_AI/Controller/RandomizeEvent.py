import random

class RandomizeEvent():
    """description of class"""

    def __init__(self, rate_chance, list_event, marge_event):
        self.rate_chance = rate_chance
        self.list_event = list_event
        self.marge_event = marge_event

    def __repr__(self):
        return "RandomizeEvent('{}', '{}', '{}')".format(self.rate_chance, self.list_event, self.marge_event)

    def wrapper_randomize(func): 
        def randomize_event(self, rate_chance, list_event, marge_event):
            if random.randrange(0, rate_chance) == 1 and len(list_event) <= 3:
                if len(list_event) == 0 or list_event[-1].x < marge_event:
                    func()
        return randomize_event

    @wrapper_randomize
    def randomize_cloud(self):
        if random.randrange(0, 120) == 2 and len(self.cloud_list) <= 3 :
            if len(self.cloud_list) == 0 or self.cloud_list[-1].x < config.WIN_WIDTH and len(self.cloud_list) > 0: 
                cloud_list.append(Cloud(self.cloud_list))

    @wrapper_randomize
    def randomize_obstacle(self):
        generate_random_obstacle = random.randrange(0,5)
        if generate_random_obstacle %2 == 0:
                obstacleList.append(Bird(base.vel))
                if self.game_mode == 1: [self.g.fitness + 1.5 for self.g in self.ge]