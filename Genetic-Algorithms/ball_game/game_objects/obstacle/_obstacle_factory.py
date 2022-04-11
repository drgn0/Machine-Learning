from random import randint 
from pygame import Surface 

from .__obstacle import Obstacle


class ObstacleFactory:
    WIDTH = 20
    MIN_HEIGHT = 50 
    MAX_HEIGHT = 350 

    color = (0, 0, 1)  # TODO: Make it work
    
    @classmethod
    def set_initial_pos(cls, initial_pos):
        cls.INITIAL_POSITION = initial_pos 

    def get_random_height(self):
        return randint(self.MIN_HEIGHT, self.MAX_HEIGHT) 
    
    def make_obstacle(self):
        obstacle = Obstacle() 

        obstacle.height = self.get_random_height() 
        self.initialise_sprite(obstacle) 

        return obstacle 
       
    def initialise_sprite(self, obstacle):
        obstacle.image = Surface((self.WIDTH, obstacle.height)) 
        obstacle.image.fill(self.color) 
        obstacle.rect = obstacle.image.get_rect() 
        obstacle.rect.bottomleft = self.INITIAL_POSITION
    
