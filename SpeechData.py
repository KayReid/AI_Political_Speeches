# learn from... https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

from sklearn.naive_bayes import MultinomialNB
import numpy as np
from Processing import *

# these are the two speakers
speakers = {0: 'clinton', 1: 'trump'}

# get the data into np arrays
clinton_x = data_writer('clinton.txt')
clinton_y = generate_y(0, clinton_x)
trump_x = data_writer('trump.txt')
trump_y = generate_y(1, trump_x)

# combine data sets
speeches_x = combine(clinton_x, trump_x)
speeches_y = combine(clinton_y, trump_y)
# print(len(clinton_x))
# print(len(trump_x))

# get count vector and Tfidf transformer
vec, vect = vectorize(speeches_x)

# split data (50-50)
train_x = speeches_x[::2]
test_x = speeches_x[1::2]

train_y = speeches_y[::2]
test_y = speeches_y[1::2]

# train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(vect, speeches_y)

# estimate its accuracy
test_x = vec.transform(test_x)

predicted = clf.predict(test_x)

print("Prediction ratio:", np.mean(predicted == test_y))

# try a different split (80-20)
tx = []
ty = []
txt = []
tyt = []
for i in range(len(speeches_x)):
    if i % 5 == 0:
        txt.append(speeches_x[i])
        tyt.append(speeches_y[i])
    else:
        tx.append(speeches_x[i])
        ty.append(speeches_y[i])

# estimate its accuracy
txt = vec.transform(txt)
predicted = clf.predict(txt)

print(vect.shape)

# print most popular words
freq_words(vec, vect, 10)

# print("Prediction ratio 2:", np.mean(predicted == tyt))
