import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # simple bot reply
    reply = f"You said: {user_msg}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    # Cloud Run provides PORT env variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
