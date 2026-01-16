from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

def get_bot_reply(message):
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return "Hello! I am your CI/CD demo chatbot 🤖"
    elif "name" in msg:
        return "I am running on Google Cloud Run."
    else:
        return "Sorry, I don't understand yet."

# Frontend
@app.route("/")
def home():
    return render_template("index.html")

# API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"reply": get_bot_reply(data.get("message", ""))})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
