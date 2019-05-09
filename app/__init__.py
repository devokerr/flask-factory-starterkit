import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)
    app.config.update()
    db.app = app
    db.init_app(app)
    migrate.db = db
    migrate.init_app(app)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    with app.app_context():
        from app.blueprints import user_blueprint
        db.create_all()

        return app
