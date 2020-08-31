from typing import Dict, List
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

import load

def zipf(r:int, c:float=1, alpha:float=1, beta:float=0) -> float:
    '''Calculates the Zipf-Mandelbrot formula'''

    return c / (r + beta)**alpha

def plot_corpus(words:List[str], scale:str='linear', n:int=-1):
    '''Plots a scatter plot for a given corpus'''

    # specify plot configuration
    plot_kwargs = {
        'c': '#4444cc',
        'marker': '.',
        's': 32,
    }

    # count and rank words
    word_count = dict(list(Counter(words).most_common())[:n])
    n_unique_words = len(word_count)

    # produce rank and frequency as np arrays
    rank = np.array(range(1, n_unique_words+1))
    frequency = np.array(list(word_count.values()))

    if scale == 'linear':

        # plot a linear scatter
        plt.scatter(rank, frequency, **plot_kwargs)
        plt.xlabel('Rank')
        plt.ylabel('Frequency')

    else:

        # plot a linear scatter
        plt.scatter(np.log(rank), np.log(frequency), **plot_kwargs)
        plt.xlabel('$log_e$ Rank')
        plt.ylabel('$log_e$ Frequency')


    # # generate zipf score
    # prop_zipf = lambda r: zipf(r, c=np.max(frequency))
    # zipf_log = np.log(prop_zipf(rank))

    # # calculate error
    # error_log = frequency_log - zipf_log
    # mean_absolute_error = np.sum(np.abs(error_log)) / len(error_log)

    # # calculate coefficient of determination (R^2)
    # mean_frequency_log = np.mean(frequency_log)
    # total_sum_of_squares = np.sum((frequency_log - mean_frequency_log)**2)
    # residual_sum_of_squares = np.sum((frequency_log - zipf_log)**2)
    # coefficient_of_determination = 1 - (residual_sum_of_squares / total_sum_of_squares)



if __name__ == '__main__':

    # load corpera
    corpera = {
        'Brown Corpus': load.load_brown(),
        'King James Bible': load.load_bible(),
        'Random (Small)': load.load_random(size='small'),
        'Random (Medium)': load.load_random(size='medium'),
        'Random (Large)': load.load_random(size='large'),
    }

    # set up figure
    fig = plt.figure(figsize=(6, 6))

    for i, (corpus_name, corpus_words) in enumerate(corpera.items()):
        # print(i, corpus_name, len(corpus_words))

        plt.subplot(2, 3, i+1)
        plt.title(corpus_name)
        plot_corpus(corpus_words, scale='log')

    # show plot
    plt.tight_layout(pad=2)
    plt.show()