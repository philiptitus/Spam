import pandas as pd
import re
import nltk
import joblib
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Constants
MODEL_PATH = 'spam_classifier.joblib'
DATA_PATH = 'data/spam.csv'

# Download NLTK stopwords
nltk.download('stopwords', quiet=True)

def preprocess_text(text):
    """Preprocess the input text."""
    if not isinstance(text, str):
        return ""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]  # Apply stemming
    return " ".join(words)

def load_data():
    """Load and preprocess the dataset."""
    df = pd.read_csv(DATA_PATH, encoding='latin-1', usecols=[0, 1])
    df.columns = ["label", "message"]
    df['label'] = df['label'].map({'spam': 1, 'ham': 0})
    df['message'] = df['message'].apply(preprocess_text)
    return df

def train_model():
    """Train and save the spam classification model."""
    print("Training new model...")
    df = load_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label'], test_size=0.2, random_state=42
    )
    
    # Create and train pipeline
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB())
    ])
    
    pipeline.fit(X_train, y_train)
    
    # Evaluate
    y_pred = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
    # Save model
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    return pipeline

def load_model():
    """Load the pre-trained model or train a new one if not found."""
    if os.path.exists(MODEL_PATH):
        print("Loading pre-trained model...")
        return joblib.load(MODEL_PATH)
    return train_model()

class SpamClassifier:
    def __init__(self):
        self.model = load_model()
    
    def predict(self, text):
        """Predict if the input text is spam or not."""
        processed_text = preprocess_text(text)
        prediction = self.model.predict([processed_text])
        return "Spam" if prediction[0] == 1 else "Not Spam"

# For testing
if __name__ == "__main__":
    classifier = SpamClassifier()
    while True:
        email_text = input("\nEnter email text (or 'quit' to exit): ")
        if email_text.lower() == 'quit':
            break
        print("Prediction:", classifier.predict(email_text))