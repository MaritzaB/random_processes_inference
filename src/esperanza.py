import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(0, 0.15, 0.1)

def f(x):
   return 3*x**2

plt.axvline(x = 3/4, ymin = 0, ymax = 10, color = 'r')
plt.plot(f(x_values), color="blue")
plt.title("Distribución Binomial")
plt.ylabel("E[X]")
plt.xlabel("Valores k (lanzamientos exitosos)")
filepath = "slides/figures/esperanza.png"
plt.savefig(filepath)
plt.clf()
