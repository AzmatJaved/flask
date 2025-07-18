# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model
model = joblib.load("iris_model.pkl")

# Start Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "🌸 Iris Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port = 9000,debug=True)
