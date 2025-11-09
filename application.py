import os
import random
from datetime import datetime
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

    if ENV == 'dev':
        text += "<style>body { background-color: red; }</style>"

    return(text)

@application.route('/json')
def get_json():
    return jsonify({"FLASK_ENV": ENV})


@application.route('/weather/<station_id>')
def get_wheater_simple(station_id):
    return jsonify({
        "station_id": station_id,
        "temperature": random.uniform(-15, 45),
        "humidity": random.uniform(40, 90),
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    application.run(debug=True)