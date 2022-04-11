from pygame.sprite import Group


def get_factory():
    from ._ball_factory import BallFactory 
    return BallFactory() 

def get_collision_handler(*args):
    from ._collision_handler import CollisionHandler 
    return CollisionHandler(*args)  


class BallHandler:
    POPULATION = 5 
    factory = get_factory()  # TODO: Does it work  ? 
    
    def __init__(self, ground, obstacles, walls):
        self.balls = Group() 
        self.spawn_balls() 

        self.collision_handler = get_collision_handler(self.balls, ground, obstacles, walls) 
    
    def draw(self, window):
        self.balls.draw(window) 
    
    def update(self):
        self.collision_handler.update() 
        self.balls.update() 

    def spawn_balls(self):
        for i in range(self.POPULATION):
            self.balls.add(self.factory.make_ball()) 

