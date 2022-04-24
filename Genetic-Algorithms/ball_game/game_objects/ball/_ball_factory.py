import pygame 
import random 


from .__ball import Ball 
from neural_network.network_handler import NetworkHandler

class BallFactory:
    def get_random_balls(self, N):
        return pygame.sprite.Group([self.get_ball() for i in range(N)]) 
    
    def get_mutated_balls(self, balls):
        balls = tuple(balls) 
        ball_scores = [ball.score for ball in balls] 

        balls = random.choices(balls, ball_scores, k=len(balls)) 
        
        return pygame.sprite.Group([
            self.get_ball(ball.get_network()) for ball in balls 
        ])


    def get_ball(self, network = None):
        ball = Ball() 

        self.initialise_rect(ball) 
        self.initialise_velocity(ball)
        self.initialise_network_handler(ball, network)  

        return ball 


    @staticmethod
    def initialise_rect(ball):
        # ball.image is already initialised.  ..Flyweight pattern
        ball.rect = ball.image.get_rect() 
        ball.rect.move_ip(BallFactory.get_initial_pos())  

    @staticmethod
    def get_initial_pos():
        return pygame.Vector2(
            random.randint(25, 400), 
            random.randint(25, 300)
        )

    @staticmethod
    def initialise_velocity(ball):
        INITIAL_VELOCITY_X = 2 
        ball.velocity = pygame.Vector2((INITIAL_VELOCITY_X, 0)) 

    @staticmethod
    def initialise_network_handler(ball, network):
        ball.network_handler = NetworkHandler(parent = ball, network = network) 
