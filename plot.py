import logging
from collections import Counter
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
from nptyping import Array

import load

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%H:%M:%S')

def zipf(r:int, c:float=1, alpha:float=1, beta:float=0) -> float:
    '''Calculates the Zipf-Mandelbrot formula'''

    return c / (r + beta)**alpha

def get_frequency_table(words:List, binned:bool=False, n:int=-1) -> Array:

    # generate count
    count = Counter(words).most_common()[:n]
    frequency_table = np.array([(i, item[1]) for i, item in enumerate(count)])

    if binned:
        # bin frequency data into mean ranks for each frequency count
        logging.info('Binning data')

        # iterate through frequency table
        binned_frequency_record = {}
        bin_sizes = {}
        for rank, frequency in frequency_table:
            
            if frequency in binned_frequency_record:
                # skip already binned frequencies
                continue
            
            # calculate average rank and add to dictionary
            ranks = frequency_table[frequency_table[:, 1] == frequency][:, 0]
            mean_rank = np.mean(ranks)
            binned_frequency_record[frequency] = mean_rank
            bin_sizes[frequency] = len(ranks)

        # collate records into table
        binned_frequency_table = np.array([(mean_rank, frequency, bin_sizes[frequency]) for frequency, mean_rank in binned_frequency_record.items()])

        return binned_frequency_table

    return frequency_table

if __name__ == '__main__':

    # load corpus
    corpus = load.load_brown()

    # calculate tables
    frequency_table = get_frequency_table(corpus, binned=False)
    binned_frequency_table = get_frequency_table(corpus, binned=True)

    # generate colors
    max_bin_size_log = np.log(np.max(binned_frequency_table[:, 2]))
    colors = [(0, 0.8*(1 - np.log(bin_size)/max_bin_size_log), np.log(bin_size)/max_bin_size_log) for bin_size in binned_frequency_table[:, 2]]

    # define scale
    log = lambda x, base: np.log(x) / np.log(base) # log_n
    scale = lambda x: log(x, np.e) # set scale to log_e

    # plot data
    plt.scatter(scale(frequency_table[:, 0]), scale(frequency_table[:, 1]), c='#cccccc')
    plt.scatter(scale(binned_frequency_table[:, 0]), scale(binned_frequency_table[:, 1]), c=colors, marker='x', s=30)
    plt.xlabel(f'$log_e$ Rank')
    plt.ylabel(f'$log_e$ Frequency')
    plt.show()