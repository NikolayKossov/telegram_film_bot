from peewee import Model, DateTimeField, AutoField
import datetime
from .sqlite import db

class BaseModel(Model):
    class Meta:
        database = db

class Request(BaseModel):
    id = AutoField()
    timestamp = DateTimeField(default=datetime.datetime.now)
