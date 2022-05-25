import pandas as pd

# find-s algorithm
def train(attributes, target):
    for r, val in enumerate(attributes):
        if target[r] == "Y":  # modified
            specific_hypothesis = val.copy()
            break
             
    for i, val in enumerate(attributes):
        if target[i] != "Y":
            continue 
    
        for c in range(len(specific_hypothesis)):
            if val[c] != specific_hypothesis[c]:
                specific_hypothesis[c] = '?'
                
    return specific_hypothesis


data = pd.read_csv("datasets/loan.csv").iloc[:5]
print(data)
 
attributes = data.iloc[:, :-1].values
print("The attributes are:\n", attributes)
 
target = data.iloc[:,-1].values
print("The targets are:\n ", target)
 
 
print("\nThe final hypothesis is:\n",train(attributes, target))