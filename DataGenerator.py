import numpy as np 
import random 


class Line:
    def __init__(self, w, b):
        # y = w1*x1 + w2x2 + ... wn*xn  +  b 
        try:
            w[0]  
        except Exception:
            raise TypeError("w should be iterable")

        self.w = w 
        self.b = b 

        # the 'range' of data. 
        # y_max - y_min 
        self.spread = abs(self.f(2) - self.f(-2))  # considering  -2 <= x < 2 
    
    def f(self, x) -> float:
        # f(x) = w1*x1 + w2x2 + ... wn*xn  +  b 
        return np.dot(self.w, x) + self.b 

    def generate(self, n = 200, err = 0.2):
        data = np.empty(n, tuple) 
        generator = (self.generate_data_point(err) for i in range(n))  

        for i, val in enumerate(generator):
            data[i] = val 
        
        return data 
        
        
    def generate_data_point(self, err: float):
        '''returns a single data point'''
        x = np.random.random((len(self.w)))
        x = (x - 0.5) * 4  #  x belongs to [-2, 2) now 

        y = self.f(x) 
        ## y = random.normalvariate(y, standard_dev)  # randomness 
        y += (random.random() - random.random()) * self.spread * err

        return x, y 
    
if __name__ == '__main__':
    line = Line((2,), 5)
    data = line.generate() 

    print(data[:5]) 

    
