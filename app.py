from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! I can edit in Github o_O"
