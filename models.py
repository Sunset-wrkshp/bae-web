from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from routes.py import app

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

#Model for the Patient information
class Patient(db.Model):
    __tablename__ = 'patients'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    age = db.Column(db.Integer)
    s_pulse = db.Column(db.Integer)
    e_pulse = db.Column(db.Integer)

    def __init__(self, firstname, lastname, age, s_pulse, e_pulse):
      self.firstname = firstname.title()
      self.lastname = lastname.title()
      self.age = age
      self.s_pulse = s_pulse
      self.e_pulse = e_pulse
