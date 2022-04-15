# Data Provider. 
# all these None values will be updated by game_initialiser.py 

from my_constants import WINDOW_SIZE


# game = None  

ground = None
walls = None 
obstacle_handler = None 

obstacle_spawn_pos = None 


def get_score():
    return obstacle_handler.get_score() 

def get_obstacles():
    return obstacle_handler.get_obstacles() 

def get_ground():
    return ground 

def get_walls():
    return walls 
