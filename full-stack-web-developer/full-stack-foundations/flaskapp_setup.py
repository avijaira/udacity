#!/usr/bin/env python
#
# flaskapp_setup.py
# Setup a Flask app with Flask-SQLAlchemy and SQLite database.

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


"""Create a Flask application (app), load the config of choice, and then
create the SQLAlchemy object (db) by passing it the application.
"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


"""The SQLAlchemy object (db) contains all the functions and helpers
from both sqlalchemy and sqlalchemy.orm. Furthermore it provides a class
called Model that is a declarative base which can be used to declare
models.
"""

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Restaurant %r>' % self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(25))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant)

    def __init__(self, name, description, price, course, restaurant):
        self.name = name
        self.description = description
        self.price = price
        self.course = course
        self.restaurant = restaurant

    def __repr__(self):
        return '<MenuItem %r>' % self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course,
        }


"""Create the tables and database.
"""
db.create_all()
