from flask_script import Server
from flask_script import Manager

from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command('runserver', Server(port=5000, use_reloader=True))

if __name__ == '__main__':
    manager.run()
