import pygame 
from pygame.sprite import Group 

def get_factory():
    from ._obstacle_factory import ObstacleFactory
    return ObstacleFactory() 


class ObstacleHandler:
    factory = get_factory() 
    from my_constants import OBSTACLE_SPAWN_TIME 
    def __init__(self):
        self.obstacles = Group([])  #  !!  DO NOT CHANGE THIS POINTER  !!  IT'S USED BY OTHER SCRIPTS. 
        self.score = 1  # to make sure balls doesn't have zero score.. i.e, zero chances of getting selected
        
    def get_obstacles(self):
        return self.obstacles 

    def get_score(self):
        return self.score 
        
    def reset(self):
        # called at start of generation 
        self.obstacles.empty() 
        self.score = 1 
        
        from my_constants import SPAWN_OBSTACLE_EVENT
        pygame.time.set_timer(SPAWN_OBSTACLE_EVENT, self.OBSTACLE_SPAWN_TIME) 
        self.spawn_obstacle() 

    def spawn_obstacle(self):
        # called in game.py in handle_events
        obstacle = self.factory.make_obstacle() 
        self.obstacles.add(obstacle)
    
    def despawn_out_of_screen_obstacles(self):
        for obstacle in self.obstacles:
            if obstacle.rect.right < 0:
                self.obstacles.remove(obstacle) 
                self.score += 1

    def update(self):
        self.obstacles.update() 
        self.despawn_out_of_screen_obstacles() 
    
    def draw(self, window):
        self.obstacles.draw(window) 

