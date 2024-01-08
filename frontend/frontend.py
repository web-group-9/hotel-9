from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
import requests
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# About Us Page

@app.route("/about")
def about():
    return render_template("about.html")

# Blog Page
@app.route("/blog")
def blog():
    return render_template("blog.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Booking Page
@app.route("/booking")
def booking():
    return render_template("booking.html")

# Rooms Page
@app.route("/rooms", methods=["GET"])
def rooms():
    return render_template("rooms.html")

class BookingForm(FlaskForm):
    room_type = StringField("Room Type", validators=[DataRequired()])
    guest_name = StringField("Name", validators=[DataRequired()])
    guest_contact_info = StringField("Contact Info", validators=[DataRequired()])
    check_in_date = DateField("Check-in Date", validators=[DataRequired()])
    check_out_date = DateField("Check-out Date", validators=[DataRequired()])
    submit = SubmitField("Complete Booking")

@app.route("/booking/complete", methods=["GET", "POST"])
def booking_complete():
    room_type = request.args.get("room_type")


    form = BookingForm()
    form.room_type.data = room_type

    if form.validate_on_submit():
        guest_name = form.guest_name.data
        guest_contact_info = form.guest_contact_info.data
        check_in_date = form.check_in_date.data
        check_out_date = form.check_out_date.data
        booking_date = datetime.now()

        guest = requests.post("http://127.0.0.1:5001/guest/create", json={
            "guest_name": guest_name,
            "contact_info": guest_contact_info
        }).json()

        guest_id = guest["guest_id"]
        
        result = requests.post("http://127.0.0.1:5001/booking/create", json={
            "guest_id": guest_id,
            "check_in_date": check_in_date.isoformat(),
            "check_out_date": check_out_date.isoformat(),
            "booking_date": booking_date.isoformat(),
            "room_type": room_type
        })

        if result.status_code >= 300:
            return render_template("complete_booking.html", room_type=room_type, form=form, error=result.text)

        return redirect(url_for("booking_success"))

    return render_template("complete_booking.html", room_type=room_type, form=form)

# Booking Success Page
@app.route("/booking/success")
def booking_success():
    return render_template("booking_success.html")


# Search Result Page
@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    if request.method == "POST":
        # Handle the POST request
        pass

    room_type = request.args.get("room_type")

    # Call backend function to get rooms by room type
    # Replace with your actual backend function
    search_results = requests.get(f"http://127.0.0.1:5001/room/type/{room_type}").json()

    return render_template("search_results.html", search_results=search_results)

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))