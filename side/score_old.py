from typing import List
from collections import Counter
from time import time

import matplotlib.pyplot as plt
import numpy as np

# constants
ENGLISH_ALPHABET_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

def get_string_size(string: str, format: str='utf8') -> int:
    '''Returns size of string in bytes'''
    return len(string.encode('utf-8'))

def get_words_from_text(text: str, approved_chars=ENGLISH_ALPHABET_CHARS) -> List[str]:
    '''Returns list of filtered words from a text'''

    # filter unwanted characters from text
    text = ''.join(char for char in text if char in approved_chars)

    # split and format words into list
    words = [word.lower() for word in text.split(' ') if len(word) > 0]

    return words

# read in file
with open('input.txt', 'r') as input_file:

    # iterate through file entries and extract words
    words = []
    for i, entry_text in enumerate(input_file):

        # get words from text and append
        entry_words = get_words_from_text(entry_text)
        words.extend(entry_words)

    # count and rank words
    word_count_rank = dict(Counter(words).most_common())
    n_unique_words = len(word_count_rank)

    # plot
    fig, ax = plt.subplots()
    plot = ax.plot(range(n_unique_words), list(word_count_rank.values()))
    ax.set_xticks(np.arange(1, n_unique_words+1, 25))

    n_labels = 6
    for i, word in enumerate(list(word_count_rank)[:n_labels]):
        ax.text(i, word_count_rank[word], word, fontsize=8)

    plt.show()