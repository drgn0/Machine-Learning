class KNN:
    def __init__(self):
        self.make_data() 
        self.K = 4 

    def make_data(self):
        from DataHandler import DataHandler 

        self.data_handler = DataHandler() 
        self.train_x, self.train_y = self.data_handler.get_training_data() 
    
    def plot(self):
        from matplotlib import pyplot as plt 

        plt.scatter(self.train_x, self.train_y)
        plt.show() 
    
    def give_neibours(self, X):
        neighbours_indices = sorted(range(len(self.train_x)), 
            key = lambda i: abs(X - self.train_x[i])
        )
        return [self.train_y[i] for i in neighbours_indices[:self.K]] 

    def give_predictor(self):
        def predict(X):
            return KNN.mean(self.give_neibours(X)) 
        
        return predict 
    
    def test(self):
        err = self.data_handler.test(self.give_predictor()) 
        print("Mean Sq. Error:", err) 
    
    @staticmethod
    def mean(arr):
        return sum(arr) / len(arr) 

def main():
    knn = KNN() 

    knn.test() 
    knn.plot() 

main()
