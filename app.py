from flask import Flask, render_template, session, request
import os
from usuario import Usuario
import json

app = Flask(__name__)
app.secret_key = "secreto"

users = [Usuario("admin","cisco"),Usuario("Gustavo","cisco"),Usuario("Jorge","cisco")]
json.dumps(users)

@app.route("/")
def inicio():
    return render_template("inicio.html",usrs=users)

@app.route("/login", methods=["POST", "GET"])
def login():
    session["usuario"] = ""
    if request.method == "POST":
        session["usuario"] = request.form["txtUsuario"]
        session["user"] = users[0]
    return render_template("login.html")


@app.route("/terminal", methods=["POST", "GET"])
def terminal():
    return render_template("terminal.html", usr=session["usuario"],usr)


app.run(debug=True, port=80)
