from flask import Flask

from .routes import auth_routes, event_routes, booking_routes, admin_routes
from .config import Config


def create_app():
    app = Flask(__name__)

    # Flask recherche les templates dans app/templates/
    app.template_folder = "templates"

    app.config.from_object(Config)

    auth_routes.init_app(app)
    event_routes.init_app(app)
    booking_routes.init_app(app)
    admin_routes.init_app(app)

    return app

