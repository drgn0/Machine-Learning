import numpy as np

class Network:
    def __init__(self, layer_sizes):
        self.weights = ([np.random.standard_normal((x, y)) / np.sqrt(x) for x, y in zip(layer_sizes[1:], layer_sizes[:-1])])
        self.biases  = ([np.random.standard_normal((x, 1)) for x in layer_sizes[1:]])
    
    def predict(self, x):
        a = x

        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.matmul(w, a) + b)
        
        return a 
    
    def feedforward(self, x):
        z = [] 
        a = [x]  # hopefully, i won't be changing  a or x 

        for b, w in zip(self.biases, self.weights):
            z.append( np.dot(w, a[-1]) + b ) 
            a.append(self.sigmoid(z[-1])) 
        
        return z, a 


    def SGD(self, training_data, epochs, learning_rate, mini_batch_size = 10, test_data = None):
        for e in range(epochs):
            np.random.shuffle(training_data) 
            for elem in training_data:
                x, y = elem 
                self.train(x, y, learning_rate) 
            # for i in range(0, len(X), mini_batch_size):
            #     self.train(X[i:i+mini_batch_size], Y[i:i + mini_batch_size], learning_rate)

            if test_data:
                correct_guesses = self.evaluate(test_data) 
                print(f'Epoch {e}: {correct_guesses}/{len(test_data)} \t {100 * correct_guesses / len(test_data)}%')


    def train(self, x, y, learning_rate):
        z, a = self.feedforward(x)
        delta = self.backpropagate(z, a, y) 
        self.update(delta, a, learning_rate) 

    def backpropagate(self, z, a, y):
        delta = [np.zeros(b.shape) for b in self.biases]

        delta[-1] = self.cost_derivative(a[-1], y)  *  self.sigmoid_prime(z[-1]) 
        
        for l in range(len(delta) - 2, -1, -1):  # oh no.. l is a bad name for variable..  well.. anyway..
            delta[l] = np.dot(self.weights[l + 1].transpose(), delta[l + 1]) * self.sigmoid_prime(z[l]) 
            
        return delta 

    def update(self, delta, a, learning_rate):
        self.biases = [b - learning_rate * db for b, db in zip(self.biases, delta)]

        d_w = [np.dot(delta[l], a[l].transpose()) for l in range(len(delta))]
        # print(d_w[0].shape, self.weights[0].shape)
        self.weights = [w - learning_rate * dw for w, dw in zip(self.weights, d_w)] 

    def evaluate(self, test_data):
        return sum(self.predict(elem[0]).argmax() == elem[1].argmax() for elem in test_data) 


    def cost_derivative(self, predicted, actual):
        return predicted - actual 


    # @staticmethod
    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z)) 

    # @staticmethod
    def sigmoid_prime(self, z):
        sig = self.sigmoid(z) 
        return sig * (1 - sig) 
