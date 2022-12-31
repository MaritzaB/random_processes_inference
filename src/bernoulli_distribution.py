from scipy.stats import bernoulli
import matplotlib.pyplot as plt

data = bernoulli.rvs(p = 0.5, size=1000)

plt.hist(data)
plt.show()
