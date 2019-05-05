import re
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


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
def vectorize(candidate : str, textfile: str):
    vec = CountVectorizer()

    dataset = []
    data = ""

    # creates a word generator
    generator = word_generator(textfile)

    try:
        while True:
            # group into sets of 100
            for _ in range(100):
                data += " " + next(generator)
            dataset.append(categorize(data, candidate))
    except StopIteration:
        # print("Document processed.")
        pass

    # initialize x to use it outside of the for loop
    x = vec

    for data in dataset:
        x = vec.fit_transform(data).toarray()

    # https: // scikit - learn.org / stable / tutorial / text_analytics / working_with_text_data.html
    # TODO: you're at the occ to frequency part
    tfidf_transformer = TfidfTransformer()
    x_tf = tfidf_transformer.fit_transform(x)

    return x_tf


# put into correct format
def categorize(sample, category):
    return [sample, category]


if __name__ == "__main__":

    data = vectorize("hilary", "test.txt")
    print(data.toarray())
