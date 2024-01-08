from flask_login import LoginManager
from app.models.user import User

login_manager = LoginManager()

users = {
    'admin': User('admin', '666666'),
    'supereditor': User('supereditor', 'supereditor'),
    'staff': User('staff', 'staff'),
    'yaemikodog' : User('yaemikodog','whatapoorguy')
}

@login_manager.user_loader
def load_user(role):
    return users.get(role)
