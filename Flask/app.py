from flask import Flask, jsonify, render_template
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start': '1',
      'limit': '5000',
      'convert': 'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',  # Use your actual API key here
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return jsonify(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
