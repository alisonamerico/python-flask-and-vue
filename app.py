# importing Flask e render_template
from flask import Flask, render_template

# creating instance of Flask
app = Flask(__name__)


# creating a route to main page and displaying the message 'Hello World'
@app.route('/')
def index():
    return render_template('index.html')


# creating a route to page about
@app.route('/about')
def about():
    return render_template('about.html')


# creating a route to page about
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
