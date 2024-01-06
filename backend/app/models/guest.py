from app.database import db

class Guest(db.Model):
    __table_args__ = {'schema': 'hotel9'}
    guest_id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(45), nullable=False)
    contact_info = db.Column(db.String(45), nullable=False)

    def serialize(self):
        return {
            'guest_id': self.guest_id,
            'guest_name': self.guest_name,
            'contact_info': self.contact_info,
            'bookings': [{'booking_id': booking.booking_id, 'check_in_date': booking.check_in_date, 'check_out_date': booking.check_out_date} for booking in self.bookings] if self.bookings else []
        }