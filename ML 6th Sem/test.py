def modify_data():
    import pandas as pd 

    data = pd.read_csv("datasets/loan_data_set.csv") 

    # new_data = data.loc[:, ['Gender', 'Married', 'Education', 'Property_Area', 'Loan_Status']]
    data.iloc[:, -1].replace('Y', 'Yes') 
    data.iloc[:, -1].replace('N', 'No') 

    print(data.head())

    # data.to_csv("datasets/loan_data_set_.csv", index = False)
