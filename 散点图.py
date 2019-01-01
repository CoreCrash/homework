import random as rand
import matplotlib.pyplot as plt

num_in = 0
times = 10000
for i in range(0, times):
    x = rand.random()
    y = rand.random()
    s = x**2 + y**2
    if s <= 1:
        num_in += 1
Pi = num_in*4/times
print(Pi)

x_out = []
y_out = []
x_in = []
y_in = []
for i in range(0, 2000):
    x = rand.random()
    y = rand.random()
    if x**2+y**2 < 1:
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)
    plt.scatter(x_in, y_in, edgecolor='none',s=10)
    plt.scatter(x_out, y_out, c='red', edgecolor='none', s=10)
plt.show()
