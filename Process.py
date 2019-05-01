import re
from collections import defaultdict
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
    split_pattern = re.compile('[\s?.!;:\-(),\\\]')

    for line in f:
        words = (w for w in split_pattern.split(line) if w)
        for w in words:
            yield w


# TODO: do not currently use a dictVector
def tokens(doc):
    """Extract tokens from doc.

    This uses a simple regex to break strings into tokens. For a more
    principled approach, see CountVectorizer or TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))


# TODO: do not currently use a dictVector
def token_freqs(doc):
    """Extract a dict mapping tokens from doc to their frequencies."""
    freq = defaultdict(int)
    for tok in tokens(doc):
        freq[tok] += 1
    return freq


# split into sets of 100
def vectorize(textfile: str):
    vec = CountVectorizer()
    # vectorizer = DictVectorizer()

    dataset = []
    data = ""

    # creates a word generator
    generator = word_generator(textfile)

    try:
        while True:
            # group into sets of 100
            for _ in range(100):
                data += " " + next(generator)
            dataset.append([data])
    except StopIteration:
        print("Document processed.")

    for data in dataset:
        x = vec.fit_transform(data).toarray()
        print(x)

    # https: // scikit - learn.org / stable / tutorial / text_analytics / working_with_text_data.html
    # TODO: you're at the tokenizing text part

    return vec


# put into correct format
def categorize(sample, category):
    return [sample, category]


if __name__ == "__main__":
    data = vectorize("test.txt")

    pass

