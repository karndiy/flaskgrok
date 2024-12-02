from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.x.ai/v1/chat/completions"
API_KEY = "xai-RGRKtiOdWZPD1TL7Bv3FTofKZRSeagJ7S6ApIywoLtPSeqvfdZGtrMxlf5d4lCl3L1Jn4HEjamN473Pu"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call-api', methods=['POST'])
def call_api():
    user_message = request.json.get('user_message', '')
    
    # Prepare payload and headers for API request
    payload = {
        "messages": [
            {"role": "system", "content": "You are a test assistant."},
            {"role": "user", "content": user_message}
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # Make the API call
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
