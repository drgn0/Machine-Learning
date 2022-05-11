import random 

from ._network import Network 

import numpy as np 

def is_equal(p, q):
    # wait.. doesn't.. p == q does the exact same thing  ?  :v 
    if isinstance(p, np.ndarray):
        return all(is_equal(x, y) for x, y in zip(p, q)) 
    
    # assert(isinstance(p, np.float64))
    return p == q 

class NetworkMutator:
    from my_constants import MUTATION_CHANCES, MUTATION_MAGNITUDE 

    def mutate_network(self, network):
        new_network = Network(
            network.sizes, 
            self.mutate_list(network.weights), 
            self.mutate_list(network.biases) 
        )

        # print(type(network.weights[0]), type(new_network.weights[0]))
        assert(not (network.weights[0] is new_network.weights[0]))
        return new_network

    def mutate_list(self, list_):
        result = [self.mutate_arr(row) for row in list_] 

        # print("Mutating") 
        # print(list_[0]) 
        # print('\n', result[0]) 

        return result

    def mutate_arr(self, arr):
        assert(len(arr.shape) == 2) 
        new_arr = arr.copy() 
        for i in range(new_arr.shape[0]):
            for j in range(new_arr.shape[1]):
                new_arr[i][j] = self.mutate_float(new_arr[i][j]) 
        return new_arr 
        
    def mutate_float(self, x):
        if random.random() < self.MUTATION_CHANCES:
            return x * (1 + self.MUTATION_MAGNITUDE * (random.random() - random.random())) 
        
        return x 
    