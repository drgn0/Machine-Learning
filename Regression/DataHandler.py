class DataHandler:
    def __init__(self, n_samples = 500, n_features = 1):
        self._already_tested = False 
        self._make_data(n_samples, n_features) 


    def _make_data(self, n_samples, n_features):
        from sklearn.datasets import make_regression

        data_x, data_y = make_regression(n_samples, n_features, noise=7, bias=100)

        self.x_training, self.y_training = data_x[:4*n_samples // 5], data_y[:4*n_samples // 5]
        self._x_test, self._y_test = data_x[4*n_samples // 5:], data_y[4*n_samples // 5:]

    def give_training_data(self):
        return self.x_training, self.y_training 

    def find_error(self, data_x, data_y, func):
        return sum( (func(x) - y) ** 2 for x, y in zip(data_x, data_y) ) / (2 * len(data_x)) 

    def training_error(self, func):
        return self.find_error(self.x_training, self.y_training, func) 

    def _test_error(self, func):
        # can only be called once. 
        if self._already_tested:
            raise ValueError("Test Data has already been tested once.")
        
        self._already_tested = True 
        return self.find_error(self._x_test, self._y_test, func) 
