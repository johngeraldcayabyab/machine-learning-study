import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

#What is the age that 75% of the people are younger than?
print(numpy.percentile(ages, 75))

#What is the age that 90% of the people are younger than?
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

print(numpy.percentile(ages, 90))

#What is the score that 20% of the people are lower than?
scores = [75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90]

print(numpy.percentile(scopres, 20))

