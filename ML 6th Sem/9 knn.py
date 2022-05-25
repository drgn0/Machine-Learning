from numpy import argsort

class KNN:
    def __init__(self, data, K = 5):
        self.data_x, self.data_y = data 

        self.K = K 
        
    def predict(self, X):
        distances = [sum(x*x) for x in (self.data_x - X)] 
        
        neibours_indices = argsort(distances)[:self.K] 
        return self.mode([self.data_y[i] for i in neibours_indices]) 
        
        
    @staticmethod
    def mode(data):
        return max(data, key = data.count)  


def get_train_test_data(split_ratio = 0.8): 
    from pandas import read_csv    
    data = read_csv("datasets/iris.csv").sample(frac = 1)  
    
    split_point = int(split_ratio * len(data)) 
    return split_data(data[:split_point]), split_data(data[split_point:]) 

def split_data(data):
    return data.iloc[:, :-1].values, data.iloc[:, -1].values


PRINT_ALL_PREDICTIONS = True 

def test(model, test_x, test_y):
    correct_guesses = 0 
    for x, y in zip(test_x, test_y):
        predicted = model.predict(x) 
        if y == predicted:
            correct_guesses += 1 

        if PRINT_ALL_PREDICTIONS:
            print("data point:", x) 
            print(f'Actual Value = {y}  Predicted Value = {predicted}')

    print(f"\nTotal Correct Guesses: {correct_guesses}/{len(test_y)}")

training_data, test_data = get_train_test_data() 
knn = KNN(training_data) 

test(knn, *test_data) 