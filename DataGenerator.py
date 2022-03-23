import numpy as np 
import random 

class Line:
    def __init__(self, w, b):
        # y = w1*x1 + w2x2 + ... wn*xn  +  b 
        self.w = w 
        self.b = b 
    
    def f(self, x) -> float:
        # f(x) = w1*x1 + w2x2 + ... wn*xn  +  b 
        return np.dot(self.w, x) + self.b 

    def generate(self, n = 500, standard_dev = 0.4):
        return np.array(
            self.generate_data_point(standard_dev) for i in range(n)
        )
        
    def generate_data_point(self, standard_dev: float):
        x = np.random.random((len(self.w)))
        x = (x - 0.5) * 5  #  x belongs to [-2.5, 2.5) now 

        y = self.f(x) 
        y = random.normalvariate(y, standard_dev)  # randomness 

        return x, y 
    
if __name__ == '__main__':
    pass 

    
