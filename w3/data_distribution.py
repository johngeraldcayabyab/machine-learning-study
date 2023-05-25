import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

# uniform, give random number between 0.0 and 5.0. Third param gives you more sample size
print(x)

plt.hist(x, 5)
plt.show()
