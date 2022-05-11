import random 

class KMeans:
    def __init__(self, data, K):
        self.data = data 
        self.K = K 

        self.centroids = random.sample(data, K)
        self.train() 

    def train(self):
        # Finds Centroids
        old_centroids = None 

        while old_centroids != self.centroids:
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
        return abs(x - y) 

    @staticmethod 
    def mean(arr):
        return sum(arr) / len(arr)
    
if __name__ == '__main__':
    data = [2, 3, 5, 8, 10, 14, 17, 20, 21]

    model = KMeans(data, 3) 

    print(model.predict(18))


'''
KNN 
Naive Bias 
K Means 
'''
