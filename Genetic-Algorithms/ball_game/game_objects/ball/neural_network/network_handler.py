from pygame.math import Vector2 

from ._network import Network 


NETWORK_SIZE = (2, 4, 2) 

class NetworkHandler:

    def __init__(self, obstacles):
        self.network = Network(NETWORK_SIZE)

        self.obstacles = obstacles 

    def get_desired_vel(self):
        return Vector2((1, -10)) 
        X = self.preprocess(obstacle_distance, obstacle_height) 
        Y = self.network.feedforward(X) 
        return self.postprocess(Y) 

    def get_next_obstacle(self, pos):
        # indexing doesn't work on obstacles.
        # and i don''t wanna use extra space ..(don't ask why) 
        return min(
            filter(lambda obstacle: obstacle.rect.centerx > pos, self.obstacles), 
            key = lambda obstacle: obstacle.centerx
        )


    @staticmethod
    def preprocess(obstacle_distance, obstacle_height):
        pass 

    @staticmethod
    def postprocess(desired_vel):
        pass 