//Creación de objeto terminal
let matrixTerminal = new Terminal()

function terminalMatrix() {

    //Inicializacion de terminal
    defineTerminal(matrixTerminal)

    //Implementacion de terminal en html
    $(".terminalMain").append(matrixTerminal.html)

    //Función recursiva que evaluar y opera comandos ingresados
    inputCommandTerminal(usr, inodo_del_directorio_actual)
}

/*
    Se evaluan los comandos ingresados en la terminal
    llamando a funciones de la terminal y haciendo
    consultas/operaciones a los archivos txt (memoria?)
    de cadausuario.
*/
function inputCommandTerminal(usuario, inodo_del_directorio_actual) {
    matrixTerminal.input(usr + "@" + usr + ":~$", function (comando) {
        //Se extrae el valor pasado por Flask para llamar a una funcion py que abra el archivo del usr
        //LOGRE PASAR INFORMACION DE FLASK A JS
        // let usr = '{{usr}}' Esta parte requiere investigacion

        //partir el comando en seccion
        //cada seccion estara dividida por un espacio 
        let comandoSeccionado = comando.split(" ");

        switch (comandoSeccionado[0]) {
            case "clr":
                clearTerminal()
                break;
            case "read":
                readFile()
                break
            case "write":
                writeFile(usuario)
                break
            case "list":
                list(inodo_del_directorio_actual)
                break
            case "createdir":
                matrixTerminal.input("", createdir(comandoSeccionado[1]))
                break
            default:
                matrixTerminal.print('"' + comando + '" no es un comando reconocido...')
                break;
        }
        inputCommandTerminal(usuario, inodo_del_directorio_actual)

        //Proceso de recibir comandos
        //Comunicar con Python para abrir archivos y operarlos
        //Interpretar y operar en base a comandos, OWR archivos del usuario
    })
}

//Abrira y leera el contenido del archivo usr.txt usando una funcion en Flask
function readFile() {
    matrixTerminal.print("HOLA")
    //Debe conectarse con escribirEnArchivo.py
}
//Abrira y escribira el contenido del archivo usr.txt usando una funcion en Flask
function writeFile(usr) {
    matrixTerminal.print("write: " + usr)
    //Debe conectarse con escribirEnArchivo.py
}

//Creara un directorio
function createdir(nombre_del_archivo) {
    matrixTerminal.print("creating " + nombre_del_archivo + "...")
    //Debe conectarse con escribirEnArchivo.py
}

//Imprimir todos los nombre y pesos de los archivos que tenemos en el directorio en el que nos encotramos
function list(inodo_del_directorio_actual) {

    //mandar string python con información de que necesitamos recibir un JSON con información de nuestro directorio actual
    //pasamos el comando y el inodo_del_directorio_actual para que python realice la busqueda y nos mande el JSON
    //recibimos JSON y lo imprimimos en la consola
}

//Limpieza de terminal
function clearTerminal() {
    matrixTerminal.clear()
}

//Inicializacion de terminal
function defineTerminal() {
    matrixTerminal.setHeight("200px")
    matrixTerminal.setWidth('1200px')
    matrixTerminal.setTextColor("#00FF41")
}