import random 

class DataHandler:
    def __init__(self):
        self._already_tested = False 
        self._make_cubic_data()
    
    def _make_cubic_data(self, n = 200):
        a = (random.random() - 0.5)
        b = (random.random() - 0.5) * 4
        c = (random.random() - 0.5) * 10
        d = (random.random() - 0.5) * 50 

        data_x = [] 
        data_y = [] 

        bias = 8
        standard_deviation = 0.15  # percent  ?

        for _i in range(n):
            x = (random.random() - 0.5) * 10
            y = a*x*x*x + b*x*x + c*x + d  +  (random.random() - random.random()) * bias 

            y += y * standard_deviation * (random.random() - random.random()) 

            data_x.append((x)) 
            data_y.append((y)) 
        
        self.train_data_x = data_x[:4 * n // 5]
        self.train_data_y = data_y[:4 * n // 5] 

        self._test_data_x = data_x[4 * n // 5:]
        self._test_data_y = data_y[4 * n // 5:] 
        

    def get_training_data(self):
        return self.train_data_x, self.train_data_y 
    
    def mean_sq_error(self, predict, data_x = None, data_y = None):
        if data_x is None:
            data_x = self.train_data_x
        if data_y is None:
            data_y = self.trian_data_y 
        
        return sum( (predict(x) - y) ** 2 for x, y in zip(data_x, data_y) ) / len(data_x) 
        
    def test(self, func):
        if self._already_tested:
            raise ValueError("Can only test once.") 
        
        self._already_tested = True 
        return self.mean_sq_error(func, self._test_data_x, self._test_data_y) 

    
