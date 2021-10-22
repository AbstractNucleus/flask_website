from flask import Blueprint, render_template, flash
from flask.globals import request
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import backend.projects.rsa.rsa_modules as rsa

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/project")
@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("/rsa", methods=['GET', 'POST'])
@views.route("/projects/rsa", methods=['GET', 'POST'])
def rsa():
    if request.method == "POST":
        message = int(request.form.get("message"))
        n_encrypt = int(request.form.get("n_encrypt"))
        e_encrypt = int(request.form.get("e_encrypt"))
        cipher = rsa.encrypt(message, n_encrypt, e_encrypt)
        flash(cipher)

    p, q, F, n, e, d = rsa.key_gen(512)
    return render_template("rsa.html", p=p, q=q, F=F, n=n, e=e, d=d)