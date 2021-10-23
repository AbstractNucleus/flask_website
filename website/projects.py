from flask import Blueprint, render_template, flash; from flask.globals import request; from flask.helpers import url_for; from werkzeug.utils import redirect
import os, sys; currentdir = os.path.dirname(os.path.realpath(__file__)); parentdir = os.path.dirname(currentdir); sys.path.append(parentdir)

projects = Blueprint("projects", __name__)


@projects.route("/")
def prjcts(): return render_template("projects.html", acti="projects")


@projects.route("/rsa", methods=['GET', 'POST'])
def rsa():
    import backend.projects.rsa.rsa_modules as rsa
    p, q, F, n, e, d = rsa.key_gen(512)
    if request.method == "POST":
        if request.form.get("message") and request.form.get("n_encrypt") and request.form.get("e_encrypt"):
            input_message = int(request.form.get("message"))
            n_encrypt = int(request.form.get("n_encrypt"))
            e_encrypt = int(request.form.get("e_encrypt"))
            cipher = rsa.encrypt(input_message, n_encrypt, e_encrypt)
            return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, 
                               e=e, d=d, cipher=cipher, n_encrypt=n_encrypt, 
                               e_encrypt=e_encrypt, n_decrypt=0, 
                               d_decrypt=0, output_message=0)
        if request.form.get("input_cipher"):
            input_cipher = int(request.form.get("input_cipher"))
            n_decrypt = int(request.form.get("n_decrypt"))
            d_decrypt = int(request.form.get("d_decrypt"))
            output_message = rsa.decrypt(input_cipher, n_decrypt, d_decrypt)
            return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, 
                               e=e, d=d, cipher=0, n_encrypt=0, 
                               e_encrypt=0, n_decrypt=n_decrypt, 
                               d_decrypt=d_decrypt, output_message=output_message)
    
    return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, e=e, d=d)

@projects.route("/user-api", methods=['GET', 'POST'])
def user_api():
    
    return render_template("user-api.html", acti="projects")