from flask import Flask, request
import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd
app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return f"The sum of {a} and {b} is {result}"

@app.route('/predict')
def predict():
    with open('diabetes_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    new_input = [[a, b, 72, 35, 0, 33.6, 0.627, 50]]
    prediction = loaded_model.predict(new_input)
    result = a + b
    return f"The sum of {a} and {b} is {prediction}"


if __name__ == '__main__':
    app.run()
