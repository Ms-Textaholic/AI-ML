import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot([1,2,3,4],[2,4,6,8])
plt.ylabel('numbers')
plt.show()


plt.plot([1,2,3,4],[10,15,35,70])
plt.ylabel('numbers')
plt.show()


x=np.linspace(0,100,10)
print(x)


y=x**2
print(y)

plt.scatter(x,y)

N_points = 1000
n_bins = 10

x = np.random.randn(N_points)
y = .6*x+np.random.randn(1000)+5

fig, axs = plt.subplots(1, 2, sharey=True)

axs[0].hist(x, bins=n_bins)
axs[1].hist(y, bins=n_bins)
