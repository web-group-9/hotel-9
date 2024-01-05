from flask import Flask, render_template
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/utilities-other")
def utilities_other():
    return render_template("utilities-other.html")

@app.route("/utilities-color")
def utilities_color():
    return render_template("utilities-color.html")

@app.route("/utilities-border")
def utilities_border():
    return render_template("utilities-border.html")

@app.route("/utilities-animation")
def utilities_animation():
    return render_template("utilities-animation.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route("/buttons")
def buttons():
    return render_template("buttons.html")

@app.route("/blank")
def blank():
    return render_template("blank.html")

@app.route("/404")
def error_404():
    return render_template("404.html")

@app.route("/forgot-password")
def forgotpassword():
    return render_template("forgot-password.html")

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))