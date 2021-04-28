from flask import Flask, current_app, request
from config import config


def create_app(app_config='development'):
    app = Flask(__name__)


    app.config.from_object(config[app_config])

    from app.main.main import main as main_bp

    app.register_blueprint(main_bp)

    return app