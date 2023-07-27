from flask_security import UserMixin, RoleMixin
from application.database import db as db

roles_users = db.Table('roles_users',
    db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
    db.Column('role_id',db.Integer(),db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=0)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    todos = db.relationship('Todos', backref='user', cascade='all, delete', lazy=True)
    roles = db.relationship('Role',secondary='roles_users',backref=db.backref('users',lazy="dynamic"))

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task=db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))