import pymongo
from pymongo import MongoClient
client = MongoClient()
import requests
import threading
import time

api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'

sequence_number = 0
def save_live_data(sequence_number):
    while True:
        #get or make a new database
        db = client.fraudEvents
        #get the events collection (table)
        events = db.events
        #get data from API
        response = requests.post(url, json={'api_key': api_key,
                                            'sequence_number': sequence_number})
        raw_data = response.json()
        if int(raw_data["_next_sequence_number"]) != sequence_number:
            events.insert_one(raw_data)
            sequence_number = int(raw_data["_next_sequence_number"])
        time.sleep(180)

save_live_data(sequence_number)