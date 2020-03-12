import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = 100000000 / x

plt.subplot(121)
plt.plot(x, y)

a = np.log(x)
b = np.log(y)

plt.subplot(122)
plt.plot(a, b)

plt.show()