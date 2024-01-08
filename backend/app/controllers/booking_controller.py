from flask import Blueprint, jsonify, request
from app.models.booking import Booking
from app.database import db
from app.models.guest import Guest
from app.models.room import Room

booking_blueprint = Blueprint("booking", __name__, url_prefix="/booking")

@booking_blueprint.route("/create", methods=["POST"])
def create():
    guest_id = request.json["guest_id"]
    room_type = request.json["room_type"]
    check_in_date = request.json["check_in_date"]
    check_out_date = request.json["check_out_date"]
    booking_date = request.json["booking_date"]


    guest = Guest.query.filter_by(guest_id=guest_id).first()

    if guest is None:
        return "Guest not found", 404
    
    room = Room.query.filter(Room.room_type.has(room_type=room_type)).first()

    if room is None:
        return "Room not found", 404

    new_booking = Booking(guest_id=guest_id, room_number=room.room_number, check_in_date=check_in_date, check_out_date=check_out_date, booking_date=booking_date)
    new_booking.guests.append(Guest.query.filter_by(guest_id=guest_id).first())

    db.session.add(new_booking)
    db.session.commit()

    return jsonify(new_booking.serialize()), 201

@booking_blueprint.route("/<int:booking_id>", methods=["GET"])
def get_booking(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404
    

    return jsonify(booking.serialize()), 200

@booking_blueprint.route("/all", methods=["GET"])
def get_all():
    bookings = Booking.query.all()
    bookings = list(map(lambda booking: booking.serialize(), bookings))

    return jsonify(bookings), 200

@booking_blueprint.route("/<int:booking_id>", methods=["PUT"])
def update(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    booking.room_number = request.json["room_number"]
    booking.start_date = request.json["start_date"]
    booking.end_date = request.json["end_date"]

    guest = Guest.query.filter_by(guest_id=request.json["guest_id"]).first()
    if guest is None:
        return "Guest not found", 404

    db.session.commit()

    return jsonify(booking.serialize()), 200

@booking_blueprint.route("/<int:booking_id>", methods=["DELETE"])
def delete(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    db.session.delete(booking)
    db.session.commit()

    return jsonify(booking), 204

@booking_blueprint.route("/<int:booking_id>/guests", methods=["GET"])
def get_guests(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    guests = booking.guests
    guests = list(map(lambda guest: guest.serialize(), guests))

    return jsonify(guests), 200

@booking_blueprint.route("/<int:booking_id>/guests/<int:guest_id>", methods=["POST"])
def add_guest(booking_id, guest_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    guest = Guest.query.filter_by(guest_id=guest_id).first()
    if guest is None:
        return "Guest not found", 404

    booking.guests.append(guest)
    db.session.commit()

    return jsonify(booking.serialize()), 200

@booking_blueprint.route("/<int:booking_id>/guests/<int:guest_id>", methods=["DELETE"])
def remove_guest(booking_id, guest_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    guest = Guest.query.filter_by(guest_id=guest_id).first()
    if guest is None:
        return "Guest not found", 404

    booking.guests.remove(guest)
    db.session.commit()

    return jsonify(booking.serialize()), 200

@booking_blueprint.route("/<int:booking_id>/rooms", methods=["GET"])
def get_rooms(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    rooms = booking.rooms
    rooms = list(map(lambda room: room.serialize(), rooms))

    return jsonify(rooms), 200

@booking_blueprint.route("/<int:booking_id>/rooms/<int:room_number>", methods=["POST"])
def add_room(booking_id, room_number):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if booking is None:
        return "Booking not found", 404

    room = Room.query.filter_by(room_number=room_number).first()
    if room is None:
        return "Room not found", 404

    booking.rooms.append(room)
    db.session.commit()

    return jsonify(booking.serialize()), 200
