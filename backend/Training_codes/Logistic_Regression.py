import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import sklearn.externals
import joblib


import Preprocess

# on récupère les données
print("debut lecture données")
data = tweets = pd.read_csv('E:\\Documents\\Cours\\ENSA Deuxième Année Informatique\\2ème Semestre\\Projet de Semestre\\DataSet\\sentiment140.csv',encoding = "ISO-8859-1")

# on labélise les colonnes

data.columns=['sentiment','tweet_id','date','query','username','text']

'''
de base dans le dataset les sentiments positfs sont noté à 4 mais on va
changer cela en 1
'''
data.loc[data['sentiment']==4,'sentiment'] = 1

data = data[['text','sentiment']]

data = data.drop(data.index[200000:1400000])

data['tokens'] = data['text'].apply(Preprocess.process_tweet)

data['cleaned'] = data['tokens'].apply(Preprocess.rejoin_words)

# gets reviews column from df
reviews = data['cleaned'].values

# gets labels column from df
labels = data['sentiment'].values

'''
on va maintenant créer les données pour l'entrainemment et de test car sentiment140
n'as pas les deux. On va donc prélever une partie des données d'entrainement pour
faire les tests

on a 1.600.000 tweets. On va donc attribuer 320000 tweets pour les tests et donc
1.280.000 pour l'entrainement
'''

train_sentences, test_sentences, train_labels, test_labels = train_test_split(reviews, labels, test_size=0.2, random_state=42,
                 stratify=labels)

print("preprocess et division du dataset terminé")

'''
on va maintenant obtenir la fréquence des mots du vocabulaire
'''
# Uses Count vectorizer to get frequency of the words
vectorizer = CountVectorizer(max_features=7000)

train_sentences = vectorizer.fit_transform(train_sentences)
test_sentences = vectorizer.transform(test_sentences)

#enregistrer le counterVectorizer qui contient les données du vocabulaire
#joblib.dump(vectorizer, "vectorizer.pkl")

'''
création et entrainement du model
'''
print("debut entrainement")
Model = LogisticRegression(max_iter = 1000,solver='saga')
Model.fit(train_sentences, train_labels)
print("fin entrainement")

'''
enregistrement du model
'''
#joblib.dump(Model,"Model_LogiticRegression.pkl")
#print("enregistrement terminé")


'''
pour tester la perfomance du model
'''
#Model = joblib.load("Model_NBC.pkl")
#print("chargement du model terminé")
      
Model.score(test_sentences, test_labels)
print("----------",Model.score(test_sentences, test_labels),"--------")




      
