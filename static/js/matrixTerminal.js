function terminalMatrix() {
    //Creación de objeto terminal
    var matrixTerminal = new Terminal()

    //Inicializacion de terminal
    defineTerminal(matrixTerminal)

    //Implementacion de terminal en html
    $(".terminalMain").append(matrixTerminal.html)

    //Función recursiva que evaluar y opera comandos ingresados
    inputCommandTerminal(matrixTerminal)
}

/*
    Se evaluan los comandos ingresados en la terminal
    llamando a funciones de la terminal y haciendo
    consultas/operaciones a los archivos txt (memoria?)
    de cadausuario.
*/
function inputCommandTerminal(matrixTerminal) {
    matrixTerminal.input("Admin@Admin:~$", function (comando) {
        //Se extrae el valor pasado por Flask para llamar a una funcion py que abra el archivo del usr
        let usr = '{{us}}' //Esta parte requiere investigacion
        switch (comando) {
            case "clr":
                clearTerminal(matrixTerminal)
                break;
            case "read":
                readFile(matrixTerminal, usr)
                break
            default:
                matrixTerminal.print('"' + comando + '" no es un comando reconocido...')
                break;
        }
        inputCommandTerminal(matrixTerminal)

        //Proceso de recibir comandos
        //Comunicar con Python para abrir archivos y operarlos
        //Interpretar y operar en base a comandos, OWR archivos del usuario
    })
}

//Abrira y leera el contenido del arhivo usr.txt usando una funcion en Flask
function readFile(matrixTerminal, usr) {
    matrixTerminal.print("read: " + usr)
    //Debe conectarse con escribirEnArchivo.py
}


//Limpieza de terminal
function clearTerminal(matrixTerminal) {
    matrixTerminal.clear()
}

//Inicializacion de terminal
function defineTerminal(matrixTerminal) {
    matrixTerminal.setHeight("200px")
    matrixTerminal.setWidth('1200px')
    matrixTerminal.setTextColor("#00FF41")
}