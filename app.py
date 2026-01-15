from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

def get_bot_reply(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! I am your CI/CD demo chatbot 🤖"
    elif "name" in msg:
        return "I am a chatbot running on Google Cloud Run."
    elif "help" in msg:
        return "Try saying: hello or what is your name"
    else:
        return "Sorry, I don't understand yet."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = get_bot_reply(user_msg)
    return jsonify({"reply": reply})

# Serve frontend
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
