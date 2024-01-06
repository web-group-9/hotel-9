from flask import Blueprint, jsonify, request
from app.models.room import Room
from app.database import db

room_blueprint = Blueprint("room", __name__, url_prefix="/room")

@room_blueprint.route("/create", methods=["POST"])
def create():
    room_number = request.json["room_number"]
    room_type = request.json["room_type"]

    new_room = Room(room_number=room_number, room_type=room_type)

    db.session.add(new_room)
    db.session.commit()

    return jsonify(new_room.serialize()), 201

@room_blueprint.route("/<string:room_number>", methods=["GET"])
def get_room(room_number):
    room = Room.query.filter_by(room_number=room_number).first()
    if room is None:
        return "Room not found", 404
    
    return jsonify(room.serialize()), 200

@room_blueprint.route("/all", methods=["GET"])
def get_all():
    rooms = Room.query.all()
    rooms = list(map(lambda room: room.serialize(), rooms))

    return jsonify(rooms), 200

@room_blueprint.route("/<string:room_number>", methods=["PUT"])
def update(room_number):
    room = Room.query.filter_by(room_number=room_number).first()
    if room is None:
        return "Room not found", 404

    room.room_type = request.json["room_type"]

    db.session.commit()

    return jsonify(room.serialize()), 200

@room_blueprint.route("/<string:room_number>", methods=["DELETE"])
def delete(room_number):
    room = Room.query.filter_by(room_number=room_number).first()
    if room is None:
        return "Room not found", 404

    db.session.delete(room)
    db.session.commit()

    return jsonify(room), 204

@room_blueprint.route("/type/<string:room_type>", methods=["GET"])
def get_rooms_by_room_type(room_type):
    rooms = Room.query.filter_by(room_type=room_type).all()
    print(rooms)

    
    if len(rooms) == 0 or rooms is None or not isinstance(rooms, list):
        return f"No rooms found for type {room_type}", 404

    serialized_rooms = [room.serialize() for room in rooms]

    return jsonify(serialized_rooms), 200