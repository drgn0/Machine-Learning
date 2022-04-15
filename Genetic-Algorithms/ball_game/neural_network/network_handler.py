from pygame.math import Vector2 

from ._network import Network 


NETWORK_SIZE = (2, 4, 2) 

class NetworkHandler:
    from GameData import WINDOW_SIZE as screen_size 
    obstacles = None 

    MIN_JUMP = 7
    MAX_JUMP = 14 
    X_MULTIPLIER = 4
    
    def __init__(self, parent):
        self.network = Network(NETWORK_SIZE)
        self.parent = parent 

    def get_desired_vel(self):
        obstacle_distance, obstacle_height = self.get_obstacle_data() 

        X = self.preprocess(obstacle_distance, obstacle_height) 
        Y = self.network.feedforward(X) 
        # print(X, Y)
        return self.postprocess(Y) 

    def get_obstacle_data(self):
        pos = self.parent.rect.centerx 
        try:
            obstacle = self.get_next_obstacle(pos) 
        except Exception:
            return self.screen_size 
            
        obstacle_distance = obstacle.rect.centerx - pos 
        obstacle_height = obstacle.rect.height 
        
        return obstacle_distance, obstacle_height

    def get_next_obstacle(self, pos):
        # indexing doesn't work on obstacles.
        # and i don''t wanna use extra space ..(don't ask why) 
        obstacles_ahead = filter(lambda obstacle: obstacle.rect.centerx > pos, self.obstacles)
        return min(
            obstacles_ahead, 
            key = lambda obstacle: obstacle.rect.centerx
        )



    def preprocess(self, obstacle_distance, obstacle_height):
        return (
            5 * obstacle_distance / self.screen_size.x, 
            5 * obstacle_height / self.screen_size.y
        )
    

    def postprocess(self, desired_vel):
        result = Vector2() 
        result.x = (2 * desired_vel[0] - 1) * self.X_MULTIPLIER
        result.y = self.MIN_JUMP + desired_vel[1] * (self.MAX_JUMP - self.MIN_JUMP) 
        result.y *= -1 

        # print(result)
        return result 