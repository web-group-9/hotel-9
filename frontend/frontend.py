from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

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