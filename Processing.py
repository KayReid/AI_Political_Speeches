import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import csv
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
# https://sigdelta.com/blog/text-analysis-in-pandas/

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
def csv_writer(candidate, textfile: str, csvfile: str):
    # creates a word generator
    generator = word_generator(textfile)

    try:
        with open(csvfile, mode='w') as test_file:
            # initialize
            writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['candidate', 'data'])

            while True:
                data = ""

                # group into sets of 100
                for _ in range(100):
                    data += " " + next(generator)

                writer.writerow([candidate, data])

    except StopIteration:
        # print("Document processed.")
        pass


def csv_reader(filename : str):
    df = pd.read_csv(filename)
    return df


def vectorize(data):
    vec = CountVectorizer()
    ft = vec.fit_transform(data['data'])

    # https: // scikit - learn.org / stable / tutorial / text_analytics / working_with_text_data.html
    tfidf_transformer = TfidfTransformer()
    ft_transformer = tfidf_transformer.fit_transform(ft)

    return ft_transformer


def combine(clinton_data, trump_data):
    frames = [clinton_data, trump_data]

    combo = pd.concat(frames)
    return combo


if __name__ == "__main__":

    # speakers = {'clinton': 0, 'trump': 1}
    csv_writer('clinton', 'test.txt', 'test.csv')
    csv_writer('trump', 'test.txt', 'test2.csv')
    train = csv_reader('test.csv')
    train2 = csv_reader('test2.csv')

    speech_data = combine(train, train2)

    # experiment with word count
    # train['word_count'] = train['data'].apply(lambda x: len(str(x).split(" ")))
    # train[['data', 'word_count']].head()
    # train['data'] = train['data'].apply(lambda x: TextBlob(x).words)

    # train and test split
    train, test = train_test_split(speech_data, test_size=0.2)

    test_vec = vectorize(test)
    train_vec = vectorize(train)

    """
    frequency_vec = vectorize(speech_data)
    print(frequency_vec.shape)
    print(frequency_vec)
    clf = MultinomialNB().fit(frequency_vec, speech_data['candidate'])
    """

    # Train a Naive Bayes classifier
    clf = MultinomialNB()
    clf.fit(train_vec, train['candidate'])

    # Estimate its accuracy
    print(test_vec.shape)
    print(test['candidate'].shape)
    print(clf.score(test_vec, test['candidate']))


