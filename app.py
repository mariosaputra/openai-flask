from flask import Flask, request, jsonify
from dotenv import load_dotenv

import requests
import os
import json

load_dotenv()

app = Flask(__name__)

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
    "Content-Type": "application/json"
}

@app.route('/query', methods=['POST'])
def query_openai():

    data = request.json
    response = requests.post(OPENAI_API_URL, headers=HEADERS, json=data)
    openai_response = response.json()
    message = openai_response['choices'][0]['message']['content']
    return jsonify({
        'message': message
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)