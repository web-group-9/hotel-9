from flask import Blueprint, jsonify, request
from app.models.guest import Guest
from app.database import db

guest_blueprint = Blueprint("guest", __name__, url_prefix="/guest")

@guest_blueprint.route("/create", methods=["POST"])
def create():
    guest_name = request.json["guest_name"]
    contact_info = request.json["contact_info"]

    new_guest = Guest(guest_name=guest_name, contact_info=contact_info)

    db.session.add(new_guest)
    db.session.commit()

    return jsonify(new_guest.serialize()), 201

@guest_blueprint.route("/<int:guest_id>", methods=["GET"])
def get_user(guest_id):
    guest = Guest.query.filter_by(guest_id=guest_id).first()
    if guest is None:
        return "Guest not found", 404
    

    return jsonify(guest.serialize()), 200

@guest_blueprint.route("/all", methods=["GET"])
def get_all():
    guests = Guest.query.all()
    guests = list(map(lambda guest: guest.serialize(), guests))

    return jsonify(guests), 200

@guest_blueprint.route("/<int:guest_id>", methods=["PUT"])
def update(guest_id):
    guest = Guest.query.filter_by(guest_id=guest_id).first()
    if guest is None:
        return "Guest not found", 404

    guest.guest_name = request.json["guest_name"]
    guest.contact_info = request.json["contact_info"]

    db.session.commit()

    return jsonify(guest.serialize()), 200


@guest_blueprint.route("/<int:guest_id>", methods=["DELETE"])
def delete(guest_id):
    guest = Guest.query.filter_by(guest_id=guest_id).first()
    if guest is None:
        return "Guest not found", 404

    db.session.delete(guest)
    db.session.commit()

    return jsonify(guest), 204