from graphene import ObjectType, String, Boolean, ID, List, Field, Int, Mutation, InputObjectType
import requests
import json
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


class User(ObjectType):
    id = Int()
    email = String()
    active = Boolean()


class Query(ObjectType):
    all_users = List(User)
    user = Field(User, id=Int())

    def resolve_all_users(self, info):
        response = requests.get('http://users:5000/users')
        return json2obj(json.dumps(response.json()['data']['users']))

    def resolve_user(self, info, id):
        response = requests.get(f'http://users:5000/users/{id}')
        print(response.json())
        return json2obj(json.dumps(response.json()['data']))
