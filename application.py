from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    text = """<!DOCTYPE html>
    <html>
        <head>
            <title>Witaj świecie, BigData z Pythionem!</title>
        </head>
        <body>
            <h1>Witaj świecie, BigData z Pythionem!</h1>
            <p>Procesy CI/CD - automatyczne wdrażąnie.</p>
            <p>Wykonał: Bartosz Bryniarski</p>
        </body>
    </html>
    """
    return(text)


if __name__ == "__main__":
    application.run(debug=True)