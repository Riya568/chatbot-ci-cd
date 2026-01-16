from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower()

    # Simple chatbot logic
    if "hello" in user_msg:
        reply = "Hello! 😊 How can I help you?"
    elif "how are you" in user_msg:
        reply = "I’m doing great! Thanks for asking 💙"
    elif "name" in user_msg:
        reply = "I am your Cloud Run chatbot 🤖"
    elif "bye" in user_msg:
        reply = "Goodbye! Have a nice day 👋"
    else:
        reply = "Sorry, I didn’t understand that yet 😅"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    # Local run
    app.run(host="127.0.0.1", port=5000, debug=True)
