from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

choices = np.arange(0, 100)

plt.subplot(121)
a = np.random.choice(choices, 100000)
plt.scatter(range(len(a)), a)

plt.subplot(122)

count = dict(Counter(a).most_common())
keys = list(count)
freq = list(count.values())
ranks = range(len(count))

plt.scatter(ranks, freq)
plt.xticks(ranks, keys)


plt.show()