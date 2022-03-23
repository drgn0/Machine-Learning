# import numpy as np 
import matplotlib.pyplot as plt 

import DataGenerator 
import Regression 

class Tester:
    def test_data(self):
        pass 
    

def plot(data_x, data_y):
    plt.scatter(data_x, data_y) 
    plt.show() 

if __name__ == '__main__':
    line = DataGenerator.Line((1, 1), 0) 

    print(*line.generate(10))