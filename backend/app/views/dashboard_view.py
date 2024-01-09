from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from datetime import datetime
from flask_login import current_user, login_user, login_required
from app.models.booking import Booking
from app.login_manager import users
from app.models.room import Room
from app.models.room_type import RoomType
from app.database import db


dashboard_blueprint = Blueprint("dashboard", __name__)


@dashboard_blueprint.route("/mainpageformanagement")
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

    return render_template("dashboard/index.html", user=current_user,monthly_earnings=monthly_earnings,annual_earnings=annual_earnings,progress_percentage=progress_percentage)

@dashboard_blueprint.route("/get_housing_rate_data")
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

@dashboard_blueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        password = request.form['password']
        user = users.get(role)

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard.index'))
    return render_template('dashboard/login.html')



@dashboard_blueprint.route("/utilities-other")
def utilities_other():
    return render_template("utilities-other.html")

@dashboard_blueprint.route("/utilities-color")
def utilities_color():
    return render_template("utilities-color.html")

@dashboard_blueprint.route("/utilities-border")
def utilities_border():
    return render_template("utilities-border.html")

@dashboard_blueprint.route("/utilities-animation")
def utilities_animation():
    return render_template("utilities-animation.html")

@dashboard_blueprint.route("/tables")
def tables():
    return render_template("tables.html")

@dashboard_blueprint.route("/register")
def register():
    return render_template("register.html")

@dashboard_blueprint.route("/charts")
def charts():
    return render_template("charts.html")

@dashboard_blueprint.route("/cards")
def cards():
    return render_template("cards.html")

@dashboard_blueprint.route("/buttons")
def buttons():
    return render_template("buttons.html")

@dashboard_blueprint.route("/blank")
def blank():
    return render_template("blank.html")

@dashboard_blueprint.route("/404")
def error_404():
    return render_template("404.html")

@dashboard_blueprint.route("/forgot-password")
def forgotpassword():
    return render_template("forgot-password.html")

@dashboard_blueprint.route('/bookings')
def bookings():
    bookings = Booking.query.all()
    room_type = RoomType.query.all()
    for booking in bookings:
        days_difference = (booking.check_out_date - booking.check_in_date).days + 1
        if booking.rooms.first():
            booking.total = float(booking.rooms.first().room_type.price_per_night) * days_difference
    return render_template('dashboard/bookings.html', bookings=bookings,room_type=room_type)
   
  
@dashboard_blueprint.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    data = request.get_json()
    booking_id = data.get('booking_id')
    print(f"booking_id: {booking_id}")
     
    try:
        booking = Booking.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return jsonify({"status": "success", "message": "Booking deleted"})
        else:
            return jsonify({"status": "error", "message": "Booking not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500


@dashboard_blueprint.route('/update_booking_date', methods=['POST'])
def update_booking_date():
    data = request.get_json()
    booking_id = data['booking_id']
    date_type = data['date_type']
    new_date = data['new_date']
    print(f"booking_id: {booking_id}, date_type: {date_type}, new_date: {new_date}")
    
    try:
        booking = Booking.query.get(booking_id)
        if booking:
            if date_type == 'check_in_date':
                booking.check_in_date = datetime.strptime(new_date, '%Y-%m-%d').date()
            elif date_type == 'check_out_date':
                booking.check_out_date = datetime.strptime(new_date, '%Y-%m-%d').date()
            db.session.commit()
            return jsonify({"status": "success", "message": "Booking date updated"})
        else:
            return jsonify({"status": "error", "message": "Booking not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500