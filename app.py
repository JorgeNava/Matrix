from flask import Flask, render_template, session, request
import os

app = Flask(__name__)
app.secret_key = "secreto"


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    session["usuario"] = ""
    if request.method == "POST":
        session["usuario"] = request.form["txtUsuario"]
    return render_template("login.html")


@app.route("/terminal", methods=["POST", "GET"])
def terminal():
    return render_template("terminal.html", usr=session["usuario"])


app.run(debug=True, port=80)
