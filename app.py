# importing Flask
from flask import Flask

# creating instance of Flask
app = Flask(__name__)


# creating a route to main page and displaying the message 'Hello World'
@app.route('/')
def index():
    return 'Hello World!'


# creating a route to page about
@app.route('/about')
def about():
    return 'Hi my name is Alison!'
