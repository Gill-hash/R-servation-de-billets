import os


class Config:
    # Dev: secret statique (pour session). En prod: utiliser une variable d'environnement.
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

