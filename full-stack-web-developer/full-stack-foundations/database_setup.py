#!/usr/bin/env python
#
# database_setup.py -- Setup SQLAlchemy with SQLite database.

import os
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sys


Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    price = Column(String(8))
    course = Column(String(25))
    description = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
