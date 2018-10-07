# importing Flask e render_template
from flask import Flask, render_template, json

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


# creating a route to page contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


# creating a route to page test
@app.route('/test')
def test():
    my_dict = {"title": "Bayside", "genre": "Alternative"}
    return json.dumps(my_dict)


if __name__ == "__main__":
    app.run(debug=True)
