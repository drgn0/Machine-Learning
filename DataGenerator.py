import numpy as np 
import random 


class Line:
    def __init__(self, w, b):
        # y = w1*x1 + w2x2 + ... wn*xn  +  b 
        assert(w)  # algorithm kindaa fails here.  ## TODO: make it work. 
        assert(self.is_iterable(w)) 

        self.w = w 
        self.b = b 

        # the 'range' of data. 
        # y_max - y_min 
        self.spread = abs(self.f([2] * len(w)) - self.f([-2] * len(w)))  # TODO: fix it. it's wrong.
    
    def f(self, x) -> float:
        # f(x) = w1*x1 + w2x2 + ... wn*xn  +  b 
        assert(self.is_iterable(x)) 
        return np.dot(self.w, x) + self.b 
        
    def generate(self, n = 200, noise = 0.2):
        generator = (self.generate_data_point(noise) for i in range(n))  
        # can't convert generator to ndarray directly
        data_x = np.empty((n, len(self.w))) 
        data_y = np.empty(n, dtype=float)

        for i, val in enumerate(generator):
            data_x[i], data_y[i] = val 
        
        return data_x, data_y 
        
        
    def generate_data_point(self, noise: float):
        '''returns a single data point'''
        x = np.random.random((len(self.w)))
        x = (x - 0.5) * 4  #  x belongs to [-2, 2) now   # TODO:  something better  ? 

        y = self.f(x) 
        y += (random.random() - random.random()) * self.spread * noise

        # print(f"f({x}) = {y}")
        return x, y 
    
    @staticmethod
    def is_iterable(arr):
        # TODO: Find better approach  ? 
        try:
            # arr[[0]  # raises exception when arr is empty. 
            arr[:1] 
            return True 
        except Exception:
            return False 
    

if __name__ == '__main__':
    line = Line((2,), 5)
    data_x, data_y = line.generate() 
