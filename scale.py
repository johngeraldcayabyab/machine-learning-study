import pandas
from sklearn import linear_model
from sklear.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv('./csv/data_scale.csv')

X = df[['Weight', 'Volume']]
y = df['C02']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX,y)

print(scaledX)

scaled = scale.transform([[2300,1.3]])

predictedC02 = regr.predict([[scaled[0]])
                             
print(predictedC02)


