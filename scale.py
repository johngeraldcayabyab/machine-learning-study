import pandas
from sklearn import linear_model
from sklear.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv('./csv/data.csv')

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
