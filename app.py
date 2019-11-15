import os
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello JUNCTION!'


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key'
    )
    return app
