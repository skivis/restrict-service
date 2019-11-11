from flask import Request
from flask_restful import Resource


class Restrict(Resource):
    def __init__(self, **kwargs):
        self.engine = kwargs['engine']

    def post(self, request: Request) -> list:
        print('hello')
        token = request.headers['Authorization']
        user = request.args.get('user')
        documents = request.get_json(force=True)
        return self.engine.apply_restrictions(documents, token)
