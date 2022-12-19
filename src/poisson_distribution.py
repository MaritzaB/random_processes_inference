from scipy.stats import poisson
import matplotlib.pyplot as plt

mu=10
n=20
k_values = list(range(n+1))

#Probability Mass Function (PMF): Probabilidad total de lograr r éxito y nr fracasos
distribution = [poisson.pmf(k, mu) for k in k_values]

plt.plot(k_values,distribution, color="blue", linestyle="dashed")
plt.bar(k_values,distribution, color="gray")
plt.title("Distribución de Poisson")
plt.ylabel("Probabilidad(k)")
plt.xlabel("x")
filepath = "slides/figures/poisson_distribution_lambda_10.png"
plt.savefig(filepath)
plt.clf()

