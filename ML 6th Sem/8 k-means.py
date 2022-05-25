
# TODO: a way to find accuracy 


from numpy.random import choice

class KMeans:
    def __init__(self, data, K = 3):
        self.data = data 
        self.K = K 

        self.centroids = list(map(data.__getitem__, choice(len(data), size = K, replace=False)))
        self.train() 

    def train(self):
        # Finds Centroids
        old_centroids = [None] * self.K

        while any((o != n).all() for o, n in zip(old_centroids, self.centroids)):
            # print(self.centroids)
            clusters = self.get_clusters() 
            old_centroids = self.centroids
            self.centroids = list(map(self.mean, clusters))
            
    def get_clusters(self):
        clusters = [[] for i in range(self.K)]  
        for x in self.data:
            closest_cluster_i = self.predict(x) 
            clusters[closest_cluster_i].append(x) 
        
        return clusters 

    def predict(self, elem):
        # returns index of closest cluster 
        distances = [self.distance(centroid, elem) for centroid in self.centroids] 
        return min(range(len(distances)), key = distances.__getitem__)  

    @staticmethod
    def distance(x, y):
        return sum(abs(x - y))

    @staticmethod 
    def mean(arr):
        return sum(arr) / len(arr)
    


def get_train_test_data(split_ratio = 0.8): 
    from pandas import read_csv    
    data = read_csv("datasets/iris.csv").sample(frac = 1)  
    
    split_point = int(split_ratio * len(data)) 
    return split_data(data[:split_point]), split_data(data[split_point:]) 

def split_data(data):
    return data.iloc[:, :-1].values, data.iloc[:, -1].values


train_data, test_data = get_train_test_data() 

train_data_x = train_data[0] 

k_means = KMeans(train_data_x) 

def test(model, test_data_x, test_data_y):
    raise NotImplementedError("Find a Way to Find Accuracy")
    accuracy = sum(model.predict(x) == y for x, y in zip(test_data_x, test_data_y)) 
    print(f'{accuracy=}')

test(k_means, *test_data) 
