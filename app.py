from flask import Flask, render_template, session, request, jsonify
import os
from usuario import Usuario
import json
from os import listdir
from os.path import isfile, isdir


app = Flask(__name__)
app.secret_key = "secreto"

users = [Usuario("admin", "cisco"), Usuario(
    "Gustavo", "cisco"), Usuario("Jorge", "cisco")]

global pathDirectorioActual

# Recipiente del usuario actual, sera asignado despues de hacer login
actualUser = Usuario("", "")


@ app.route("/")
def inicio():
    return render_template("inicio.html")


@ app.route("/login", methods=["POST", "GET"])
def login():
    global pathDirectorioActual
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
        pathDirectorioActual ="./files/"+actualUser._Nombre
    return render_template("login.html")


@ app.route("/terminal", methods=["POST", "GET"])
def terminal():
    copias = 1
    global pathDirectorioActual
    comando_recibido = request.args.get("comando_a_enviar")
    if (comando_recibido is not None):
        comando_seccionado = comando_recibido.split("-")
        if(comando_seccionado[0] == "createf"):
            nombre_del_archivo = pathDirectorioActual+"/" + \
                comando_seccionado[1] + ".txt"
            file_handler = open(nombre_del_archivo, 'w')
            file_handler.close()
            # actualUser.crearArchivo(comando_seccionado[1],funcion_que_devuelve_inodo_del_dir_Actual)
        elif comando_seccionado[0] == "cd":
            if comando_seccionado[1]== ".." or comando_seccionado[1]== "../":
                separarPath =pathDirectorioActual.split("/")
                words = 0
                pathDirectorioActual =""
                for word in separarPath:
                    if words < len(separarPath)-1:
                        words+=1
                        pathDirectorioActual +=  word + "/"
                    else:
                        pathDirectorioActual.rstrip("/")
                        break
            else:
                pathDirectorioActual += "/"+comando_seccionado[1] 
            print("path directorio actual"+pathDirectorioActual)   
        elif(comando_seccionado[0] == "createdir"):
            nombre_del_directorio = pathDirectorioActual +"/"+ comando_seccionado[1]
            os.mkdir(nombre_del_directorio)
        elif(comando_seccionado[0] == "edit"):
            nombre_del_archivo = pathDirectorioActual+"/" + \
                comando_seccionado[1] + ".txt"
            file_handler = open(nombre_del_archivo, 'a')
            file_handler.write(comando_seccionado[2]+"\n")
            file_handler.close()
        elif(comando_seccionado[0] == "delete"):
            nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + ".txt"
            os.remove(nombre_del_archivo)
        elif(comando_seccionado[0] == "deletedir"):
            nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1]
            os.rmdir(nombre_del_archivo)
        elif(comando_seccionado[0] == "rename"):
            nombre_del_archivo_viejo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + ".txt"
            nombre_del_archivo_nuevo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[2] + ".txt"
            os.rename(nombre_del_archivo_viejo, nombre_del_archivo_nuevo)
        elif(comando_seccionado[0] == "renamedir"):
            nombre_del_archivo_viejo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1]
            nombre_del_archivo_nuevo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[2]
            os.rename(nombre_del_archivo_viejo, nombre_del_archivo_nuevo)
        elif(comando_seccionado[0] == "copy"):
            nombre_del_archivo_original = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + ".txt"
            nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                comando_seccionado[1] + "(copy("+str(copias)+")).txt"
            while True:
                if os.path.exists(nombre_del_archivo):
                    copias += 1
                    nombre_del_archivo = "./files/"+actualUser._Nombre+"/" + \
                        comando_seccionado[1] + "(copy("+str(copias)+")).txt"
                else:
                    break
            file_handler_original = open(nombre_del_archivo_original, 'r')
            file_handler = open(nombre_del_archivo, 'w')
            file_handler.write(file_handler_original.read())
            file_handler.close()
            file_handler_original.close()
    else:
        print("Comando is None")
    return render_template("terminal.html", usr=actualUser._Nombre)


@app.route('/dataManager', methods=['GET', 'POST'])
def dataManager():
    global pathDirectorioActual
    if request.is_json:
        data = request.get_json()
        if(data.get("comando") == "read"):
            nombre_del_archivo = pathDirectorioActual+"/" + \
                data.get("nombre") + ".txt"
            file_handler = open(nombre_del_archivo, 'r')
            file_content1 = dict()
            count = 0
            Lines = file_handler.readlines()
            for line in Lines:
                file_content1[count] = line.strip()
                count += 1
            file_handler.close()
            return file_content1
        elif (data.get("comando") == "list"):
            direccion = pathDirectorioActual+"/"
            dir_content = dict()
            count = 0
            for dir_files in ls1(direccion):
                dir_content[count] = dir_content.get(count, dir_files)
                count += 1
            return dir_content


def ls1(path):
    return [obj for obj in listdir(path) if isfile(path + obj)]


"""
VAMOS A GUARDAR TODA LA INFORMACIÓN DEL USUARIO ACTUAL DENTRO DE SU ARCHIVO MEMORIA
def guardarPartida(actualUser):´
*Abrimos el archivo memoria del usuario
*Escribismos toda la informacion de la estructura del usuario en su archivo de memoria 

VAMOS A INICIALIZAR TODA LA INFORMACIÓN DEL ARCHIVO MEMORIA DEL USUARIO DENTRO DE SUS ESTRCUTURAS
def cargarPartida(actualUser):
* Buscar el archivo del usuario
* Extraer todo del archivo memoria a la estructura del usuario
"""


app.run(debug=True, port=80)