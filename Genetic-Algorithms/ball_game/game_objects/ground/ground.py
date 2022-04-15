import pygame 

from my_constants import GROUND_COLOR

class Ground(pygame.sprite.Sprite):
    HEIGHT = 35 
    def __init__(self):
        super().__init__() 

        from GameData import WINDOW_SIZE
        self.image = pygame.Surface((WINDOW_SIZE.x, self.HEIGHT)).convert_alpha()
        self.image.fill(GROUND_COLOR) 
        
        self.rect = self.image.get_rect() 

        self.rect.move_ip(0, WINDOW_SIZE.y - self.HEIGHT) 
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
