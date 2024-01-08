from flask import Flask, render_template, jsonify,request, redirect, url_for
from flask_login import LoginManager, login_user
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(role):
    return users.get(role)


class User(UserMixin):
    def __init__(self, role, password):
        self.id = role  # Assuming role is unique
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)
users = {
    'admin': User('admin', '666666'),
    'supereditor': User('supereditor', 'supereditor'),
    'staff': User('staff', 'staff'),
    'yaemikodog' : User('yaemikodog','whatapoorguy')
}

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

db = SQLAlchemy(app)

class Booking(db.Model):
    __tablename__ = 'booking'
    __table_args__ = {'schema': 'hotel9'}
    booking_id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('hotel9.guest.guest_id'))
    room_number = db.Column(db.String(4), db.ForeignKey('hotel9.room.room_number'))
    check_in_date = db.Column(db.Date)
    check_out_date = db.Column(db.Date)
    booking_date = db.Column(db.Date)
    guest = db.relationship('Guest', backref='bookings')  # Use 'Guest' instead of 'guest'
    room = db.relationship('Room', backref='bookings')   # Use 'Room' instead of 'room'

class Room(db.Model):
    __tablename__ = 'room'
    __table_args__ = {'schema': 'hotel9'}
    room_number = db.Column(db.String(4), primary_key=True)
    room_type_id = db.Column(db.String(20), db.ForeignKey('hotel9.room_type.room_type'))
    room_type = db.relationship('RoomType', backref='rooms')

class RoomType(db.Model):
    __tablename__ = 'room_type'
    __table_args__ = {'schema': 'hotel9'}
    room_type = db.Column(db.String(20), primary_key=True)
    price_per_night = db.Column(db.String(45))

class Guest(db.Model):
    __tablename__='guest'
    __table_args__ = {'schema': 'hotel9'}
    guest_id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(45))
    contact_info = db.Column(db.String(45))

@app.route("/mainpageformanagement")
@login_required
def index():
        # Fetch data from Booking and Room tables
    booking = Booking.query.all()
    room = Room.query.all()
    roomtype = RoomType.query.all()

    # Calculate monthly earnings
    monthly_earnings = 0.0
    current_month = datetime.now().month

    annual_earnings = 0.0
    current_year = datetime.now().year

    for current_booking in booking:
        # Check if the booking is in the current month
        if current_booking.check_in_date.month == current_month or current_booking.check_out_date.month == current_month:
            # Calculate the number of days the room is booked
            booking_days = (current_booking.check_out_date - current_booking.check_in_date).days + 1

            # Find the corresponding room
            current_room = next((room for room in room if room.room_number == current_booking.room_number), None)

            if current_room:
                # Find the corresponding room type
                room_type = next((rt for rt in roomtype if rt.room_type == current_room.room_type_id), None)

                if room_type:
                    # Add the earnings for the booking to the total
                    monthly_earnings += booking_days * float(room_type.price_per_night)

        # Check if the booking is in the current year
        if current_booking.check_in_date.year == current_year or current_booking.check_out_date.year == current_year:
            # Calculate the number of days the room is booked
            booking_days = (current_booking.check_out_date - current_booking.check_in_date).days + 1

            # Find the corresponding room
            current_room = next((room for room in room if room.room_number == current_booking.room_number), None)

            if current_room:
                # Find the corresponding room type
                room_type = next((rt for rt in roomtype if rt.room_type == current_room.room_type_id), None)

                if room_type:
                    # Add the earnings for the booking to the total
                    annual_earnings += booking_days * float(room_type.price_per_night)

    daily_housing_rate = 100.0  # You can replace this with the actual daily housing rate
    total_days_in_year = 365

    # Calculate the number of days booked in the current year
    days_booked = sum((current_booking.check_out_date - current_booking.check_in_date).days + 1 for current_booking in booking
                      if current_booking.check_in_date.year == current_year or current_booking.check_out_date.year == current_year)

    # Calculate progress percentage
    progress_percentage = (days_booked / total_days_in_year) * 100

    return render_template("index.html", user=current_user,monthly_earnings=monthly_earnings,annual_earnings=annual_earnings,progress_percentage=progress_percentage)

@app.route("/get_housing_rate_data")
def get_housing_rate_data():
    # Fetch data from Booking table
    booking = Booking.query.all()

    # Calculate housing rate for each month
    housing_rate_data = {}
    for booking in booking:
        current_month = booking.check_in_date.month
        key = f"{current_month:02d}"  # Format month as two digits (e.g., '01' for January)
        
        # Calculate the number of days the room is booked
        booking_days = (booking.check_out_date - booking.check_in_date).days + 1

        # Calculate total earnings for the month
        monthly_earnings = housing_rate_data.get(key, 0) + booking_days

        # Update the housing rate data
        housing_rate_data[key] = monthly_earnings

    data = {
        "labels": list(housing_rate_data.keys()),
        "values": list(housing_rate_data.values())
    }

    return jsonify(data)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        password = request.form['password']
        user = users.get(role)

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html')

# @app.route('/bookings')
# def bookings():
#     bookings = Booking.query.all()
#     return render_template('bookings.html', bookings=bookings)
   
  
# @app.route('/cancel_booking', methods=['POST'])
# def cancel_booking():
#     data = request.get_json()
#     booking_id = data.get('booking_id')
#     print(f"booking_id: {booking_id}")
     
#     try:
#         booking = Booking.query.get(booking_id)
#         if booking:
#             db.session.delete(booking)
#             db.session.commit()
#             return jsonify({"status": "success", "message": "Booking deleted"})
#         else:
#             return jsonify({"status": "error", "message": "Booking not found"}), 404
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"status": "error", "message": str(e)}), 500


# @app.route('/update_booking_date', methods=['POST'])
# def update_booking_date():
#     data = request.get_json()
#     booking_id = data['booking_id']
#     date_type = data['date_type']
#     new_date = data['new_date']
#     print(f"booking_id: {booking_id}, date_type: {date_type}, new_date: {new_date}")
    
#     try:
#         booking = Booking.query.get(booking_id)
#         if booking:
#             if date_type == 'check_in_date':
#                 booking.check_in_date = datetime.strptime(new_date, '%Y-%m-%d').date()
#             elif date_type == 'check_out_date':
#                 booking.check_out_date = datetime.strptime(new_date, '%Y-%m-%d').date()
#             db.session.commit()
#             return jsonify({"status": "success", "message": "Booking date updated"})
#         else:
#             return jsonify({"status": "error", "message": "Booking not found"}), 404
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))