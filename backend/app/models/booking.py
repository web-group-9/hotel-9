from app.database import db

booking_has_guest = db.Table('booking_has_guest',
    db.Column('booking_booking_id', db.Integer, db.ForeignKey('hotel9.booking.booking_id'), primary_key=True),
    db.Column('guest_guest_id', db.Integer, db.ForeignKey('hotel9.guest.guest_id'), primary_key=True),
    schema='hotel9'
)

booking_has_room = db.Table('booking_has_room',
    db.Column('booking_booking_id', db.Integer, db.ForeignKey('hotel9.booking.booking_id'), primary_key=True),
    db.Column('room_room_number', db.String(4), db.ForeignKey('hotel9.room.room_number'), primary_key=True),
    schema='hotel9'
)

class Booking(db.Model):
    __table_args__ = {'schema': 'hotel9'}
    booking_id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(4), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    booking_date = db.Column(db.Date, nullable=False)

    guests = db.relationship('Guest', secondary=booking_has_guest, backref='bookings', lazy='dynamic')
    rooms = db.relationship('Room', secondary=booking_has_room, backref='bookings', lazy='dynamic')

    def serialize(self):
        return {
            'booking_id': self.booking_id,
            'guest_id': self.guest_id,
            'room_number': self.room_number,
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date,
            'booking_date': self.booking_date,
            'guests': [{'guest_name': guest.guest_name, 'contact_info': guest.contact_info} for guest in self.guests] if self.guests else []
        }
