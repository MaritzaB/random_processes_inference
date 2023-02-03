import random
import math
import matplotlib.pyplot as plt


steps = 100
step_weigth = 1

x = y = 0
x_list = [x]
y_list = [y]

listax = [x]
listay = [y]
for i in range(steps + 1):
    angulo = random.random() * math.pi * 2
    x += step_weigth * math.cos(angulo)
    y += step_weigth * math.sin(angulo)
    listax.append(x)
    listay.append(y)


# Plot random_walk
plt.plot(
    listax,
    listay,
    color="black",
)
plt.axis("equal")
plt.title("Caminata aleatoria")
filepath = "reports/figures/Random_walk.png"
plt.savefig(filepath)
plt.clf()
