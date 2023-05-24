import numpy as np

a = np.array([100, 105, 100, 95, 100], dtype=float)
print(np.diff(a) / a[:-1] * 100.)



