from pygame.math import Vector2 

from ._network import Network 


import GameData 

def get_network_mutator():
    from ._network_mutator import NetworkMutator 
    return NetworkMutator() 

class NetworkHandler:
    from GameData import WINDOW_SIZE as screen_size 
    from my_constants import NETWORK_SIZE
    # obstacles = None 
    network_mutator = get_network_mutator() 

    MIN_JUMP = 7
    MAX_JUMP = 14 
    X_MULTIPLIER = 5
    
    def __init__(self, parent, network = None):
        if network is None:
            self.network = Network(self.NETWORK_SIZE) 
        else:
            self.network = self.network_mutator.mutate_network(network) 
            
        self.parent = parent 

    def get_desired_vel(self):
        obstacle_distance, obstacle_height = self.get_obstacle_data() 
        pos = self.parent.rect.centerx 

        X = self.preprocess(pos, obstacle_distance, obstacle_height) 
        Y = self.network.feedforward(X) 
        # print(X, '\n', Y)
        return self.postprocess(Y) 

    def get_obstacle_data(self):
        # returns obstacle_distance, obstacle_height 
        ball_pos = self.parent.rect.centerx 
        obstacle = self.get_next_obstacle(ball_pos) 
        
        if obstacle is None:  
            return self.screen_size.x, 0   
            
        return (
            obstacle.rect.centerx - ball_pos, 
            obstacle.rect.height 
        )

    def get_next_obstacle(self, pos):
        # indexing doesn't work on obstacles.
        # and i don''t wanna use extra space ..(don't ask why) 
        obstacles_ahead = filter(lambda obstacle: obstacle.rect.centerx > pos, GameData.get_obstacles())
        return min(
            obstacles_ahead, 
            key = lambda obstacle: obstacle.rect.centerx,
            default = None  # no obstacle ahead 
        )



    def preprocess(self, pos, obstacle_distance, obstacle_height):
        x = pos / self.screen_size.x 
        y = obstacle_distance / self.screen_size.x
        z = obstacle_height ** 2 / self.screen_size.y ** 2 

        return (
            5 * x, 
            5 * y, 
            5 * z 
        )
    

    def postprocess(self, desired_vel):
        result = Vector2() 
        result.x = (2 * desired_vel[0] - 1) * self.X_MULTIPLIER
        result.y = self.MIN_JUMP + desired_vel[1] * (self.MAX_JUMP - self.MIN_JUMP) 
        result.y *= -1 

        # print(result)
        return result 


    def get_mean_of_sq_of_weights(self):
        return sum( self.mean_of_sq_of_2d_array(layer) for layer in self.network.weights ) / len(self.network.weights)
    
    @staticmethod
    def mean_of_sq_of_2d_array(matrix):
        return sum( sum(x * x for x in row) / len(row) for row in matrix ) / len(matrix)
