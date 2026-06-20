# Placeholder: l'ancien backend n'avait pas de blueprint séparé 'event_routes'.
# La gestion des événements est faite dans admin_routes.

from flask import Blueprint


event_routes = Blueprint("event_routes", __name__)


def init_app(app):
    return


# Pour compatibilité (si jamais ton init_app appelle event_routes.init_app(app)).

