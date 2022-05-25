def get_train_test_data(split_ratio = 0.8): 
    from pandas import read_csv    
    data = read_csv("datasets/iris.csv").sample(frac = 1)  
    
    split_point = int(split_ratio * len(data)) 
    return split_data(data[:split_point]), split_data(data[split_point:]) 

def split_data(data):
    return data.iloc[:, :-1].values, data.iloc[:, -1].values


def get_decision_tree():
    from sklearn.tree import DecisionTreeClassifier 
    return DecisionTreeClassifier(max_depth=3) 


train_data, test_data = get_train_test_data() 
model = get_decision_tree() 
model.fit(*train_data) 

def test(model, test_x, test_y):
    predicted_y = model.predict(test_x) 

    for x, y in zip(test_x, predicted_y):
        print(f"Prediction for {x} = {y}") 
    

    from sklearn import metrics 

    confusion_matrix = metrics.confusion_matrix(test_y, predicted_y)
    print("\nConfusion Matrix:\n", confusion_matrix)
    accuracy = metrics.accuracy_score(test_y, predicted_y)
    print("\nAccuracy:", accuracy, '\n')

test(model, *test_data) 