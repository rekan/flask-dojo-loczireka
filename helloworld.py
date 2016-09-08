from flask import *
from peewee import *

db = PostgresqlDatabase('flask_app')


class BaseModel(Model):
    class Meta:
        database = db


class Random(BaseModel):
    count = IntegerField(null=True)
