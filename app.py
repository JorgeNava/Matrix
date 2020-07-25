from flask import Flask, render_template, session, request

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
    """
    Idea - Podriamos hacer que la terminal mandará datos POST
    recibirlos aqui y tener un if con dos returns diferentes
    uno para cuando el POST aun no este ingresado y otro donde si
    en el segundo antes de hacer el return pondriamos funciones
    de READ y WRITE de los archivos correspondientes al usuario
    y luego mandamos la informacion solicitada como parametros 
    en el return.
    """
    """
    Idea - Las funciones dentro de matrixTerminal que estan dentro
    del switch podria devolver en los POST (dado que este Flask ya
    conoce el nombre del usuario, por lo tanto ya sabemos que archivo
    abrir) solamente datos como ¿tenemos que leer o escribir en ese 
    archivo?, ¿por que linea debemos empezar?/¿que esta buscando el
    usuario?, el valor que desea ingresar
    """
    """
    Conflicto - ¿Como vamos a enviar la información encontrada en la
    idea anterior devuelta al js para que sea impreso en la terminal?
    """
    # if request.method == "POST":
    #session["usuario"] = request.form["txtUsuario"]
    return render_template("terminal.html", usr=session["usuario"])


app.run(debug=True, port=80)
