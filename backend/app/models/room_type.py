from app.database import db

class RoomType(db.Model):
    db.__tablename__ = "room_type"
    __table_args__ = {'schema': 'hotel9'}
    room_type = db.Column(db.String(20), primary_key=True)
    price_per_night = db.Column(db.String(45), nullable=False)

    def serialize(self):
        return {
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'rooms': [{'room_number': room.room_number} for room in self.rooms] if self.rooms else []
        }