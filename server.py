from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_messages = request.json.get("messages", [])
        payload = {
            "model": "x-ai/grok-4-fast:free",
            "messages": user_messages
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "Flask Chatbot"
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
