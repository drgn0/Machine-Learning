from random import randint 
from pygame import Surface 

from .__obstacle import Obstacle

from my_constants import OBSTACLE_COLOR


##  TODO:  Delete This File.  :v 
# Add these functionalities in Obstacle class. 


class ObstacleFactory:
    from GameData import obstacle_spawn_pos as INITIAL_POSITION 

    WIDTH = 20
    MIN_HEIGHT = 50 
    MAX_HEIGHT = 350 

    def get_random_height(self):
        return randint(self.MIN_HEIGHT, self.MAX_HEIGHT) 
    
    def make_obstacle(self):
        obstacle = Obstacle() 

        obstacle.height = self.get_random_height() 
        self.initialise_sprite(obstacle) 

        return obstacle 
       
    def initialise_sprite(self, obstacle):
        obstacle.image = Surface((self.WIDTH, obstacle.height)).convert_alpha()
        obstacle.image.fill(OBSTACLE_COLOR) 
        obstacle.rect = obstacle.image.get_rect() 
        obstacle.rect.bottomleft = self.INITIAL_POSITION
    
