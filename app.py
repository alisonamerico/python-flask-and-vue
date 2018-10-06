# importing Flask
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
>>>>>>> template added

# creating instance of Flask
app = Flask(__name__)


# creating a route to main page and displaying the message 'Hello World'
@app.route('/')
def index():
<<<<<<< HEAD
    return 'Hello World!'
=======
    return render_template('templates/index.html')
>>>>>>> template added


# creating a route to page about
@app.route('/about')
def about():
    return 'Hi my name is Alison!'
<<<<<<< HEAD
=======


if __name__ == "__main__":
    app.run()
>>>>>>> template added
