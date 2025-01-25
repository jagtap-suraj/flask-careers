# Import the Flask class from the flask module
from flask import Flask, render_template

# Create a new instance of the Flask class
app = Flask(__name__, template_folder='./template')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
