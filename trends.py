import basic_stat
import word_analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


def trends():
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

    f = open("stemmed.txt")
    words = f.read()
    words = words.split()
    for word in words:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)
    f = {}
    for w in pos_word_list:
        if w not in f:
            f[w] = 1
        else:
            f[w] += 1 
    pos = sorted(f, key=f.__getitem__, reverse=True)
    y = []
    for w in pos:
        y.append(f[w])
    n = min(len(pos), 10)
    plt.subplot(1, 2, 1)
    plt.barh(pos[:n], y[:n])
    plt.title('Positive Words contributing to sentiments')
    f = {}
    for w in neg_word_list:
        if w not in f:
            f[w] = 1
        else:
            f[w] += 1 
    neg = sorted(f, key=f.__getitem__, reverse=True)
    y = []
    for w in neg:
        y.append(f[w])
    n = min(len(neg), 10)
    plt.subplot(1, 2, 2)
    plt.barh(neg[:n], y[:n])
    plt.title('Negitive Words contributing to sentiments')
    plt.show()