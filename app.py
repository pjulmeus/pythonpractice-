from flask import Flask 

app = Flask(__name__)

@app.route('/')
def homepag():
    return "homepage"

@app.route('/hello')
def say_hello():
    return "Hello there!"

@app.route('/goodbye')
def say_goodbye():
    return "Goodbye Losers"