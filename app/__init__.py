from flask import Flask, current_app, request
from config import config
from flask import Blueprint



def create_app(app_config='development'):
    app = Flask(__name__)


    app.config.from_object(config[app_config])

    from app.main.main import main
    app.register_blueprint(main)

    from app.auth.auth import auth
    app.register_blueprint(auth)
    return app