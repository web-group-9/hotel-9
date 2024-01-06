import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app()
if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("HOST_PORT"), debug=os.getenv("DEBUG"))