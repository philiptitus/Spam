# from flask import Flask, request, jsonify
# from model import SpamClassifier
# import os

# # Initialize Flask app
# app = Flask(__name__)

# # Configure for Vercel
# app.config['JSON_SORT_KEYS'] = False
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# # Initialize the classifier when the app starts
# classifier = SpamClassifier()

# @app.route('/')
# def home():
#     return "Welcome to the Spam Detection API! Use /predict endpoint with a POST request to check if a message is spam."

# @app.route('/predict', methods=['POST'])
# def predict():
#     """
#     Endpoint to predict if a message is spam or not.
#     Expected JSON payload: {"message": "your text here"}
#     """
#     try:
#         # Get JSON data from request
#         data = request.get_json(force=True)
        
#         # Check if message exists in the request
#         if 'message' not in data or not data['message'].strip():
#             return jsonify({
#                 'error': 'No message provided',
#                 'usage': 'Send a POST request with JSON body: {"message": "your text here"}'
#             }), 400
        
#         # Get prediction
#         text = data['message']
#         prediction = classifier.predict(text)
        
#         # Return the result
#         return jsonify({
#             'message': text,
#             'is_spam': prediction == 'Spam',
#             'prediction': prediction
#         })
        
#     except Exception as e:
#         return jsonify({
#             'error': str(e),
#             'usage': 'Send a POST request with JSON body: {"message": "your text here"}'
#         }), 500

# # This is required for Vercel to recognize your app
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# # This is the WSGI entry point that Vercel will use
# handler = app
import streamlit as st
from model import SpamClassifier

st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Spam Detection App")
st.write("Enter a message below to check if it’s spam or not.")

classifier = SpamClassifier()

# User input
user_input = st.text_area("Your message", placeholder="Type your message here...")

if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        prediction = classifier.predict(user_input)
        if prediction == "Spam":
            st.error("🚫 This message is likely spam!")
        else:
            st.success("✅ This message looks fine (Not Spam).")
