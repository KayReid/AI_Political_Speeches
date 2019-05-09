import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.naive_bayes import MultinomialNB


def word_generator(textfile: str):

    # what could go wrong
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


# get the speakers
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
    # combine two datasets and turn into np arrays
    data = []

    for datum in dataOne:
        data.append(datum)

    for datum in dataTwo:
        data.append(datum)

    return np.array(data)


if __name__ == "__main__":

    speakers = {0: 'clinton', 1: 'trump'}

    # get the np arrays
    clinton_x = data_writer(0, 'test.txt')
    clinton_y = generate_y(0, clinton_x)
    trump_x = data_writer(1, 'test.txt')
    trump_y = generate_y(1, trump_x)

    speeches_x = combine(clinton_x, trump_x)
    print(len(clinton_x))
    print(len(trump_x))
    speeches_y = combine(clinton_y, trump_y)

    # do frequency analysis on text
    vec, vect = vectorize(speeches_x)

    # split data
    train_x = speeches_x[::2] # np.arange(0, len(speeches_x), 2)
    test_x = speeches_x[1::2] # np.arange(1, len(speeches_x), 2)

    train_y = speeches_y[::2] # np.arange(0, len(speeches_y), 2)
    test_y = speeches_y[1::2] # np.arange(1, len(speeches_y), 2)

    vec_train = vectorize(train_x)
    vec_test = vectorize(test_x)

    # Train a Naive Bayes classifier
    clf = MultinomialNB()
    clf.fit(vect, speeches_y)

    # Estimate its accuracy
    print(vect.shape)
    test_x = vec.transform(test_x)
    print(test_x.shape)
    # test_x = test_x.reshape(-1,1)
    predicted = clf.predict(test_x)

    print(np.mean(predicted == test_y))


