from flask import Flask, render_template, session, request, jsonify
import os
from usuario import Usuario
import json
import shutil
from os import listdir
from os.path import isfile, isdir


app = Flask(__name__)
app.secret_key = "secreto"

users = [Usuario("admin", "cisco"), Usuario(
    "Gustavo", "cisco"), Usuario("Jorge", "cisco")]

pathDirectorioActual = None

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
                actualUser._PathDirectorios.append({0: actualUser._Nombre})
        pathDirectorioActual = "./files/"+actualUser._Nombre
    return render_template("login.html")


@ app.route("/terminal", methods=["POST", "GET"])
def terminal():
    copias = 1
    global pathDirectorioActual
    comando_recibido = request.args.get("comando_a_enviar")
    if (comando_recibido is not None):
        comando_seccionado = comando_recibido.split("-")
        if(comando_seccionado[0] == "createf"):
            # LISTO
            nombre_del_archivo = comando_seccionado[1] + ".txt"
            path_del_archivo = pathDirectorioActual + \
                "/" + nombre_del_archivo
            file_handler = open(path_del_archivo, 'w')
            file_handler.close()
            actualUser.crearArchivo(comando_seccionado[1])
        elif comando_seccionado[0] == "cd":
            # LISTO
            nombre_del_directorio = comando_seccionado[1]
            if nombre_del_directorio == ".." or nombre_del_directorio == "../":
                separarPath = pathDirectorioActual.split("/")
                words = 0
                pathDirectorioActual = ""
                for word in separarPath:
                    if words < len(separarPath)-1:
                        words += 1
                        pathDirectorioActual += word + "/"
                    else:
                        pathDirectorioActual = pathDirectorioActual.rstrip("/")
                        break
            else:
                pathDirectorioActual += "/"+nombre_del_directorio
            actualUser.actualizar_dir_actual_cada_CD(nombre_del_directorio)
        elif(comando_seccionado[0] == "createdir"):
            # LISTO
            nombre_del_directorio = comando_seccionado[1]
            path_del_directorio = pathDirectorioActual + \
                "/" + nombre_del_directorio
            os.mkdir(path_del_directorio)
            actualUser.crearDirectorio(nombre_del_directorio)
        elif(comando_seccionado[0] == "edit"):
            # LISTO
            nombre_del_archivo = comando_seccionado[1] + ".txt"
            path_del_archivo = pathDirectorioActual + \
                "/" + nombre_del_archivo
            file_handler = open(path_del_archivo, 'a')
            file_handler.write(comando_seccionado[2]+"\n")
            file_handler.close()
            actualUser.editFile(comando_seccionado[1])
        elif(comando_seccionado[0] == "delete"):
            # LISTO
            if len(comando_seccionado) == 2:
                nombre_del_archivo = comando_seccionado[1] + ".txt"
            else:
                nombre_del_archivo = comando_seccionado[1] + \
                    " " + comando_seccionado[2] + ".txt"
            path_del_archivo = pathDirectorioActual + \
                "/" + nombre_del_archivo
            os.remove(path_del_archivo)
            print("path to delete[0]: ", path_del_archivo)
            actualUser.borrarArchivo(comando_seccionado[1])
        elif(comando_seccionado[0] == "deletedir"):
            # GUSTAVO - TRABAJANDO
            nombre_del_directorio = comando_seccionado[1]
            path_del_directorio = pathDirectorioActual + \
                "/" + nombre_del_directorio
            shutil.rmtree(path_del_directorio)
            actualUser.borrarDirectorio(nombre_del_directorio)
        elif(comando_seccionado[0] == "rename"):
            # LISTO
            nombre_del_archivo_viejo = comando_seccionado[1] + ".txt"
            nombre_del_archivo_nuevo = comando_seccionado[2] + ".txt"
            path_del_archivo_viejo = pathDirectorioActual + "/" + nombre_del_archivo_viejo
            path_del_archivo_nuevo = pathDirectorioActual + "/" + nombre_del_archivo_nuevo

            os.rename(path_del_archivo_viejo, path_del_archivo_nuevo)
            actualUser.renameFile(comando_seccionado[1], comando_seccionado[2])
        elif(comando_seccionado[0] == "renamedir"):
            # LISTO
            nombre_del_directorio_viejo = comando_seccionado[1]
            nombre_del_directorio_nuevo = comando_seccionado[2]
            path_del_directorio_viejo = pathDirectorioActual + \
                "/" + nombre_del_directorio_viejo
            path_del_directorio_nuevo = pathDirectorioActual + \
                "/" + nombre_del_directorio_nuevo
            os.rename(path_del_directorio_viejo, path_del_directorio_nuevo)
            actualUser.renombrarDirectorio(
                nombre_del_directorio_viejo, nombre_del_directorio_nuevo)
        elif(comando_seccionado[0] == "copy"):
            path_del_archivo_original = pathDirectorioActual + \
                "/" + comando_seccionado[1] + ".txt"
            path_copia = pathDirectorioActual+"/" + \
                comando_seccionado[1] + "(copy("+str(copias)+")).txt"
            while True:
                if os.path.exists(path_copia):
                    copias += 1
                    path_copia = pathDirectorioActual+"/" + \
                        comando_seccionado[1] + "(copy("+str(copias)+")).txt"
                else:
                    break
            file_handler_original = open(path_del_archivo_original, 'r')
            file_handler = open(path_copia, 'w')
            file_handler.write(file_handler_original.read())
            file_handler.close()
            file_handler_original.close()
            path_copia = comando_seccionado[1] + "(copy("+str(copias) + "))"
            actualUser.crearArchivo(path_copia)
    else:
        print("Comando is None")
    return render_template("terminal.html", usr=actualUser._Nombre)


@ app.route('/dataManager', methods=['GET', 'POST'])
def dataManager():
    global pathDirectorioActual
    if request.is_json:
        data = request.get_json()
        if(data.get("comando") == "read"):
            nombre_del_archivo = pathDirectorioActual + \
                "/" + data.get("nombre") + ".txt"
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

            inodo_de_archivo = 404

            for dir_files in ls1(direccion):
                # buscamos el inodo del archivo en base a su nombre
                if dir_files == ".":
                    inodo_de_archivo = actualUser._InodoDelDirectorioActual
                elif dir_files == "..":
                    inodo_de_archivo = actualUser._InodoDelDirectorioPapa
                else:
                    inodo_de_archivo = actualUser.buscarInodoPorNombreArchivo(
                        dir_files.rsplit(".")[0])
                dir_content[inodo_de_archivo] = dir_content.get(
                    inodo_de_archivo, dir_files)
            return dir_content
        elif(data.get("comando") == "actual"):
            current_path = {0: pathDirectorioActual}
            return current_path
        elif(data.get("comando") == "open"):
            openPath = pathDirectorioActual.replace("/", "\\")
            openPath += "\\"+data.get("nombre") + ".txt"
            os.startfile(openPath)
            current_path = {0: pathDirectorioActual}
            return current_path


def ls1(path):
    # return [obj for obj in listdir(path) if isfile(path + obj)]
    contenido_de_dir = [".", ".."]
    with os.scandir(path) as archivos:
        for archivo in archivos:
            contenido_de_dir.append(archivo.name)
    return contenido_de_dir


app.run(debug=True, port=80)
