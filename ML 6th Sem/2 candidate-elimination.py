import numpy as np 
import pandas as pd

def learn(attributes, target): 
    specific_h = attributes[0].copy()
    general_h = [["?"] * len(specific_h) for i in range(len(specific_h))]

    for i, h in enumerate(attributes):
        if target[i] == "Y":
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]:                    
                    specific_h[x] = '?'                     
                    general_h[x][x] = '?'
                   
        if target[i] == "N": 
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        

    general_h = [h for h in general_h if h != ['?'] * len(specific_h)]
    
    return specific_h, general_h 

data = pd.read_csv("datasets/loan.csv").iloc[:3]

print(data)
 
attributes = np.array(data)[:,:-1]
print("The attributes are:\n", attributes)
 
target = np.array(data)[:,-1]
print("The targets are:\n ", target)
 



specifics, generals = learn(attributes, target)

print("Final Specific Hypothesis: ", specifics, sep="\n")
print("Final General Hypothesis: ", generals, sep="\n")