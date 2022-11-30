import pandas as pd
from sklearn import linear_model

# Categorial data is about transforming data into bits, or numbers
# whats the difference of categorial data to scaling?
# Problem with label encoding is that it assumes higher the categorical value, better the category. “Wait, What!?”.
# This is why we use one hot encoder to perform “binarization” of the category and include it as a feature to train the model.
# source of one hot encoding https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f

cars = pd.read_csv('../csv/data.csv')
# print(cars.to_string())

# one hot encoding
ohe_cars = pd.get_dummies(cars[['Car']])

# print(ohe_cars.to_string())

X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# print(X)

predictedC02 = regr.predict([[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

print(predictedC02)

# other examples if only two values
# still use on hot encoding but drop the first column making it more binary like
colors = pd.DataFrame({'color': ['blue', 'red']})
dummies = pd.get_dummies(colors, drop_first=True)
print(dummies)

# what if we have three more groups and you still want to represent the data in more less column?
colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
print(dummies)
# there you got, but it's not worth it
