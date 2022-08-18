import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class UserLogin(Base):
    __tablename__ = 'user_login'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

def serialize(self):
        return {
            "id": self.id,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "person_id": self.person_id,
            
            # do not serialize the password, its a security breach
        }

class UserLogOut(Base):
    __tablename__ = 'user_logOut'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

def serialize(self):
        return {
            "id": self.id,
            "email_address": self.email_address,
            "user_name": self.user_name,
            "person_id": self.person_id,
            
            # do not serialize the password, its a security breach
        }
class Gender(Base):
    __tablename__ = "gender"
    id = Column(Integer, primary_key=True)
    male = Column(String(120), nullable=False)
    female = Column(String(120), nullable=False)
    other = Column(String(120), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))



def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

  

