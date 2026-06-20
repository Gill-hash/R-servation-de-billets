from flask import Blueprint, render_template, request

from ..storage import create_reservation


booking_routes = Blueprint("booking_routes", __name__)


@booking_routes.route("/", methods=["GET"])
def reservation():
    return render_template("reservation.html")


@booking_routes.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "GET":
        return render_template("reservation.html")

    form = request.form

    try:
        booking = create_reservation(form)
        return render_template("result.html", booking=booking)
    except ValueError as e:
        # e.args[0] = list of errors
        errors = e.args[0] if e.args else ["Données invalides"]

        event_name = (form.get("event") or "").strip()
        name = (form.get("name") or "").strip()
        email = (form.get("email") or "").strip()
        payment = (form.get("payment") or "").strip()
        places = 0
        try:
            places = int(form.get("places") or 0)
        except Exception:
            places = 0

        booking = {
            "event": event_name,
            "name": name,
            "email": email,
            "payment": payment,
            "places": places,
            "errors": errors,
        }
        return render_template("result.html", booking=booking)

