from flask import jsonify
from flask import Flask
from flask_restful import Api
from flask_restful.representations.json import output_json

from app.data import entitlements
from app.dto import User
from app.resources import Hello, Restrict
from app.services import SmartEngine, AuthService
from app.services.rules import RulesEngine
from app.rules import (
    ContentRestriction,
    ApacContentRestriction,
)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.BaseConfig')


    @app.errorhandler(404)
    def not_found(error):
        data = {'code': 404, 'message': 'Resource not found'}
        return jsonify(data), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        data = {'code': 500, 'message': 'Internal Server error'}
        return jsonify(data), 500


    class Service(Api):
        def handle_error(self, e):
            # Attach the exception to itself so Flask-Restful's error handler
            # tries to render it.
            if not hasattr(e, 'data'):
                e.data = e
            return super().handle_error(e)


    api = Service(app)


    # @api.representation('application/json')
    # def json_ex(data, code, *args, **kwargs):
    #     if isinstance(data, Exception):
    #         data = {'code': code, 'message': str(data)}
    #     return output_json(data, code, *args, **kwargs)


    rules = [
        ContentRestriction(),
        ApacContentRestriction(),
    ]

    rules_engine = RulesEngine(rules)
    auth = AuthService()
    user = User(entitlements)

    engine = SmartEngine(rules_engine, user, auth)

    api.add_resource(Hello, '/')
    api.add_resource(Restrict, '/restrict', resource_class_kwargs={'engine': engine})

    return app
