from flask import Flask, current_app, request
import sqlalchemy
from config import config
from flask import Blueprint

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.main import main
    app.register_blueprint(main)

    from app.auth.auth import auth
    app.register_blueprint(auth)
    return app