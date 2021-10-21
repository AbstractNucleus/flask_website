from flask import Blueprint, render_template

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

@views.route("/rsa")
@views.route("/projects/rsa")
def rsa():
    import os, sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    from backend.projects.rsa.rsa_modules import key_gen
    
    p, q, F, n, e, d = key_gen(512)
    
    return render_template("rsa.html", p=p, q=q, F=F, n=n, e=e, d=d)