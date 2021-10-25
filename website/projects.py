from flask import Blueprint, render_template, flash; from flask.globals import request; from flask.helpers import make_response, url_for
from flask.wrappers import Response; from werkzeug.utils import redirect; import requests
import os, sys; currentdir = os.path.dirname(os.path.realpath(__file__)); parentdir = os.path.dirname(currentdir); sys.path.append(parentdir)

projects = Blueprint("projects", __name__)
def g(frm):
    return request.form.get(frm)


@projects.route("/")
def prjcts(): return render_template("projects.html", acti="projects")

@projects.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == 'POST':
        login_username = g("login_username")
        
        
        resp = make_response(render_template('home.html'))
        resp.set_cookie('login_username', login_username)
    return resp

@projects.route("/rsa", methods=['GET', 'POST'])
def rsa():
    import backend.projects.rsa.rsa_modules as rsa
    p, q, F, n, e, d = rsa.key_gen(512)
    if request.method == "POST":
        if g("message") and g("n_encrypt") and g("e_encrypt"):
            input_message = int(g("message"))
            n_encrypt = int(g("n_encrypt"))
            e_encrypt = int(g("e_encrypt"))
            cipher = rsa.encrypt(input_message, n_encrypt, e_encrypt)
            return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, 
                               e=e, d=d, cipher=cipher, n_encrypt=n_encrypt, 
                               e_encrypt=e_encrypt, n_decrypt=0, 
                               d_decrypt=0, output_message=0)
        if g("input_cipher") and g("n_decrypt") and g("d_decrypt"):
            input_cipher = int(g("input_cipher"))
            n_decrypt = int(g("n_decrypt"))
            d_decrypt = int(g("d_decrypt"))
            output_message = rsa.decrypt(input_cipher, n_decrypt, d_decrypt)
            return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, 
                               e=e, d=d, cipher=0, n_encrypt=0, 
                               e_encrypt=0, n_decrypt=n_decrypt, 
                               d_decrypt=d_decrypt, output_message=output_message)
    
    return render_template("rsa.html", acti="projects", p=p, q=q, F=F, n=n, e=e, d=d)

@projects.route("/user-api", methods=['GET', 'POST'])
def user_api():
    import random
    token = "OGJhYmVhMjMtOGI0Mi00MDVhLTkwZDktZDZjZGRlMzUxMTlk"
    api_auth = {'Authorization' : f'Bearer {token}'}

    if request.method == "POST":
        if g("login_username") and g("login_password"): # Login user
            try:
                print(1)
                login_data = {"username": g("login_username"), "password": g("login_password")}
                print(login_data)
                login = requests.post("https://api.m3o.com/v1/user/Login", headers=api_auth, json=login_data).json()
                print(login)
                try:
                    print(2)
                    if login["Code"] == 500:
                        return render_template("user-api.html", acti="projects", login_error="username or password is wrong")
                except:
                    print(3)
                    #db_login_data = {"record": {"username": g("login_username"), "logged_in": True}}
                    return render_template("user-api.html", acti="projects", logged_in=True)
                    #return make_response(render_template("user-api.html", acti="projects", logged_in=True)).set_cookie("session", login["session"]["id"])
            except:
                print(4)

        if g("register_email") and g("register_username") and g("register_password"): # Register user
            register_email = str(g("register_email")); register_username = str(g("register_username")); register_password = str(g("register_password"))
            user_id = str(random.randint(10000000,99999999))
            user_register_data = {"email": register_email, "id": user_id, "password": register_password, "username": register_username}
            try:
                create_user_response = requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, json=user_register_data).json()
                while create_user_response["Code"] == 500:
                    user_id = str(random.randint(10000000,99999999))
                    user_register_data = {"email": register_email, "id": user_id, "password": register_password, "username": register_username}
                    create_user_response = requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, json=user_register_data).json()
                try:
                    if create_user_response["Code"] == 400:
                        return render_template("user-api.html", acti="projects", error="username already exists")
                except:
                    return render_template("user-api.html", acti="projects", success=f"user successfully created {user_register_data['username']}")
            except:
                try:
                    if create_user_response["Code"] == 400:
                        return render_template("user-api.html", acti="projects", error="username already exists")
                except:
                    return render_template("user-api.html", acti="projects", success=f"user successfully created {user_register_data['username']}")
        if g("read_user"): # Search for user
            from datetime import datetime
            read_user = g("read_user")
            try:
                read_user = int(read_user)
                search = requests.post("https://api.m3o.com/v1/user/Read", headers=api_auth, json={"id": str(read_user)}).json()
                try:
                    print(search)
                    if search["Code"] == 500:
                        return render_template("user-api.html", acti="projects", search=f'user not found [{read_user}]')
                except:
                    return render_template("user-api.html", acti="projects", search=True, search_creation=search["account"]["created"], search_updated=search["account"]["updated"], search_username=search["account"]["username"], search_id=search["account"]["id"], search_email=search["account"]["email"])
            except:
                search = requests.post("https://api.m3o.com/v1/user/Read", headers=api_auth, json={"username": read_user}).json()
                try:
                    if search["Code"] == 500:
                        return render_template("user-api.html", acti="projects", search=f'user not found [{read_user}]')
                except:
                    return render_template("user-api.html", acti="projects", search=True, search_creation=datetime.utcfromtimestamp(int(search["account"]["created"])).strftime('%Y-%m-%d %H:%M:%S'), search_updated=datetime.utcfromtimestamp(int(search["account"]["updated"])).strftime('%Y-%m-%d %H:%M:%S'), search_username=search["account"]["username"], search_id=search["account"]["id"], search_email=search["account"]["email"])
        return render_template("user-api.html", acti="projects")
    return render_template("user-api.html", acti="projects")