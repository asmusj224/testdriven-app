from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models import User


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


class UserList(Resource):
    def post(self):
        post_data = request.get_json()
        response = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response, 400
        email = post_data.get('email')
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(User(email=email))
                db.session.commit()
                response['status'] = 'success'
                response['message'] = f'{email} was added!'
                return response, 201
            else:
                response['message'] = 'Sorry. That email already exists.'
                return response, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response, 400

    def get(self):
        response = {
            'status': 'success',
            'data': {
                'users': [user.to_json() for user in User.query.all()]
            }
        }
        return response, 200


class Users(Resource):
    def get(self, user_id):
        response = {
            'status': 'fail',
            'message': 'User does not exist'
        }
        try:
            user = User.query.filter_by(id=user_id).first()
            if not user:
                return response, 404
            else:
                response = {
                    'status': 'success',
                    'data': {
                        'id': user.id,
                        'email': user.email,
                        'active': user.active
                    }
                }
                return response, 200
        except ValueError:
            return response, 404


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UserList, '/users')
api.add_resource(Users, '/users/<user_id>')
