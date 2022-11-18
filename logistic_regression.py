import numpy
from sklearn import linear_model

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape([-1, 1])

y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

predicted = logr.predict(numpy.array([1.46]).reshape(-1, 1))

print(predicted)

# Odds and Coefficient
log_odds = logr.coef_
odds = numpy.exp(log_odds)

print(odds)


# Probability since were only checking binomial values

def logit2prob(logr, x):
    log_odds = logr.coef_ * x + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return (probability)


# Checks the percentage if a value has the probability to become a tumor
print(logit2prob(logr, X))
