import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# To calculate the mean, find the sum of all values, and divide the sum by the number of values:
x = numpy.mean(speed)

print(x)

# The median value is the value in the middle, after you have sorted all the values:
y = numpy.median(speed)

print(y)

# If there are two numbers in the middle, divide the sum of those numbers by two.
speed2 = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

z = numpy.median(speed2)

print(z)

a = stats.mode(speed, keepdims=True)

print(a)
