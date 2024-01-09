from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return "<p>May the force be with you</p>"
