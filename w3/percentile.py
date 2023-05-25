import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# What is the age that 75% of the people are younger than?
print(numpy.percentile(ages, 75)) # 43.0

# What is the age that 90% of the people are younger than?
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

print(numpy.percentile(ages, 90)) # 61.0

# What is the score that 20% of the people are lower than?
scores = [75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90]

print(numpy.percentile(scores, 20)) # 79.6

#Explanation
#1) Depends on context. 95th percentile in school is a good thing. 95th percentile in weight is bad. Saying x percentile means you are above that percent of people in whatever is being measured. In academics it means you have higher marks than x percent of people. In weight it means you weigh more than x percent of people.
#2) When you say "Xth percentile" it means that you are above X% of the group. So for example if a baby is at the 90th weight percentile, it means they weigh more than 90% of the babies of the same age.
#3) Also for percentile, you have to rearrange the numbers first from in order

# To understand the questions above better, the answers are listed below
#1) 75% of the people are younger than 43
#2) 90% of the people are younger than 61
#3) 20% of the people score are lower than 79.6