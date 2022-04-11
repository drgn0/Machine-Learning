import pygame 

class Ground(pygame.sprite.Sprite):
    HEIGHT = 35 
    def __init__(self, screen_size, *args):
        super().__init__(*args) 

        color = (0.7, 0.2, 0.3) 
        self.image = pygame.Surface((screen_size.x, self.HEIGHT)) 
        self.image.fill(color) 
        
        self.rect = self.image.get_rect() 

        self.rect.move_ip(0, screen_size.y - self.HEIGHT) 
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

    def get_height(self):
        return self.HEIGHT