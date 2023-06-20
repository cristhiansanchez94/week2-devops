import random
import traceback 
import requests
from flask import Flask, render_template
from socket import gethostname, gethostbyname


app = Flask(__name__)


@app.route("/health")
def health():
    return "healthy"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_quote")
def quote():
    quote = ''
    for port in ['4999', '5000']:
        if quote == '':
            try:
                quote = requests.get(f"http://localhost:{port}/quote").text
            except Exception as e:
                print(traceback.format_exc())
                pass
    print("quote - ", quote)

    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
