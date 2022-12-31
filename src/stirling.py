import math
import matplotlib.pyplot as plt


def Stirling(n):
    return (
        math.sqrt(2 * math.pi * n)
        * (n**n)
        * math.e ** (-n)
    )


n = list(range(0, 101, 5))
error = []

for i in n:
    error.append(
        (
            (math.factorial(i) - Stirling(i))
            / math.factorial(i)
        )
        * 100
    )

plt.figure(figsize=(10, 8))
plt.scatter(n[1::], error[1::])
plt.annotate(
    "("
    + str(n[2])
    + " , "
    + "{:0.2}".format(error[2])
    + ")",
    [10, 0.9],
)
plt.annotate(
    "("
    + str(n[-1])
    + " , "
    + "{:0.2}".format(error[-1])
    + ")",
    [90, 0.15],
)

filepath = "reports/figures/stirling.png"
plt.savefig(filepath)
plt.clf()
