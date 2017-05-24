from flask_sqlalchemy import SQLAlchemy

from . import app


db = SQLAlchemy(app)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hired_on = db.Column(db.DateTime, default=db.func.now())
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship(Department, backref=db.backref('employees', uselist=True, cascade='delete,all'))
