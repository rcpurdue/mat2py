# ex7: Plots, Python

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10000, 1)

plt.hist(x, 50, edgecolor='w')
plt.xlabel('Bin')
plt.ylabel('Value')
plt.title('Histogram, Normal Distribution')
plt.text(-3.5, 600, 'n=10,000, bins=50')
plt.axis([-4, 4, 0, 800])
plt.grid(True)
plt.show()
