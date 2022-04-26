import pygame 
from pygame.sprite import Group


def get_factory():
    from ._ball_factory import BallFactory 
    return BallFactory() 

def get_collision_handler(parent):
    from ._collision_handler import CollisionHandler 
    return CollisionHandler(parent)  


class BallHandler:
    from my_constants import POPULATION 
    # from my_constants import NO_OF_VISIBLE_BALLS 

    factory = get_factory() 
    
    def __init__(self):
        self.all_balls = Group() 
        self.alive_balls = Group() 
        self.visible_balls = Group() 

        self.collision_handler = get_collision_handler(parent = self) 

    def get_alive_balls(self):
        return self.alive_balls 

    def draw(self, window):
        self.visible_balls.draw(window) 
    
    def update(self):
        self.collision_handler.update() 
        self.visible_balls = self.get_visible_balls() 
        self.alive_balls.update() 

        if len(self.alive_balls) == 0:
            self.request_generation_update() 
    
    def get_visible_balls(self):
        return self.alive_balls
        return Group(sorted(self.alive_balls, key = lambda ball: ball.score, reverse=True)[:self.NO_OF_VISIBLE_BALLS])

    @staticmethod
    def request_generation_update():
        from my_constants import UPDATE_GENERATION_EVENT
        event = pygame.event.Event(UPDATE_GENERATION_EVENT) 

        is_posted = pygame.event.post(event) 
        assert(is_posted) 


    def spawn_balls(self):
        ball_spawner = self.get_ball_spawner() 
        self.all_balls = ball_spawner() 

        assert(len(self.alive_balls) == 0) 
        self.alive_balls.add(self.all_balls) 
    
    def get_ball_spawner(self):
        if len(self.all_balls) == 0:  # first generation 
            return self.get_random_balls 
        
        return self.get_mutated_balls 

    def get_random_balls(self):
        return self.factory.get_random_balls(N = self.POPULATION) 

    def get_mutated_balls(self):
        return self.factory.get_mutated_balls(self.all_balls) 
