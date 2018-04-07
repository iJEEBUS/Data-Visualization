import numpy as np
import matplotlib.pyplot as plt

# Create vector of 10000 items that have a normal
# distribution, a variance of 0.5^2, and a mean of 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)

# Plot histogram (normalized) with 50 bins
plt.hist(v, bins=50, density=1)
#plt.show()

# Compute histogram with numpy then plot it
(n, bins) = np.histogram(v, bins=50, normed=True)
plt.plot(0.5*(bins[1:]+bins[:-1]), n)
plt.show()