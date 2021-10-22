from flask import Blueprint, render_template, flash; from flask.globals import request; from flask.helpers import url_for; from werkzeug.utils import redirect

views = Blueprint("views", __name__)

@views.route("/")
def home(): return render_template("home.html")
@views.route("/home")
@views.route("/h")
def ret_home(): return redirect(url_for("views.home"))

@views.route("/about")
def about(): return render_template("about.html")