import pygame 
import random 


from .__ball import Ball 
from .neural_network.network_handler import NetworkHandler

class BallFactory:
    def make_ball(self):
        ball = Ball() 

        self.initialise_sprite(ball) 
        self.initialise_velocity(ball)
        self.initialise_network_handler(ball)  

        return ball 


    @staticmethod
    def initialise_sprite(ball):
        ball.image = pygame.image.load("Assets/ball.png") 
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
    def initialise_network_handler(ball):
        ball.network_handler = NetworkHandler(ball.NETWORK_SIZE) 
