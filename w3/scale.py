import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv('../csv/data_scale.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)
print(scaledX)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedC02 = regr.predict([scaled[0]])

print(predictedC02)
