from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

threshold = 6  

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    pH = float(request.form['pH'])
    alcohol = float(request.form['alcohol'])
    
    
    if pH < 5 and 7 <= alcohol <= 10:
        predicted_quality = 'good'
    else:
        predicted_quality = 'bad'

    return render_template('home.html', prediction_text=f'Predicted Wine Quality: {predicted_quality}')

if __name__ == "__main__":
    app.run(debug=True)
