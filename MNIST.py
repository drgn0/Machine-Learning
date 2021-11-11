''' gave 92% accuracy ''' 

import numpy as np 
import pandas as pd 

import NeuralNetwork


def give_data(file_name):
    file_path = 'F:\Study Material\ML\DataSets\\' + file_name
    train_data = pd.read_csv(file_path, names = ['y'] + ['x_' + str(i) for i in range(28*28)]) 

    labels = [np.zeros((10, 1)) for i in range(len(train_data))]
    for i, y in enumerate(train_data['y']):
        labels[i][y][0] = 1 
    
    return [(train_data.iloc[i][1:].values.reshape(784, 1) / 255, labels[i]) for i in range(len(train_data))] 
     

def main():
    training_data = give_data('mnist_train.csv')
    # image, label

    test_data = give_data('mnist_test.csv') 
    
    print("Starting Training.") 
    net = NeuralNetwork.Network([28*28, 30, 10])

    net.SGD(training_data, 10, 2.2, test_data=test_data) 



if __name__ == '__main__':
    main() 
