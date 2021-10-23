from flask import Blueprint, render_template, flash; from flask.globals import request; from flask.helpers import url_for
from flask.wrappers import Response; from werkzeug.utils import redirect; import requests
import os, sys; currentdir = os.path.dirname(os.path.realpath(__file__)); parentdir = os.path.dirname(currentdir); sys.path.append(parentdir)

projects = Blueprint("projects", __name__)
def g(frm):
    return request.form.get(frm)


@projects.route("/")
def prjcts(): return render_template("projects.html", acti="projects")


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

    user_login_data = str({"email": g("email"), 
                            "password": g("password")})
    user_delete_data = str({"id": "fdf34f34f34-f34f34-f43f43f34-f4f34f"})               # Unfinished
    user_logout_data = str({"sessionId": "sds34s34s34-s34s34-s43s43s34-s4s34s"})        # Unfinished
    user_read_data = str({"id": "usrid-1"})                                             # Unfinished
    user_read_session_data = str({"sessionId": "sds34s34s34-s34s34-s43s43s34-s4s34s"})  # Unfinished
    
    db_count_records_data = str({"table": "users"})
    db_delete_record_data = str({"id": "1", "table": "users"})  # Unfinished
    db_read_record_data = str({"id": "1", "table": "users"})
    db_update_record_data = str({"record": {
                                    "age": 43,
                                    "id": "1"},
                                "table": "users"})      # Unfinished


    def create_user(data):
        return requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, data=data)
    def login_user(data):
        return requests.post("https://api.m3o.com/v1/user/Login", headers=api_auth, data=data)
    def delete_user(data):
        return requests.post("https://api.m3o.com/v1/user/Delete", headers=api_auth, data=data)
    def logout_user(data):
        return requests.post("https://api.m3o.com/v1/user/Logout", headers=api_auth, data=data)
    def read_user(data):
        return requests.get("https://api.m3o.com/v1/user/Read", headers=api_auth, data=data)
    def read_session(data):
        return requests.get("https://api.m3o.com/v1/user/ReadSession", headers=api_auth, data=data)
    
    def count_records(data):
        return requests.get("https://api.m3o.com/v1/db/Count", headers=api_auth, data=data)
    def create_record(data):
        return requests.post("https://api.m3o.com/v1/db/Create", headers=api_auth, data=data)
    def delete_record(data):
        return requests.post("https://api.m3o.com/v1/db/Delete", headers=api_auth, data=data)
    def read_record(data):
        return requests.get("https://api.m3o.com/v1/db/Read", headers=api_auth, data=data)
    def update_record(data):
        return requests.post("https://api.m3o.com/v1/db/Update", headers=api_auth, data=data)

    #db_rad_record_data = str({"query": "username == isak", "table": "users"})
    #hh = requests.get("https://api.m3o.com/v1/db/Read", headers=api_auth, data=db_rad_record_data)
    #print(hh.text)

    if request.method == "POST":
        register_email = str(g("register_email")); register_username = str(g("register_username")); register_password = str(g("register_password"))
        if g("register_email") and g("register_username") and g("register_password"):
            user_id = str(random.randint(10000000,99999999))
            user_register_data = str({"email": register_email, "id": user_id, "password": register_password, "username": register_username})
            db_create_record_data = str({"record": {"email": register_email, "id": user_id, "password": register_password, "username": register_username}, "table": "users"})
            user_register_data = {"email": "nosel@gmail.com", "id": user_id, "password": "leonleon", "username": "nosel"}
            b = requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, data=user_register_data)
            #a = create_record(db_create_record_data)
            print(b.text)
            #print(a.text)
            print(user_id)


    return render_template("user-api.html", acti="projects")