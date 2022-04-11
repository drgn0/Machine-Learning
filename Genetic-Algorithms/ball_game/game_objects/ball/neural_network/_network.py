import numpy as np 

class Network:
    def __init__(self, sizes):
        self.sizes = sizes 
        self.weights = [np.random.standard_normal((x, y)) for x, y in zip(sizes[1:], sizes[:-1])] 
        self.biases = [np.random.standard_normal((x, 1)) for x in sizes[1:]] 
    
    def predict(self, x):
        assert(x.shape == (self.sizes[0], 1)) 

        a = x
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.matmul(w, a) + b) 

        return a 


    @staticmethod
    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z)) 
    