import os
from flask import Flask, jsonify

application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

@application.route('/')
def hello_world():
    text = """<!DOCTYPE html>
    <html>
        <head>
            <title>Witaj świecie, BigData z Pythionem!</title>
        </head>
        <body>
            <h1>Hello world! BigData z Pythionem!</h1>
            <p>Procesy CI/CD - automatyczne wdrażąnie.</p>
            <p>Wykonał: Bartosz Bryniarski</p>
        </body>
    </html>
    """
    return(text)

@application.route('/json')
def get_json():
    return jsonify({"FLASK_ENV": ENV})


if __name__ == "__main__":
    application.run(debug=True)