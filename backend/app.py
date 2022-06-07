import sklearn.externals
import joblib
from flask import Flask, jsonify, request
from flask_cors import CORS

import Preprocess
import Getter


Vectorizer = joblib.load("Vocabulary/vectorizer.pkl")
HOST = '0.0.0.0'
PORT = 8081


app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/api/analyse', methods = ['GET','POST'])
def analyse():
    #recupérer les informations de la requête
    req = request.get_json()

    #chargement du modèle
    if req['model'] == 'Support Vector Machine (SVM)':
        Model = joblib.load("Models/Model_SVM.pkl")
    elif req['model'] == 'Logistic Regression':
        Model = joblib.load("Models/Model_LogiticRegression.pkl")
    elif req['model'] == 'Naives Bayes':
        Model = joblib.load("Models/Model_NBC.pkl")

    #parametre pour la recherche
    date_debut = req['start_date']
    date_fin = req['end_date']
    keywords = req['keywords']
    limit = 50 # le nombre de tweets à récupérer à chaque analyse

    tweet_df = Getter.get_tweets(keywords,date_debut,date_fin,limit)

    #creation d'une colonne contenant les tweets prétraités

    tweet_df['tweet_cleaned'] = tweet_df['tweet'].apply(Preprocess.process_tweet)

    #transformation des tweets en vecteurs et application du modèle
    tweet_df['predicted_sentiment'] = None
    for i in tweet_df.index:
        tweet_df['predicted_sentiment'][i] = Model.predict(Vectorizer.transform([tweet_df['tweet_cleaned'][i]]))[0]

    positive_at_count = tweet_df.loc[tweet_df['predicted_sentiment'] == 1]['predicted_sentiment'].count()
    negative_at_count = tweet_df.loc[tweet_df['predicted_sentiment'] == 0]['predicted_sentiment'].count()
    
    return jsonify([{'name':'positive','value':int(positive_at_count)},
                    {'name':'negative','value':int(negative_at_count)}])
    '''return jsonify([{'name': 'positive', 'value': 10},
                    {'name': 'negative', 'value': 10}])'''

'''@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404'''

if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
