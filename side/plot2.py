import re
import math
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

from load import load_brown

# def get_words_from_file(file_path):

#     # open file and extract words
#     with open(file_path, 'r') as input_file:
#         words = []
#         for entry_text in input_file:
#             entry_words = re.findall(r'\b[A-Za-z]+\b(?![,])', entry_text.lower())
#             words.extend(entry_words)

#     return words

# load words
words = load_brown()

# count and rank words
word_count = dict(Counter(words).most_common())
n_unique_words = len(word_count)

# set up figure
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# scatter plot settings
s = 2
marker = ','
alpha = 1
color = '#00aa88'
color2 = '#6666aa'

# scatter plot
rank = np.array(range(n_unique_words))
frequency = np.array(list(word_count.values()))
ax = axes[0]
ax.scatter(rank, frequency, s=s, marker=marker, alpha=alpha, color=color)
for i, word in enumerate(list(word_count)[:5]):
    ax.text(i+300, word_count[word], word, fontsize=8)
ax.set_title(f'Word Frequency Distribution')
ax.set_xlabel('Frequency Rank')
ax.set_ylabel('Frequency')

# scatter plot log-space
rank_log = np.log(rank+1)
frequency_log = np.log(frequency)
ax = axes[1]
ax.scatter(rank_log, frequency_log, s=s, marker=marker, alpha=alpha, color=color)

lobf = np.poly1d(np.polyfit(rank_log, frequency_log, 1))(np.unique(rank_log))
lobf_x1, lobf_x2 = np.min(rank_log), np.max(rank_log)
lobf_y1, lobf_y2 = np.max(frequency_log), lobf[-1]
ax.plot([lobf_x1, lobf_x2], [lobf_y1, lobf_y2], alpha=0.6, color='r', linestyle='--', linewidth=2, label="Linear Fit")
ax.set_title(f'Log-Space Distribution')
ax.set_xlabel('$log_e$ Frequency Rank')
ax.set_ylabel('$log_e$ Frequency')
ax.legend()

# scatter plot error
linear_fit = lambda x: ((lobf_y2 - lobf_y1)/(lobf_x2 - lobf_x1)) * x + lobf_y1
frequency_error = (frequency_log - linear_fit(rank_log))
ax = axes[2]
ax.set_ylim(-5, 5)
ax.scatter(rank_log, frequency_error, s=s, marker=marker, alpha=alpha, color=color)
ax.plot([0, np.max(rank_log)], [0, 0], alpha=0.6, color='r', linestyle='--', linewidth=2, label="Linear Fit")
ax.set_title(f'Log-Space Error')
ax.set_xlabel('$log_e$ Frequency Rank')
ax.set_ylabel('$log_e$ Error')
ax.legend()


# show plot
plt.tight_layout()
plt.show()