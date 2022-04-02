# import matplotlib.pyplot as plt 
from numpy import array 

import DataGenerator
from KNN import KNN 



def main():
    train_data, test_data = get_data() 
    knn = KNN(train_data) 

    print('Mean Sq Error:', test(knn, test_data))

    # TODO: plot stuff and VERIFY that it's working.  




def get_data():
    line = DataGenerator.Line((2, 4, 3), 5)  # f = 2x + 4y + 3z + 5 

    data_x, data_y = line.generate(50)
    # data_x, data_y = zip(*data) 
    train_data_x, test_data_x = split_data(data_x)
    train_data_y, test_data_y = split_data(data_y)  

    return (train_data_x, train_data_y), (test_data_x, test_data_y)

def split_data(data):
    # 80% training data.  20% test data.  
    return data[:4*len(data)//5], data[4*len(data)//5:] 




def test(model, test_data) -> float:
    data_x, data_y = test_data
    prediction = array(list(map(model.predict, data_x)))

    deviation = abs(prediction - data_y) 
    return mean_of_sq(deviation) 

def mean_of_sq(x) -> float:
    return mean(x*x) 

def mean(arr) -> float:
    return sum(arr) / len(arr) 



if __name__ == '__main__':
    main()
