from flask_restful import Resource, reqparse, marshal_with

from demo import db, log
from demo.model.user import User, user_fields
from .util import api


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        u = User.query.get(user_id)
        log.debug('get user %s' % u)
        return u

    def delete(self, user_id):
        u = User.query.get(user_id)
        db.session.remove(u)
        db.session.commit()
        return 'ok'


api.add_resource(UserResource, '/api/user/<user_id>')


class UserList(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('name', type=str, required=True)
    parse.add_argument('cellphone', type=str, required=True)

    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args = self.parse.parse_args()
        u = User(
            name=args['name'],
            cellphone=args['cellphone']
        )

        db.session.add(u)
        db.session.commit()
        return u


api.add_resource(UserList, '/api/users')
