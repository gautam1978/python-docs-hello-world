from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Saurav new BCCI president and this is UAT env"
