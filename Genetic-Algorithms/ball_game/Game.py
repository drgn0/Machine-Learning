import pygame, sys  # standard libraries


from my_constants import WHITE  

pygame.init() 
pygame.display.set_caption("Ball Game") 



WINDOW_SIZE = pygame.Vector2((800, 500)) 
FPS = 60 


def get_ball_handler(*args):
    from game_objects.ball.ball_handler import BallHandler 
    return BallHandler(*args) 

def get_obstacle_handler(ground): # TODO:  Make it work without passing ground  
    from game_objects.obstacle.obstacle_handler import ObstacleHandler 
    return ObstacleHandler(ground) 

def get_ground():
    from game_objects.ground.ground import Ground  

    return Ground(WINDOW_SIZE) 
     


class Game:
    def __init__(self):       
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock() 

        self.ground = get_ground() 
        self.walls = pygame.sprite.Group([]) 

        self.obstacle_handler = get_obstacle_handler(self.ground)  # ground is used to set spawn position for obstacles 
        self.ball_handler = get_ball_handler(self.ground, self.obstacle_handler.get_obstacles(), self.walls)  

    def game_loop(self):
        while True:
            self.handle_events() 
            self.simulate_frame() 
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
    
    def simulate_frame(self):
        self.update_stuff() 
        self.draw_stuff() 

        pygame.display.update()  # TODO:  optimise 
        self.clock.tick(FPS) 
    
    def update_stuff(self):
        self.ball_handler.update() 
        self.obstacle_handler.update() 
    
    def draw_stuff(self):
        self.window.fill(WHITE) 
        
        self.ground.draw(self.window) 
        self.walls.draw(self.window) 
        self.ball_handler.draw(self.window) 
        self.obstacle_handler.draw(self.window) 
    
if __name__ == '__main__':
    game = Game() 
    game.game_loop() 