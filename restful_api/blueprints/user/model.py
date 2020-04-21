from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

#Base = declarative_base()

class Users(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(30), unique=True, nullable=False)
	age = db.Column(db.Integer, nullable=True, default=20)
	sex = db.Column(db.String(10), nullable=False)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
	updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
	deleted_at = db.Column(db.DateTime)
	rents = db.relationship('Rents', backref='user', lazy=True) 

	response_field = {
		'id':fields.Integer,
		'name': fields.String,
		'age': fields.Integer,
		'sex': fields.String,
		'client_id': fields.Integer
	}

	def __init__(self, name, age, sex, client_id):
		self.name = name
		self.age = age
		self.sex = sex
		self.client_id = client_id

	def __repr__(self):
		return '<User %r>' % self.id