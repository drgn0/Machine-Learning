import pygame
from sys import exit 


from my_constants import *


class Game:
    def __init__(self): 
        from game_initialiser import GameInitialiser 
        GameInitialiser(self)
        self.all_sprite_groups = [self.ball_handler, self.obstacle_handler, self.walls, self.ground] 
        
    def game_loop(self):
        while True:
            self.handle_events() 
            self.simulate_frame() 
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()
            elif event.type == SPAWN_OBSTACLE_EVENT:
                self.obstacle_handler.spawn_obstacle() 
            elif event.type == UPDATE_GENERATION_EVENT:
                self.update_generation() 
    
    def update_generation(self):
        self.generation += 1 
        self.obstacle_handler.reset() 
        self.ball_handler.spawn_balls() 

    def simulate_frame(self):
        self.update_stuff() 
        self.draw_stuff() 

        pygame.display.update()  # TODO:  optimise 
        self.clock.tick(FPS) 
    
    def update_stuff(self):
        self.ball_handler.update() 
        self.obstacle_handler.update() 
    
    def draw_stuff(self):
        self.window.fill(BACKGROUND_COLOR) 

        for group in self.all_sprite_groups:
            group.draw(self.window)
  

if __name__ == '__main__':
    game = Game() 
    game.game_loop() 

