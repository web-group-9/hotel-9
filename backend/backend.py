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
def hello_world():
    return render_template("index.html", title=app.name)

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))