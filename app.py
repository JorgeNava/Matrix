from flask import Flask, render_template, session, request
import os
from usuario import Usuario
import json

app = Flask(__name__)
app.secret_key = "secreto"

users = [Usuario("admin", "cisco"), Usuario(
    "Gustavo", "cisco"), Usuario("Jorge", "cisco")]

# Recipiente del usuario actual, sera asignado despues de hacer login
actualUser = users[2]


@ app.route("/")
def inicio():
    return render_template("inicio.html")


@ app.route("/login", methods=["POST", "GET"])
def login():
    session["usuario"] = ""
    if request.method == "POST":
        for u in users:
            if request.form["txtUsuario"] in u._Nombre:
                session["usuario"] = request.form["txtUsuario"]
                actualUser._Nombre = u._Nombre
                actualUser._Contraseña = u._Contraseña
                actualUser._LIL = u._LIL
                actualUser._LBL = u._LBL
                actualUser._Inodo = u._Inodo
                actualUser._Directorio = u._Directorio
                actualUser._InodoDelDirectorioActual = u._InodoDelDirectorioActual
    return render_template("login.html")


@ app.route("/terminal", methods=["POST", "GET"])
def terminal():
    return render_template("terminal.html", usr=actualUser._Nombre, inodo_del_directorio_actual=actualUser._InodoDelDirectorioActual)


app.run(debug=True, port=80)
