import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv('./csv/people.csv')

nationalityMap = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(nationalityMap)
goMap = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(goMap)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()

# you can still use X but X.values removes the warning because of Dataframe Stuff https://stackoverflow.com/questions/69326639/sklearn-warning-valid-feature-names-in-version-1-0
dtree = dtree.fit(X.values, y)

# If you want to see the decision tree, then print this
tree.plot_tree(dtree, feature_names=features)

prediction = dtree.predict([[40, 10, 7, 1]])

print(prediction)
# print(dtree.predict([[40, 10, 7, 1]]))

# print(X)
