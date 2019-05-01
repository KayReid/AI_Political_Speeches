import re
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer


def word_generator(textfile: str):

    # what could go wrong
    try:
        f = open(textfile)
    except IOError:
        print("File was not found.")
        return

    # TODO make regex more robust
    # this separates the tokens
    split_pattern = re.compile('[\s?.!;:\-(),]')

    for line in f:
        words = (w for w in split_pattern.split(line) if w)
        for w in words:
            yield w


# split into sets of 100
def split_data(textfile: str):
    dataset = []
    data = ""

    # creates a word generator
    generator = word_generator(textfile)

    try:
        while True:
            # group into sets of 100
            for _ in range(100):
                data += " " + next(generator)
            dataset.append(data)
    except StopIteration:
        print("Document processed.")


# put into correct format
def categorize(sample, category):
    return [sample, category]


def vectorize(data):
    


    # use the dictvectorize?
    # https://scikit-learn.org/dev/modules/feature_extraction.html#common-vectorizer-usage
    # https://www.quora.com/What-are-the-ways-to-load-custom-dataset-for-scikit-learn-What-is-the-format-of-the-dataset-that-is-to-be-used-in-scikit-I-have-a-dataset-that-is-in-the-form-of-a-text-file
    # https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer
    pass

if __name__ == "__main__":

    pass

