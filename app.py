from flask import Flask, render_template, session, request, jsonify
import os
from usuario import Usuario
import json

app = Flask(__name__)
app.secret_key = "secreto"

users = [Usuario("admin", "cisco"), Usuario(
    "Gustavo", "cisco"), Usuario("Jorge", "cisco")]

# Recipiente del usuario actual, sera asignado despues de hacer login
actualUser = Usuario("", "")


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
    # O usamos JSON
    # si recibe POST se le para saber que funcion correr
    # switch con funciones en base a comando corrido en terminal
    # js escribe en un txt, py lo abre y extrae los datos, py escribe en txt y js lo lee
    #comando_recibido = request.args.get("comando")
    #Nombre_archivo = request.args.get("nombreArchivo")
    comando_recibido = request.args.get("comando_a_enviar")
    if (comando_recibido is not None):
        comando_seccionado = comando_recibido.split("-")
        if(comando_seccionado[0] == "createf"):
            nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + ".txt"
            file_handler = open(nombre_del_archivo, 'w')
            file_handler.close()
        elif(comando_seccionado[0] == "edit"):
            nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + ".txt"
            file_handler = open(nombre_del_archivo, 'a')
            file_handler.write(comando_seccionado[2]+"\n")
            file_handler.close()
    else:
        print("Comando is None")
    return render_template("terminal.html", usr=actualUser._Nombre, inodo_del_directorio_actual=actualUser._InodoDelDirectorioActual)

    # return jsonify("Is done!!!")'''


app.run(debug=True, port=80)
