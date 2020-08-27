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
            nombre_del_archivo = comando_seccionado[1] + ".txt"
            path_del_archivo = pathDirectorioActual + \
                "/" + nombre_del_archivo
            file_handler = open(path_del_archivo, 'w')
            file_handler.close()
            # Registramos el archivo en la estructura
            actualUser.crearArchivo(nombre_del_archivo)
            """for i in range(1):
                print("Nombre archivo: " + actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: " +
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: " +
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: " + str(actualUser._Inodo[i]._Libre))
                print(actualUser._Directorio[0]._Nombre)
                print(actualUser._Directorio[0]._Inodos)"""
        elif comando_seccionado[0] == "cd":
            if comando_seccionado[1] == ".." or comando_seccionado[1] == "../":
                separarPath = pathDirectorioActual.split("/")
                words = 0
                pathDirectorioActual = ""
                for word in separarPath:
                    if words < len(separarPath)-1:
                        words += 1
                        pathDirectorioActual += word + "/"
                    else:
                        pathDirectorioActual.rstrip("/")
                        break
            else:
                pathDirectorioActual += "/"+comando_seccionado[1]
            '''
            PENDIENTE
            print("Inodo del directorio actual: "+ \
                  actualUser._InodoDelDirectorioActual)
            actualUser.actualizar_dir_actual_cada_CD(comando_seccionado[1])
            print("Inodo del directorio actual: "+actualUser._InodoDelDirectorioActual)'''
        elif(comando_seccionado[0] == "createdir"):
            nombre_del_directorio = pathDirectorioActual + \
                "/" + comando_seccionado[1]
            os.mkdir(nombre_del_directorio)
            nombre_del_directorio_a_registrar = comando_seccionado[1]
            actualUser.crearDirectorio(nombre_del_directorio_a_registrar)
            '''for i in range(5):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))
                print("Nombre directorio: "+ \
                      actualUser._Directorio[i]._NombreDir)
                print("inodo directorio: "+ \
                      str(actualUser._Directorio[i]._InodoDir))
                CHECAR SI LA LIL DEBE EMPEZAR EN 0 O 1'''
        elif(comando_seccionado[0] == "edit"):
            nombre_del_archivo = pathDirectorioActual + \
                "/" + comando_seccionado[1] + ".txt"
            file_handler = open(nombre_del_archivo, 'a')
            file_handler.write(comando_seccionado[2]+"\n")
            file_handler.close()
            nombre_del_archivo_a_editar = comando_seccionado[1] + ".txt"
            '''FALTO ARREGLAR LO DEL TAMAÑO del achivo
            for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))'''
            actualUser.editFile(nombre_del_archivo_a_editar)
            '''for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))'''
        elif(comando_seccionado[0] == "delete"):
            nombre_del_archivo = pathDirectorioActual + "/" + \
                comando_seccionado[1] + ".txt"
            os.remove(nombre_del_archivo)
            nombre_del_archivo_a_borrar = comando_seccionado[1] + ".txt"
            '''PROBLEMA SOLO FUNCIONA BIEN LA PRIMERA VEZ
            for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))
                print(actualUser._Directorio[0]._Nombre)
                print(actualUser._Directorio[0]._Inodos)
            actualUser.borrarArchivo(nombre_del_archivo_a_borrar)
            print("----------------------------------------------------------------")
            for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))
                print(actualUser._Directorio[0]._Nombre)
                print(actualUser._Directorio[0]._Inodos)'''
        elif(comando_seccionado[0] == "deletedir"):
            nombre_del_archivo = pathDirectorioActual + \
                "/" + comando_seccionado[1]
            os.rmdir(nombre_del_archivo)
            nombre_del_directorio_a_borrar = comando_seccionado[1]
            ''' CHECAR BIEN FUNCION DE BORRAR DIRECTORIO EN USUARIO.PY YA QUE SOLO FUNCIONA 1 VEZ
            for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))
                print("Nombre directorio "+str(i)+":"+ \
                      actualUser._Directorio[i]._NombreDir)
                print("inodo directorio "+str(i)+":"+ \
                      str(actualUser._Directorio[i]._InodoDir))
                print(actualUser._Directorio[i]._Nombre)
                print(actualUser._Directorio[i]._Inodos)'''
            actualUser.borrarDirectorio(nombre_del_directorio_a_borrar)
            print("----------------------------------------------------------------")
            '''for i in range(3):
                print("Nombre archivo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de creación: "+ \
                      actualUser._Inodo[i]._Fecha_de_creacion)
                print("Fecha de ult modificación: "+ \
                      actualUser._Inodo[i]._Fecha_ult_modificacion)
                print("Libre: "+ str(actualUser._Inodo[i]._Libre))
                print("Nombre directorio "+str(i)+":"+ \
                      actualUser._Directorio[i]._NombreDir)
                print("inodo directorio "+str(i)+":"+ \
                      str(actualUser._Directorio[i]._InodoDir))
                print(actualUser._Directorio[i]._Nombre)
                print(actualUser._Directorio[i]._Inodos)    '''
        elif(comando_seccionado[0] == "rename"):
            nombre_del_archivo_viejo = pathDirectorioActual + \
                "/" + comando_seccionado[1] + ".txt"
            nombre_del_archivo_nuevo = pathDirectorioActual + \
                "/" + comando_seccionado[2] + ".txt"
            os.rename(nombre_del_archivo_viejo, nombre_del_archivo_nuevo)
            nombre_del_archivo_viejo_a_registrar = comando_seccionado[1] + ".txt"
            nombre_del_archivo_nuevo_a_registrar = comando_seccionado[2] + ".txt"
            actualUser.renameFile(
                nombre_del_archivo_viejo_a_registrar, nombre_del_archivo_nuevo_a_registrar)
            '''for i in range(3):
                print("Nombre archivo nuevo: "+ actualUser._Inodo[i]._Nombre)
                print("Fecha de ult modificación: "+ actualUser._Inodo[i]._Fecha_ult_modificacion)'''
        elif(comando_seccionado[0] == "renamedir"):
            nombre_del_archivo_viejo = pathDirectorioActual + \
                "/" + comando_seccionado[1]
            nombre_del_archivo_nuevo = pathDirectorioActual + \
                "/" + comando_seccionado[2]
            os.rename(nombre_del_archivo_viejo, nombre_del_archivo_nuevo)

            nombre_del_directorio_viejo_a_registrar = comando_seccionado[1] + ".txt"
            nombre_del_directorio_nuevo_a_registrar = comando_seccionado[2] + ".txt"
            actualUser.renombrarDirectorio(
                nombre_del_directorio_viejo_a_registrar, nombre_del_directorio_nuevo_a_registrar)
            '''for i in range(3):
                print("Nuevo Nombre directorio: "+ \
                      actualUser._Directorio[0]._NombreDir)
                print("Fecha de ult modificación: "+ actualUser._Inodo[i]._Fecha_ult_modificacion)'''
        elif(comando_seccionado[0] == "copy"):
            nombre_del_archivo_original = pathDirectorioActual + \
                "/" + comando_seccionado[1] + ".txt"
            nombre_del_archivo = pathDirectorioActual+"/" + \
                comando_seccionado[1] + "(copy("+str(copias)+")).txt"
            while True:
                if os.path.exists(nombre_del_archivo):
                    copias += 1
                    nombre_del_archivo = pathDirectorioActual+"/" + \
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


def ls1(path):
    # return [obj for obj in listdir(path) if isfile(path + obj)]
    contenido_de_dir = [".", ".."]
    with os.scandir(path) as archivos:
        for archivo in archivos:
            contenido_de_dir.append(archivo.name)
    return contenido_de_dir


app.run(debug=True, port=80)
