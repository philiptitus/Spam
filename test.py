import requests
response = requests.post(
    'http://localhost:5000/predict',
    json={'message': 'URGENT! You have won a 1 week FREE!'}
)
print(response.json())