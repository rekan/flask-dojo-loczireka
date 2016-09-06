from flask import *
from peewee import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    hello = Random(text='Helloka')
    hello.save()
    return 'Hello world!'


database = PostgresqlDatabase('flask_app')
db.connect()
db.create_tables([Random])


class BaseModel(Model):
    class Meta:
        db = database


class Random(BaseModel):
    text = CharField()


app.run(debug=True)
