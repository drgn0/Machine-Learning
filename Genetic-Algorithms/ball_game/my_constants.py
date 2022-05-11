from pygame import Vector2 


FPS = 60 
WINDOW_SIZE = Vector2(900, 550) 

NETWORK_SIZE = (3, 5, 2) 
POPULATION = 1500
# NO_OF_VISIBLE_BALLS = 50

MUTATION_CHANCES = 0.2
MUTATION_MAGNITUDE = 1


if False:
    from random import randint 
    def get_random_color():  # please don't judge me.  :'v
        return tuple(randint(0, 255) for i in range(3))

# colors 
BACKGROUND_COLOR = (40, 200, 80)
GROUND_COLOR = (50, 20, 60)
WALL_COLOR = (60, 25, 40) 
OBSTACLE_COLOR = (80, 30, 50)

if False:
    print(f"{BACKGROUND_COLOR=}")
    print(f"{GROUND_COLOR=}")
    print(f"{WALL_COLOR=}")
    print(f"{OBSTACLE_COLOR=}")


# events 
from pygame import USEREVENT
SPAWN_OBSTACLE_EVENT = USEREVENT + 1 
UPDATE_GENERATION_EVENT = USEREVENT + 2 
