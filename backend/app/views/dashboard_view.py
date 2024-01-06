from flask import Blueprint, render_template

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates/dashboard")

@dashboard_blueprint.route("/")
def index():
    return render_template("index.html")

@dashboard_blueprint.route("/login")
def login():
    return render_template("login.html")

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
