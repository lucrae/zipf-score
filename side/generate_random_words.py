import random

import matplotlib.pyplot as plt
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
unique_words = list(dict.fromkeys(words))

n_words = 100000

with open('random_medium.txt', 'w') as file:

    random_words = []
    for i in range(n_words):
        random_words.append(random.choice(unique_words))

    file.write(' '.join(random_words))