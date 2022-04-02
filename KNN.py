from numpy import argsort

class KNN:
    def __init__(self, data, K = 5):
        self.data_x, self.data_y = data 

        self.K = K 
        
    def predict(self, X):
        distances = [sum(x*x) for x in (self.data_x - X)]  # TODO:  optimise  ?
        
        neibours_indices = argsort(distances)[:self.K] 
        return self.mean([self.data_y[i] for i in neibours_indices]) 
        
        
    @staticmethod
    def mean(data):
        return sum(data) / len(data)  

    