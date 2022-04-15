import pygame 
from my_constants import * 

import GameData 

    
class GameInitialiser:
    def __init__(self, game):
        self.game = game 
        self.initialise() 
    
    def initialise(self):
        self.initialise_pygame() 
        
        self.game.generation = 0 
        self.set_game_objects() 
    
    def initialise_pygame(self):
        pygame.init() 
        pygame.display.set_caption("Ball Game") 

        self.game.window = pygame.display.set_mode(WINDOW_SIZE) 
        self.game.clock = pygame.time.Clock() 

    def set_game_objects(self):
        self.set_walls() 
        self.set_ground() 
        self.set_obstacle_handler() 
        self.set_ball_handler() 
    
    def set_walls(self):
        walls = get_walls() 
        self.game.walls = walls 
        GameData.walls = walls 
    
    def set_ground(self):
        ground = get_ground() 
        self.game.ground = ground 
        GameData.obstacle_spawn_pos = ground.rect.topright 
        GameData.ground = ground 
    
    def set_obstacle_handler(self):
        obstacle_handler = get_obstacle_handler() 
        self.game.obstacle_handler = obstacle_handler 
        GameData.obstacle_handler = obstacle_handler 
    
    def set_ball_handler(self):
        ball_handler = get_ball_handler() 
        self.game.ball_handler = ball_handler 



def get_ball_handler():
    from game_objects.ball.ball_handler import BallHandler 
    return BallHandler() 

def get_obstacle_handler(): 
    # ground is passed just to get initial spawning position of obstacles.
    # TODO:  Make it work without passing ground  ?
    from game_objects.obstacle.obstacle_handler import ObstacleHandler 
    return ObstacleHandler() 

def get_ground():
    from game_objects.ground.ground import Ground  

    return Ground() 
     
def get_walls():
    import game_objects.wall.walls as walls 
    return walls.get_walls() 

