import matplotlib.pyplot as plt
import numpy as np


# Creating random dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)

plt.boxplot(data)

filepath = "reports/figures/boxplot_test.png"
plt.savefig(filepath)
plt.clf()
