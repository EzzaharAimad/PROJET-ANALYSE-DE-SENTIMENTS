import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import sklearn.externals
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


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
on va maintenant obtenir la fréquence des mots
'''
# Uses Count vectorizer to get frequency of the words
vectorizer = CountVectorizer(max_features=7000)

train_sentences = vectorizer.fit_transform(train_sentences)
test_sentences = vectorizer.transform(test_sentences)

#enregistrer le counterVectorizer qui contient les données du vocabulaire
#joblib.dump(vectorizer, "vectorizer.pkl")

'''
création du model

print("debut entrainement")
#Model = MultinomialNB()
#Model.fit(train_sentences, train_labels)
Model = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
Model.fit(train_sentences, train_labels)
print("fin entrainement")


enregistrement du model
'''
#joblib.dump(Model,"Model_KNN.pkl")
print("enregistrement terminé")

'''
pour tester la perfomance du model
'''
Model = joblib.load("Model_KNN.pkl")

print("chargement du model terminé")
#Model.score(test_sentences, test_labels)
predictions = Model.predict(test_sentences)
print("----------",accuracy_score(predictions,test_labels),"--------")

#on va créer nous meme une fonction pour faire l'évaluation
'''def predict(tweets,labels):
    cpt=0
    for i in range(np.size(tweets)-1):
        tweet_clean = Preprocess.rejoin_words(Preprocess.process_tweet(tweets[i]))
        x=Model.predict(vectorizer.transform([tweet_clean]))
        if x[0]==labels[i]:
            cpt += 1
    acc = cpt/np.size(tweets)
    print("Accuracy : ",acc)


predict(test_sentences, test_labels)'''
