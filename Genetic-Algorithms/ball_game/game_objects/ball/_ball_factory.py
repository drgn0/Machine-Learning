import pygame 
import random 


from .__ball import Ball 
from neural_network.network_handler import NetworkHandler

class BallFactory:
    def get_random_balls(self, N):
        return pygame.sprite.Group([self.get_ball() for i in range(N)]) 
    
    def get_mutated_balls(self, balls):  # TODO:  is this function supposed to be here  ??
        balls = tuple(balls) 
        ball_scores = [(ball.score ** 2) / max(2, ball.network_handler.get_mean_of_sq_of_weights()) for ball in balls] 
        print('Best Score:', max([ball.score for ball in balls]) - 1)
        # print(ball_scores, '\n') 

        random_balls_count = len(balls) // 50 
        balls = random.choices(balls, ball_scores, k=len(balls)-random_balls_count) 

        return pygame.sprite.Group(
            [self.get_ball(ball.get_network()) for ball in balls], 
            [self.get_ball() for i in range(random_balls_count)]
        )


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
