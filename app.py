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
import requests
import threading
import time



api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'



with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")


def save_live_data():
    while True:
        #get or make a new database
        db = client.fraudEvents
        #get the events collection (table)
        events = db.events
        #get data from API
        sequence_number = 0
        response = requests.post(url, json={'api_key': api_key,
                                            'sequence_number': sequence_number})
        raw_data = response.json()
        events.insert_one(raw_data)
        time.sleep(180)

save_live_data()


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

