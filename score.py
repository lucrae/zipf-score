import re
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

# extract words from text file
with open('input.txt', 'r') as input_file:
    words = []
    for entry_text in input_file:
        entry_words = re.findall(r'\b[A-Za-z]+\b(?![,])', entry_text.lower())
        words.extend(entry_words)

# count and rank words
word_count = dict(Counter(words).most_common())
n_unique_words = len(word_count)
# plot
fig, ax = plt.subplots()
ax.scatter(range(n_unique_words), list(word_count.values()), marker='.', alpha=0.8)
# ax.set_xticks(np.arange(1, n_unique_words+1, 25))
n_labels = 6
for i, word in enumerate(list(word_count)[:n_labels]):
    ax.text(i, word_count[word], word, fontsize=8)
plt.show()