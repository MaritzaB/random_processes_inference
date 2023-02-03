from scipy.stats import binom
import matplotlib.pyplot as plt

n = 20
p = 0.5
k_values = list(range(n + 1))

mean, var = binom.stats(n, p)
print(
    "mean: ",
    mean,
    "var: ",
    var,
)
# mean: numero de tiros exitosos en promedio
# var:

distribution = [
    binom.pmf(k, n, p) for k in k_values
]
# Probability Mass Function (PMF): 
# Probabilidad total de lograr r exito y nr fracasos


plt.plot(
    k_values,
    distribution,
    color="black",
    linestyle="dashed",
)
plt.bar(
    k_values,
    distribution,
    color="gray",
)
plt.title("Distribucion Binomial")
plt.ylabel("Probabilidad(k)")
plt.xlabel("Valores k (lanzamientos exitosos)")
filepath = "slides/figures/binomial_distribution_normal.png"
plt.savefig(filepath)
plt.clf()
