import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, jsonify
import pymongo
from pymongo import MongoClient
client = MongoClient()


with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")

content = []
db = client.fraudEvents

data = db.events.find().sort([('_id', pymongo.ASCENDING)]).limit(5)

for datum in data:
    temp = []
    temp.append(datum['data'][0]['country'])
    temp.append(datum['data'][0]['email_domain'])
    temp.append(datum['data'][0]['user_age'])
    prediction = model.predict_proba(datum)
    content.append(temp)

print('content: ' + str(content))

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html', 
                            country1 = content[0][0],
                            email1 = content[0][1],
                            age1 = content[0][2],
                            country2 = content[1][0],
                            email2 = content[1][1],
                            age2 = content[1][2],
                            country3 = content[2][0],
                            email3 = content[2][1],
                            age3 = content[2][2],
                            country4 = content[3][0],
                            email4 = content[3][1],
                            age4 = content[3][2],
                            country5 = content[4][0],
                            email5 = content[4][1],
                            age5 = content[4][2],  
                            probability1 = content[0][3]    
                            probability2 = content[1][3] 
                            probability3 = content[2][3] 
                            probability4 = content[3][3]   
                            probability5 = content[4][3]                                                                                                         
                            )


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    data = request.json
    prediction = model.predict_proba([data['user_input']])
    return jsonify({'probability': prediction[0][1]})





