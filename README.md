# Spam Detection Service

A machine learning-based spam detection service built with Flask, designed to be integrated with the Fiona email marketing platform. This service classifies incoming email content as either spam or ham (not spam) using a pre-trained machine learning model.

## Features

- **ML-Powered Classification**: Uses a trained model to detect spam with high accuracy
- **RESTful API**: Simple HTTP endpoints for easy integration
- **Fast Inference**: Optimized for quick response times
- **Scalable**: Designed to handle multiple concurrent requests

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- virtualenv (recommended)

## Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd spam
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Service

Start the Flask development server:
```bash
python app.py
```

The service will be available at `http://localhost:5000` by default.

### API Endpoints

#### Check if Content is Spam
```
POST /predict
Content-Type: application/json

{
    "message": "Your email content here..."
}
```

**Response:**
```json
{
    "is_spam": true,
    "confidence": 0.98,
    "message": "This message appears to be spam"
}
```

### Environment Variables

Create a `.env` file in the project root with the following variables:

```
FLASK_APP=app.py
FLASK_ENV=development  # or 'production' in production
PORT=5000
DEBUG=True  # Set to False in production
```

## Model Training

The spam detection model is pre-trained and saved as `spam_classifier.joblib`. To retrain the model:

1. Prepare your training data in the `data/` directory
2. Run the training script:
   ```bash
   python model.py
   ```

## Testing

Run the test script to verify the service is working:
```bash
python test.py
```

## Integration with Fiona

This service is designed to be integrated with the Fiona email marketing platform. The main Django application makes HTTP requests to this service to check outgoing emails for potential spam content before sending.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT LICENSE

## Support

For support, please contact me.
