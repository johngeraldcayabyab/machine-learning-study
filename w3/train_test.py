import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print(r2)

print(mymodel(5))

# print(y)

# plt.scatter(test_x, test_y)
# plt.show()


# read more
# https://data-flair.training/blogs/train-test-set-in-python-ml/
# https://towardsdatascience.com/how-to-split-a-dataset-into-training-and-testing-sets-b146b1649830