from __future__ import annotations

from flask import Flask
from flask_db_play import home


def create_app(test_config: dict[str, str | bool]) -> Flask:
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    app.register_blueprint(home.bp, url_prefix="/home")

    return app
