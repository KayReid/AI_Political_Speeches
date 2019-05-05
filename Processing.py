import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import csv

# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/


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
def csv_writer(candidate : str, textfile: str, csvfile: str):
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

    ft = vec.fit_transform(data['data']) #.toarray()

    # https: // scikit - learn.org / stable / tutorial / text_analytics / working_with_text_data.html
    tfidf_transformer = TfidfTransformer()
    ft_transformer = tfidf_transformer.fit_transform(ft)

    return ft_transformer

def combine(clinton_data, trump_data):
    frames = [clinton_data, trump_data]

    combo = pd.concat(frames)
    return combo


if __name__ == "__main__":

    csv_writer('clinton', 'test.txt', 'test.csv')
    csv_writer('trump', 'test.txt', 'test2.csv')
    train = csv_reader('test.csv')
    train2 = csv_reader('test2.csv')

    speech_data = combine(train, train2)

    # experiment with word count
    train['word_count'] = train['data'].apply(lambda x: len(str(x).split(" ")))
    train[['data', 'word_count']].head()

    # train['data'] = train['data'].apply(lambda x: TextBlob(x).words)

    vect = vectorize(speech_data)
    print(vect.shape)
