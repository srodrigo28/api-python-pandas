from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Home Site </h1>' 

app.run()