import os
from flask import Flask
from app.database import db

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    
    db.init_app(app)

    from app.models.guest import Guest
    from app.models.room import Room
    from app.models.booking import Booking
    from app.models.room_type import RoomType

    with app.app_context():
        from app.views.dashboard_view import dashboard_blueprint
        app.register_blueprint(dashboard_blueprint)
        from app.controllers.guest_controller import guest_blueprint
        app.register_blueprint(guest_blueprint)
        from app.controllers.room_controller import room_blueprint
        app.register_blueprint(room_blueprint)
        from app.controllers.booking_controller import booking_blueprint
        app.register_blueprint(booking_blueprint)
        from app.controllers.room_type_controller import room_type_blueprint
        app.register_blueprint(room_type_blueprint)
    
    return app
