import numpy as np 


def default_data(func):
    # decorator to have default data 
    def modified_func(self, data = None):
        if data is None:
            data = self.training_data 
        
        return func(self, data) 
    
    return modified_func 



class Regression:
    def __init__(self, data: np.ndarray[ tuple[np.ndarray, float] ]):
        # data: Array[ (x, y) ]
        self.training_data = data  

        self.w = np.random.random(data[0].shape) 
        self.b = np.random.rand() + 1 

        # self.train() 
    

    def train(self, epoches = 10, learning_rate = 0.1):
        for e in range(epoches):
            self.shuffle_training_data() 
            self.gradient_descent() 

    def shuffle_training_data(self):
        np.random.shuffle(self.training_data) 

    def predict(self, x):
        return np.dot(self.w, x) + self.b 

    @default_data 
    def gradient_descent(self, data):
        # on self.training_data 
        error = self.mean_sq_error(self.training_data)
        self.update(self, error)  
        # TODO: Make it work. 
        
    
    @default_data
    def mean_sq_error(self, data):
        return sum(map(self.deviation_sq, data)) / len(data) 

    @default_data
    def delta_mean_sq_error(self, data):
        pass 

    def del_w(self, data_point):
        x, y = data_point 
        pass 



    def deviation(self, data_point: tuple[np.ndarray, float]) -> float:
        x, y = data_point 
        return abs(self.predict(x) - y) 

    def deviation_sq(self, data_point: tuple[np.ndarray, float]) -> float:
        x, y = data_point 
        return (self.predict(x) - y) ** 2 
    
    