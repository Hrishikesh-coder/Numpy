import numpy as np

import matplotlib.pyplot as plt

a = np.arange(30)

print(a.shape)

a.shape = 2,-1,3

print(a.shape)

print(a)

mu,sigma = 2,0.5

v = np.random.normal(mu,sigma,10000)

plt.hist(v,bins=50,density=1)

plt.show()

(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()

