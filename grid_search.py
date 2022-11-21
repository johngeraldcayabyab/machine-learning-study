# https://towardsdatascience.com/grid-search-in-python-from-scratch-hyperparameter-tuning-3cca8443727b
# https://kapernikov.com/tutorial-image-classification-with-scikit-learn/ review this code in the future on how to make your own image dataset

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris['data']
y = iris['target']

logit = LogisticRegression(max_iter=10000)

print(logit.fit(X, y))
print(logit.score(X, y))

C = [0.25, 0.5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5]

scores = []

for choice in C:
    logit.set_params(C=choice)
    logit.fit(X, y)
    scores.append(logit.score(X, y))

#We can see that the lower values of C performed worse than the base parameter of 1. However, as we increased the value of C to 1.75 the model experienced increased accuracy.
#It seems that increasing C beyond this amount does not help increase model accuracy.
print(scores)

#We scored our logistic regression model by using the same data that was used to train it. If the model corresponds too closely to that data, it may not be great at predicting unseen data. This statistical error is known as over fitting.
#To avoid being misled by the scores on the training data, we can put aside a portion of our data and use it specifically for the purpose of testing the model. Refer to the lecture on train/test splitting to avoid being misled and overfitting.
