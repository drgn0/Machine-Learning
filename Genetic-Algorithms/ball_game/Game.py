import pygame, sys  # standard libraries


from my_constants import * 

pygame.init() 
pygame.display.set_caption("Ball Game") 



WINDOW_SIZE = pygame.Vector2((800, 500)) 
ALLOWED_SCREEN = pygame.Rect((20, 20), WINDOW_SIZE - (40, 40))  # TODO: Better Approach  ? 
FPS = 60 

POPULATION = 5 


GROUND_HEIGHT = 35 

def get_ball_handler(*args):
    from game_objects.ball.ball_handler import BallHandler 
    return BallHandler(*args) 

def get_obstacle_handler(ground): # TODO:  Make it work without passing ground  ?
    from game_objects.obstacle.obstacle_handler import ObstacleHandler 
    return ObstacleHandler(ground) 

def get_ground():
    from game_objects.ground.ground import Ground  

    ground = Ground(WINDOW_SIZE) 
    return ground 


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
    
'''
def update_balls():
    check_ball_death() 
    handle_ground_ball_collisions()  # makes ball jump. if collided with ground
    balls.update()  # their position and stuff.. 
    balls.draw(window)  

def check_ball_death():
    check_collision_with_obstacles() 
    kill_out_of_bound_balls() 

def check_collision_with_obstacles():
    for obstacle in obstacles:
        pygame.sprite.spritecollide(obstacle, balls, dokill = True) 
    
def kill_out_of_bound_balls():
    for ball in balls:
        if is_out_of_bound(ball):
            kill_ball(ball) 

def is_out_of_bound(ball):
    return not ALLOWED_SCREEN.contains(ball.rect) 

def kill_ball(ball):
    balls.remove(ball)  

def handle_ground_ball_collisions():
    for ball in pygame.sprite.spritecollide(ground, balls, dokill = False):
        ball_jump(ball) 

def ball_jump(ball):
    obstacle_x, obstacle_height = get_next_obstacle(ball.rect.centerx) 
    obstacle_distance = obstacle_x - ball.rect.centerx 

    ball.jump(obstacle_distance, obstacle_height) 

def get_next_obstacle(pos_x):
    # next obstacle on right side of given position 
    return WINDOW_SIZE.x, 0

''' 

if __name__ == '__main__':
    game = Game() 
    game.game_loop() 