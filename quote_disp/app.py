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
    base_url = 'week2-devops-web1-id'
    for id in [1,2]:
        url = base_url.replace('id',str(id))
        try: 
            response = requests.get(f"http://{url}:5000/quote")
            if response.status_code==200:
                quote = response.text
                break
        except Exception as e:
                pass
    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
