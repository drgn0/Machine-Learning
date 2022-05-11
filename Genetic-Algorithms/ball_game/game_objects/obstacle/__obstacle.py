from pygame.sprite import Sprite  



class Obstacle(Sprite):
    def __init__(self):
        super().__init__() 

        self.speed = 3

    def update(self):
        self.rect.move_ip(-self.speed, 0) 