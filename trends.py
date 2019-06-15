import basic_stat
import word_analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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
    plt.subplot(2, 1, 1)
    plt.title('Positive ' + s)
    plt.barh(x[:n], y[:n])
    # plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    x = sorted(g, key=g.__getitem__, reverse=True)
    y = []
    for i in x:
        y.append(g[i])
    n = min(len(x), 10)
    plt.subplot(2, 1, 2)
    plt.barh(x[:n], y[:n])
    # plt.xticks(x[:n], rotation='vertical')
    plt.title('Negitive ' + s)
    plt.show()

def bigram_trends():
    f = open("filtered.txt")
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
    f = open("filtered.txt")
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


def ngram_with_neg(n, s1):
    n += 1
    f = open('filtered.txt')
    words = f.read()
    ng = nltk.ngrams(words.split(), n)
    f = {}
    sid = SentimentIntensityAnalyzer()
    for g in ng:
        s = ""
        for i in range(1, n):
            s += (g[i] + ' ')
        s = s[:len(s) - 1]
        if (sid.polarity_scores(g[0])['compound']) <= -0.5:
            if s not in f:
                f[s] = 1
            else:
                f[s] += 1
    x = sorted(f, key=f.__getitem__, reverse=True)
    y = []
    for i in x:
        y.append(f[i])
    n = min(len(x), 10)
    plt.title(s1 + ' preceded with negative words')
    plt.barh(x[:n], y[:n])
    plt.show()


def sentiment_score(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return score['compound']

def best_review():
    f = open("filtered.txt")
    s_reviews = f.read()
    s_reviews = s_reviews.split('\n')
    best_score = -float('inf')
    best_rev = ""
    f = open("reviews.txt")
    reviews = f.read()
    reviews = reviews.split('\n')
    for i in range(len(s_reviews)):
        score = sentiment_score(s_reviews[i])
        if score > best_score:
            best_rev, best_score = reviews[i], score
    print("Best Review(score = {}): ".format(best_score), best_rev)

def worst_review():
    f = open("filtered.txt")
    s_reviews = f.read()
    s_reviews = s_reviews.split('\n')
    worst_score = float('inf')
    worst_rev = ""
    f = open("reviews.txt")
    reviews = f.read()
    reviews = reviews.split('\n')
    for i in range(len(s_reviews)):
        score = sentiment_score(s_reviews[i])
        if score < worst_score:
            worst_rev, worst_score = reviews[i], score
    print("Worst Review(score = {}): ".format(worst_score), worst_rev)

def trends():
    # nltk.download('vader_lexicon')
    # monogram_trends()
    # bigram_trends()
    # trigram_trends()
    # ngram_with_neg(2, 'Bigrams')
    ngram_with_neg(3, 'Trigrams')
    # best_review()
    # worst_review()

