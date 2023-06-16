import heapq
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from collections import Counter


nltk.download("stopwords") # comment out if already downloaded


def bag_of_words(file_address, top_n = 0):
    """
    This function disregards the word order and grammar, focusing only on word occurrence.
    :param file_address: text file from which you want to create a bag of words
    :param top_n: Number of most frequent words You want this function to return
    :return: a list of top_n words (if top_n is given) or a counter of all words
    """
    english_stop_words = stopwords.words("english")
    stemmer = PorterStemmer()
    data = []
    with open(file_address, 'r') as handler:
        for line in handler.readlines():
            data.append(line.strip())
    data = " ".join(data)
    data = word_tokenize(data.lower())
    for word in data[:]:
        if len(word) <= 3 or word in english_stop_words:
            data.remove(word)
    for i in range(len(data)):
        if not data[i].endswith('e'):
            data[i] = stemmer.stem(data[i])
    data = Counter(data)
    if top_n == 0:
        return data
    else:
        data = heapq.nlargest(top_n, Counter(data), key=data.get)
        return data