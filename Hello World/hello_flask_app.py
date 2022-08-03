from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

config = dotenv_values()

app = Flask(__name__)

DB_URI = config['DB_SERVER'] + '://' + config['USER'] + ':' + config['PASSWORD'] + \
    '@' + config['DB_IP'] + ':' + config['DB_PORT'] + '/' + config['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Person {self.id}, {self.name}>'


db.create_all()

# newPerson = Person(name="Mantis")
# db.session.add(newPerson)
# db.session.commit()


@app.route('/')
def index():
    person = Person.query.first()
    return "Hello " + person.name


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
