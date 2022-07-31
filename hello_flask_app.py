from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

config = dotenv_values()

app = Flask(__name__)

DB_URI = config['DB_SERVER'] + '://' + config['USER'] + ':' + config['PASSWORD'] + \
    '@' + config['DB_IP'] + ':' + config['DB_PORT'] + '/' + config['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
