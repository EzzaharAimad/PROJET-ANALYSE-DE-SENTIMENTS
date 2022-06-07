import nltk, string, re, html

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

'''
première étape pré-traiter les tweets
'''

def remove_useless_things(tweet):

    #rendre tout les mots en minuscule
    tweet = str(tweet).lower()
    
    #retirer les retweets
    new_tweet = re.sub(r'^RT[\s]+','',tweet)

    #retier les username
    new_tweet = re.sub(r'^@\w*','',new_tweet)

    #retirer les liens
    new_tweet = re.sub(r'https?:\/\/\w*\.\w*','',new_tweet)

    #retirer # devant les hashtags
    new_tweet = re.sub(r'#','',new_tweet)

    #retirer les lettres qui se trouvent après les apostrophes
    new_tweet = re.sub(r'\'.*?\s',' ', new_tweet)

    #retirer les mots qui ont des caractères non alphanumérics
    #new_tweet = re.sub(r'[a-zA-Z0-9]*[^a-zA-Z0-9][^a-zA-Z0-9]*',' ',new_tweet)

    return html.unescape(new_tweet)

'''
tokeniser les tweets c'est à dire diviser chaque élément de la phrase en mots
'''
def tokenize_tweet(tweet):
    tweet_tokens = nltk.tokenize.word_tokenize(tweet)

    return tweet_tokens

'''
retirer les stops-words c'est-à-dire des mots inutiles passe partout et couramment
utilisé qui n'apportent aucun sens en plus à la phrase
'''

stops_en = set(stopwords.words('english'))
stops_fr = set(stopwords.words('french'))
punctuations = string.punctuation

def remove_stops(tweet_tokens):

    tweet_meaningful = []

    for word in tweet_tokens:
        if(word not in stops_en and word not in punctuations):
            out = ''.join([i for i in word if i not in punctuations])
            tweet_meaningful.append(out)

    return tweet_meaningful


'''
on va maintenant appliquer la lemmatization aux tokens
le stemming aussi fait la meme chose et est plus rapide mais dans certains
cas la lemmatization est plus précise et donne des résultats plus corrects
linguistiquement
'''

lemmatizer = WordNetLemmatizer()

def lemmatizing(tokens):
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]    
    #lemmatizing is performed. It's more efficient than stemming.
    return (lemmatized_tokens)


# on va maintenant combiner le tout dans une seule fonction
def process_tweet(tweet):
    pre_tweet = remove_useless_things(tweet)
    tweet_tokens = tokenize_tweet(pre_tweet)
    tweet_meaningful = remove_stops(tweet_tokens)
    tweet_clean = lemmatizing(tweet_meaningful)

    return " ".join(tweet_clean)

