from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return jsonify(content=data["content"], author=data["author"])
    except requests.RequestException:
        return jsonify(content="Failed to load quote. Try again later.", author="")

if __name__ == "__main__":
    app.run(debug=True)