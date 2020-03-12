import re
import math
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from load import load_brown, load_random, load_bible

# load words
words = load_brown()

# count and rank words
word_count = dict(Counter(words).most_common())
n_words = len(words)
n_unique_words = len(word_count)

# define zipf-mandelbrot formula
def zipf(r, c=1, alpha=1, beta=0):
    return c / (r + beta)**alpha

# produce rank and frequency as np arrays
rank = np.array(range(1, n_unique_words+1))
frequency = np.array(list(word_count.values()))

# calculate log values
rank_log = np.log(rank)
frequency_log = np.log(frequency)

# generate zipf score
prop_zipf = lambda r: zipf(r, c=np.max(frequency))
zipf_log = np.log(prop_zipf(rank))

# calculate error
error_log = frequency_log - zipf_log
mean_absolute_error = np.sum(np.abs(error_log)) / len(error_log)

# calculate coefficient of determination (R^2)
mean_frequency_log = np.mean(frequency_log)
total_sum_of_squares = np.sum((frequency_log - mean_frequency_log)**2)
residual_sum_of_squares = np.sum((frequency_log - zipf_log)**2)
coefficient_of_determination = 1 - (residual_sum_of_squares / total_sum_of_squares)

# set up figure
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# scatter plot
ax = axes[0]
ax.scatter(rank, frequency, s=16, marker='.', color='#00aaaa')
ax.set_title(f'Word Frequency (n={n_words:,})')
ax.set_xlabel('Frequency Rank')
ax.set_ylabel('Frequency')
if np.min(frequency) != 1:
    ax.set_ylim(bottom=0)

# scatter plot log-space
ax = axes[1]
ax.scatter(rank_log, frequency_log, s=16, marker='.', color='#00aaaa')
ax.plot(rank_log, zipf_log, color='r', alpha=0.3, linestyle='--', linewidth=2, label='Power-Law Curve')
ax.set_title('Log-Space Distribution')
ax.set_xlabel('$log_e$ Frequency Rank')
ax.set_ylabel('$log_e$ Frequency')
ax.legend()

# error
ax = axes[2]
ax.scatter(rank_log, error_log, s=16, marker='.', color='#aa66aa')
ax.plot([0, np.max(rank_log)], [0, 0], color='r', alpha=0.3, linestyle='--', linewidth=2, label='Power-Law Curve')
ax.set_ylim((-16, 16))
ax.set_title('Log-Space Error')
ax.set_xlabel('$log_e$ Frequency Rank')
ax.set_ylabel('Log-Space Error')
text_str = f'MAE = {mean_absolute_error:.3f}\n$R^2$ = {coefficient_of_determination:.3f}'
ax.text(0, -6, text_str, fontsize=10, color='#aa00aa')
ax.legend()

# show plot
plt.tight_layout()
plt.show()
