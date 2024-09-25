from peewee import Model, DateTimeField, CharField, ForeignKeyField, IntegerField
from datetime import datetime
from .sqlite import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Query(BaseModel):
    user = ForeignKeyField(User, backref='queries')
    movie_name = CharField()
    timestamp = DateTimeField(default=datetime.now)

class Movie(BaseModel):
    title = CharField()  # Название фильма
    movie_id = IntegerField(unique=True)  # Уникальный ID фильма
    user = ForeignKeyField(User, backref='movies')  # Связь с пользователем

# Создание таблиц
db.connect()
db.create_tables([User, Query, Movie])