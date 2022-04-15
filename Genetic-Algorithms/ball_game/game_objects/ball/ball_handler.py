import pygame 
from pygame.sprite import Group


def get_factory():
    from ._ball_factory import BallFactory 
    return BallFactory() 

def get_collision_handler(*args):
    from ._collision_handler import CollisionHandler 
    return CollisionHandler(*args)  


class BallHandler:
    from my_constants import POPULATION 
    factory = get_factory() 
    
    def __init__(self):
        self.balls = Group() 
        self.collision_handler = get_collision_handler(self.balls) 

    def draw(self, window):
        self.balls.draw(window) 
    
    def update(self):
        self.collision_handler.update() 
        self.balls.update() 

        if len(self.balls) == 0:
            self.request_generation_update() 
    
    @staticmethod
    def request_generation_update():
        from my_constants import UPDATE_GENERATION_EVENT
        event = pygame.event.Event(UPDATE_GENERATION_EVENT) 

        is_posted = pygame.event.post(event) 
        assert(is_posted) 



    def spawn_balls(self):
        for i in range(self.POPULATION):
            self.balls.add(self.factory.make_ball()) 

