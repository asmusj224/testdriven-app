import json
import unittest

from project.tests.base import BaseTestCase

from project import db
from project.api.models import User


def add_user(email):
    user = User(email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):
    def test_users(self):
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'test@test.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('test@test.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'test': 'test@test.com'}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'test@test.com'
                }),
                content_type='application/json'
            )

            response = self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'test@test.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        user = add_user('test@test.org')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('test@test.org', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_invalid_id(self):
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        add_user('test@test.com')
        add_user('test1@test.com')

        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('test@test.com', data['data']['users'][0]['email'])
            self.assertIn('test1@test.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
