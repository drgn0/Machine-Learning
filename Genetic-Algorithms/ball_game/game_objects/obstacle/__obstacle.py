from pygame.sprite import Sprite  

from my_constants import OBSTACLE_SPEED 

class Obstacle(Sprite):
    def __init__(self):
        super().__init__() 

        self.speed = OBSTACLE_SPEED

    def update(self):
        self.rect.move_ip(-self.speed, 0) 