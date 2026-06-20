from flask import Blueprint, render_template, request, redirect, url_for, session

from ..storage import USERS


auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = (request.form.get("username") or "").strip()
    password = (request.form.get("password") or "").strip()

    if USERS.get(username) and USERS[username] == password:
        session["user"] = username
        return redirect(url_for("admin"))

    return render_template("login.html", error="Identifiants invalides")


@auth_routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("reservation"))


def require_login(session_obj):
    return bool(session_obj.get("user"))

