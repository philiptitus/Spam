from flask import Flask, request, jsonify
from model import SpamClassifier
import os

app = Flask(__name__)

# Initialize the classifier when the app starts
classifier = SpamClassifier()

@app.route('/')
def home():
    return "Welcome to the Spam Detection API! Use /predict endpoint with a POST request to check if a message is spam."

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict if a message is spam or not.
    Expected JSON payload: {"message": "your text here"}
    """
    try:
        # Get JSON data from request
        data = request.get_json(force=True)
        
        # Check if message exists in the request
        if 'message' not in data or not data['message'].strip():
            return jsonify({
                'error': 'No message provided',
                'usage': 'Send a POST request with JSON body: {"message": "your text here"}'
            }), 400
        
        # Get prediction
        text = data['message']
        prediction = classifier.predict(text)
        
        # Return the result
        return jsonify({
            'message': text,
            'is_spam': prediction == 'Spam',
            'prediction': prediction
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'usage': 'Send a POST request with JSON body: {"message": "your text here"}'
        }), 500

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
