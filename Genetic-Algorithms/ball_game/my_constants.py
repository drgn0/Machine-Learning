from pygame import Vector2 


FPS = 60 
WINDOW_SIZE = Vector2(900, 550) 

POPULATION = 10 

# colors 
'''
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
''' 
BACKGROUND_COLOR = (255, 255, 255)
GROUND_COLOR = (0, 0, 0)
WALL_COLOR = (0, 0, 0) 
OBSTACLE_COLOR = (0, 0, 0) 

# events 
from pygame import USEREVENT
SPAWN_OBSTACLE_EVENT = USEREVENT + 1 
UPDATE_GENERATION_EVENT = USEREVENT + 2 
