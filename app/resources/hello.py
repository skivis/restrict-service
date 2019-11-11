from flask_restful import Resource


class Hello(Resource):

    def get(self) -> dict:
        return {'message': 'Service operational.'}
