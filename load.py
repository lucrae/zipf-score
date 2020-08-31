import re
import os

def load_brown():

    # get file paths
    file_directory = os.path.join('corpus', 'brown')
    file_filter = lambda file_name: file_name != 'meta'
    file_paths = [os.path.join(file_directory, file_name) for file_name in os.listdir(file_directory) if file_filter(file_name)]
    
    # iterate through files
    brown_words = []
    for file_path in file_paths:

        # extract words from file
        with open(file_path, 'r') as file:

            file_words = []

            # iterate through text entries
            for entry in file:
                if len(entry) > 1:

                    # get words
                    words = [entry_piece.split('/')[0] for entry_piece in entry.split()]
                    
                    # filter words
                    word_filter = lambda word: word != word.upper() # not all caps
                    word_format = lambda word: word.lower()
                    words = [word_format(word) for word in words if word_filter(word)]
                    
                    brown_words.extend(words)
    
    return brown_words

def load_random(size='large'):

    file_path = os.path.join('corpus', 'random', f'random_{size}.txt')
    with open(file_path, 'r') as file:
        file_words = file.read().split(' ')

    return file_words

def load_bible():

    # open file and extract words
    file_path = os.path.join('corpus', 'bible', 'king_james.txt')
    with open(file_path, 'r') as file:
        words = re.findall(r'\b[A-Za-z]+\b(?![,])', file.read().lower())

    return words
