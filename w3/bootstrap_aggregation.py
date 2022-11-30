from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt

# https://www.sharpsightlabs.com/blog/scikit-train_test_split/
data = datasets.load_wine(as_frame=True)

X = data.data
y = data.target

X_train, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.25, random_state=22)

dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train, y_train)
# decision_tree


y_pred = dtree.predict(X_test)

print("Train data accuracy:", accuracy_score(y_true=y_train, y_pred=dtree.predict(X_train)))
print("Test data accuracy:", accuracy_score(y_true=y_test, y_pred=y_pred))

estimator_range = [2, 4, 6, 8, 10, 12, 14, 16]
models = []
scores = []

for n_estimators in estimator_range:
    clf = BaggingClassifier(n_estimators=n_estimators, random_state=22)
    clf.fit(X_train, y_train)

    models.append(clf)
    scores.append(accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))

plt.figure(figsize=(9, 6))
plt.plot(estimator_range, scores)

plt.xlabel("n_estimators", fontsize=18)
plt.ylabel("score", fontsize=18)
plt.tick_params(labelsize=16)

plt.show()
