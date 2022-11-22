import pandas as pd

# Categorial data is about transforming data into bits, or numbers
# whats the difference of categorial data to scaling?
# Problem with label encoding is that it assumes higher the categorical value, better the category. “Wait, What!?”.
# This is why we use one hot encoder to perform “binarization” of the category and include it as a feature to train the model.

cars = pd.read_csv('./csv/data.csv')
# print(cars.to_string())

# one hot encoding
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())
