from flask_login import UserMixin

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import db


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(40))
    city = db.Column(db.Integer, db.ForeignKey("cities.id"))


class Cities(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(30), unique=True)


class Citizen_ideas(db.Model):
    __tablename__ = "citizen_ideas"

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime)
    citizen = db.Column(db.Integer, db.ForeignKey("users.id"))
    idea_name = db.Column(db.String(100), unique=True)
    idea_description = db.Column(db.String(500))
    files_path = db.Column(db.String(100))
