import basic_stat
import word_analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

def monogram_trends():
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


def get_plot(f, g, s):
    x = sorted(f, key=f.__getitem__, reverse=True)
    y = []
    for i in x:
        y.append(f[i])
    n = min(len(x), 10)
    plt.subplot(1, 2, 1)
    plt.title('Positive ' + s)
    plt.barh(x[:n], y[:n])
    x = sorted(g, key=g.__getitem__, reverse=True)
    y = []
    for i in x:
        y.append(g[i])
    n = min(len(x), 100)
    plt.subplot(1, 2, 2)
    plt.barh(x[:n], y[:n])
    plt.title('Negitive ' + s)
    plt.show()

def bigram_trends():
    f = open("stemmed.txt")
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    #Create your bigrams
    bgs = nltk.bigrams(tokens)
    #compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    pos = []
    neg = []
    sid = SentimentIntensityAnalyzer()    
    pos_bigrams=[]
    neg_bigrams=[]
    pf = {}
    nf = {}
    for key in fdist:
        bigram = key[0] + ' ' + key[1]
        if (sid.polarity_scores(bigram)['compound']) >= 0.5:
            if bigram not in pf:
                pf[bigram] = 1
            else:
                pf[bigram] += 1
        elif (sid.polarity_scores(bigram)['compound']) <= -0.5:
            if bigram not in nf:
                nf[bigram] = 1
            else:
                nf[bigram] += 1

    get_plot(pf, nf, 'Bigrams')

def trigram_trends():
    f = open("stemmed.txt")
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    #Create your trigrams
    bgs = nltk.trigrams(tokens)
    #compute frequency distribution for all the trigrams in the text
    fdist = nltk.FreqDist(bgs)
    pos = []
    neg = []
    sid = SentimentIntensityAnalyzer()    
    pos_trigrams=[]
    neg_trigrams=[]
    pf = {}
    nf = {}
    for key in fdist:
        trigram = key[0] + ' ' + key[1] + ' ' + key[2]
        if (sid.polarity_scores(trigram)['compound']) >= 0.5:
            if trigram not in pf:
                pf[trigram] = 1
            else:
                pf[trigram] += 1
        elif (sid.polarity_scores(trigram)['compound']) <= -0.5:
            if trigram not in nf:
                nf[trigram] = 1
            else:
                nf[trigram] += 1

    get_plot(pf, nf, 'Trigrams')


def trends():
    nltk.download('vader_lexicon')
    # monogram_trends()
    # bigram_trends()
    trigram_trends()
