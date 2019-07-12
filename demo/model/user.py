from flask_restful import fields

from demo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cellphone = db.Column(db.String(20), index=True, unique=True)


user_fields = {
    'id': fields.Integer,
    'name': fields.String
}