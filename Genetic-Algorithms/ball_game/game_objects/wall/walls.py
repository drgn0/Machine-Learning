from pygame.sprite import Sprite, Group 
from pygame import Surface, Rect 

from my_constants import WALL_COLOR


WALL_THICKNESS = 20 

def get_walls():
    from GameData import WINDOW_SIZE as screen_size 
    
    left_wall = Wall(Surface(
        (WALL_THICKNESS, screen_size.y)
    ))

    top_wall = Wall(Surface(
        (screen_size.x, WALL_THICKNESS)
    ))

    right_wall = Wall(Surface(
        (WALL_THICKNESS, screen_size.y) 
    ))
    right_wall.rect.move_ip(screen_size.x - WALL_THICKNESS, 0) 

    return Group(left_wall, right_wall, top_wall) 


class Wall(Sprite):
    def __init__(self, surface):
        super().__init__() 
        
        self.image = surface.convert_alpha()
        self.image.fill(WALL_COLOR) 
        self.rect = self.image.get_rect() 