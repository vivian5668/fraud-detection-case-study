from browser import document, ajax
import json


import time
import math
import datetime

import browser.timer

def on_complete(req):
    if req.status==200 or req.status==0:
        document["result"].html = req.text
    else:
        document["result"].html = "error " + req.text

def get_prediction(ev):
    """Get the predicted probability."""
    req = ajax.ajax()
    req.bind('complete', on_complete)
    req.open('POST', '/predict', True)
    req.set_header('content-type','application/json')
    data = json.dumps({'user_input': document['user_input'].value})
    req.send(data)

document["predict_button"].bind("click", get_prediction)








