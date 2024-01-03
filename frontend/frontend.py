from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title=app.name)

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))