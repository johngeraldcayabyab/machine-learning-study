import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

print(actual)
print(predicted)

# 20 is amount of coin flips
# 6 is expected number of heads in the flips
# Formula P(x:n,p) = nCx x px(1-p)n-x

# (20! / (6! × (20 - 6)!)) × (0.50) ^ (6) × (1 - 0.50) ^ (20 - 6)

# Can be translated to 20 amount of days
# 10 expected up days. I think minervini mentioned something about how many weeks before something goes up after the VCP
# so in a market, running numpy.random.binomial(1, ?????) 1 is green candle, 0 is red candle. ???? = the bias if it will go up or down since it's not 50/50 how will you get the ????


confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
# cm_display.plot()
# plt.show()

# The Confusion Matrix created has four different quadrants:

# True Negative (Top-Left Quadrant)
# False Positive (Top-Right Quadrant)
# False Negative (Bottom-Left Quadrant)
# True Positive (Bottom-Right Quadrant)


Accuracy = metrics.accuracy_score(actual, predicted)  # (True Positive + True Negative) / Total Predictions
Precision = metrics.precision_score(actual, predicted)  # True Positive / (True Positive + False Positive)
print(Accuracy)
print(Precision)

# True Positive / (True Positive + False Negative)
# Sensitivity is good at understanding how well the model predicts something is positive:
Sensivitiy_recall = metrics.recall_score(actual, predicted)
print(Sensivitiy_recall)

# How well the model is at prediciting negative results?
# Specificity is similar to sensitivity, but looks at it from the persepctive of negative results.
Specificity_recall = metrics.recall_score(actual, predicted, pos_label=0)

# F-score
# F-score is the "harmonic mean" of precision and sensitivity.
# It considers both false positive and false negative cases and is good for imbalanced datasets.
# How to Calculate
# 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

F1_score = metrics.f1_score(actual, predicted)
print(F1_score)

# for more resources
# https://towardsdatascience.com/baffling-concept-of-true-positive-and-true-negative-bffbc340f107
