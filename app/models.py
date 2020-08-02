from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id', ondelete='CASCADE'), nullable=False)


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'{self.id}) {self.name}'
