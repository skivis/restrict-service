import os


class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False
    SECRET_KEY = '5d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
    JSONIFY_PRETTYPRINT_REGULAR = False
