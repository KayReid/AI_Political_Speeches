import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np


# goes through a file and creates a generator
def word_generator(textfile: str):

    try:
        f = open(textfile)
    except IOError:
        print("File was not found.")
        return

    # TODO make regex more robust
    # this separates the tokens
    split_pattern = re.compile('[\s?.!;:\-(),\\\]')

    for line in f:
        words = (w for w in split_pattern.split(line) if w)
        for w in words:
            yield w


# split into sets of 100
def data_writer(textfile: str):
    # creates a word generator
    generator = word_generator(textfile)
    dataset = []

    try:
        # loop through and read the words
        while True:
            data = ""

            # group into sets of 100
            for _ in range(100):
                data += " " + next(generator)
            dataset.append(data)

    except StopIteration:
        pass

    return dataset


# get the speakers into a list
def generate_y(speaker, data):
    y = []

    for _ in range(len(data)):
        y.append(speaker)

    return y


def vectorize(data):
    # count words in sample
    vec = CountVectorizer()
    ft = vec.fit_transform(data)

    # turn into frequency analysis
    transformer = TfidfTransformer()
    return vec, transformer.fit_transform(ft)


def combine(dataOne, dataTwo):
    # combine two data sets and turn into np arrays
    data = []

    for datum in dataOne:
        data.append(datum)

    for datum in dataTwo:
        data.append(datum)

    return np.array(data)


