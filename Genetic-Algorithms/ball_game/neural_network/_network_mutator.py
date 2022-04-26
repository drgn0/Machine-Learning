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
            self.mutate_arr(network.weights), 
            self.mutate_arr(network.biases) 
        )

        # print(type(network.weights[0]), type(new_network.weights[0]))
        assert(not (network.weights[0] is new_network.weights[0]))
        return new_network

    def mutate_arr(self, arr):
        # TODO:  !!  REWORK  !!
        if isinstance(arr, list):
            return [self.mutate_arr(row) for row in arr] 
        
        if not isinstance(arr, np.ndarray):
            # arr is actually a float 
            assert(isinstance(arr, np.float64))
            return self.mutate_float(arr) 

        new_arr = arr.copy()
        for i, x in enumerate(new_arr):
            new_arr[i] = self.mutate_arr(x) 

        if not is_equal(arr, new_arr):
            pass 
            # print(*zip(arr, new_arr))
            # print(arr, '\n', new_arr, '\n\n\n') 

        return new_arr 
    
    
    def mutate_float(self, x):
        if random.random() < self.MUTATION_CHANCES:
            return x * (1 + self.MUTATION_MAGNITUDE * (random.random() - random.random())) 
        
        return x 
    