from flask import Blueprint, jsonify, request
from app.models.room_type import RoomType
from app.database import db

room_type_blueprint = Blueprint("room_type", __name__, url_prefix="/room_type")

@room_type_blueprint.route("/create", methods=["POST"])
def create():
    room_type = request.json["room_type"]
    price_per_night = request.json["price_per_night"]

    new_room_type = RoomType(room_type=room_type, price_per_night=price_per_night)

    db.session.add(new_room_type)
    db.session.commit()

    return jsonify(new_room_type.serialize()), 201

@room_type_blueprint.route("/<string:room_type>", methods=["GET"])
def get_room_type(room_type):
    room_type = RoomType.query.filter_by(room_type=room_type).first()
    if room_type is None:
        return "Room type not found", 404
    
    return jsonify(room_type.serialize()), 200

@room_type_blueprint.route("/all", methods=["GET"])
def get_all():
    room_types = RoomType.query.all()
    room_types = list(map(lambda room_type: room_type.serialize(), room_types))

    return jsonify(room_types), 200

@room_type_blueprint.route("/<string:room_type>", methods=["PUT"])
def update(room_type):
    room_type = RoomType.query.filter_by(room_type=room_type).first()
    if room_type is None:
        return "Room type not found", 404

    room_type.price_per_night = request.json["price_per_night"]

    db.session.commit()

    return jsonify(room_type.serialize()), 200

@room_type_blueprint.route("/<string:room_type>", methods=["DELETE"])
def delete(room_type):
    room_type = RoomType.query.filter_by(room_type=room_type).first()
    if room_type is None:
        return "Room type not found", 404

    db.session.delete(room_type)
    db.session.commit()

    return jsonify(room_type), 204

@room_type_blueprint.route("/<string:room_type>/rooms", methods=["GET"])
def get_rooms_by_room_type(room_type):
    room_type = RoomType.query.filter_by(room_type=room_type).first()
    if room_type is None:
        return "Room type not found", 404

    return jsonify([room.serialize() for room in room_type.rooms]), 200
