import random as rand
import matplotlib.pyplot as plt

n = 100000
n_in = 0
n_out = 0
x0 = 0
pilist = []
x0list = []
#设置横纵坐标
for i in range(1, n):
    x = rand.random()
    y = rand.random()
    m = x**2 + y**2
    x0 += 1
    if m < 1:
        n_in += 1
    else:
        n_out += 1
    Pi = 4*n_in/(n_in+n_out)
    pilist.append(Pi)
    x0list.append(x0)
plt.scatter(x0list, pilist)
plt.show()
print('Pi =', 4*n_in/n)
