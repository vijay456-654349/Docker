# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:12:29 2021

@author: DELL
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger,swag_from

app = Flask(__name__)
Swagger(app)

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return"welcome all"
    
@app.route('/predict')
def predict_note_authentication():
    
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "Hello The answer is"+str(prediction)


if __name__=='__main__':
    app.run()