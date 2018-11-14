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

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    data = request.json
    prediction = model.predict_proba([data['user_input']])
    return jsonify({'probability': prediction[0][1]})

# def update_live_stream():
#     db = client.fraudEvents
#     events = db.events
#     record = events.find_one({"_next_sequence_number" : 1485})
#     print(record)
#     document["data_stream"].html = record['data'][0]['country']

# document["get_new_data"].bind("click", update_live_stream)

