from app.database import db

class Room(db.Model):
    __table_args__ = {'schema': 'hotel9'}
    room_number = db.Column(db.String(4), primary_key=True)
    room_type = db.Column(db.String(20), db.ForeignKey('hotel9.room_type.room_type'), nullable=False)
    
    room_type_ref = db.relationship('RoomType', backref='rooms')

    def serialize(self):
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'room_type_details': {
                'room_type': self.room_type_ref.room_type,
                'price_per_night': self.room_type_ref.price_per_night
            },
            'bookings': [{'booking_id': booking.booking_id, 'check_in_date': booking.check_in_date, 'check_out_date': booking.check_out_date} for booking in self.bookings] if self.bookings else []
        }
