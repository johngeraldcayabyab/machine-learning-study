import numpy as np
import matplotlib.pyplot as plt

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# window = 2
# average_data = []
#
# for index in range(len(data) - window + 1):
#     windowRange = data[index:index + window]  # list slice
#     rangeMean = np.mean(windowRange)
#     average_data.append(rangeMean)

x = np.linspace(0, 10, 50)
y = np.sin(x)
window = 5
average_y = []
for ind in range(len(y) - window + 1):
    average_y.append(np.mean(y[ind:ind + window]))
