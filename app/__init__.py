import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# def create_app(config_file='setting.py'):
def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Application Configuration
    # app.config.from_object('config.Config')

    # Initialize Plugins
    app.config['SQLALCHEMY_DATABASE_URI'] = 'squite:///db.sqlite'

    db.init_app(app)
    # db = SQLAlchemy(app)

    with app.app_context():
        from .auth import auth_bp
        app.register_blueprint(auth_bp)

        from .routes import main_bp
        app.register_blueprint(main_bp)

        return app