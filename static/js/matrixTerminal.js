function terminalMatrix() {
    var matrixTerminal = new Terminal()

    defineMatrix(matrixTerminal)

    $(".terminalMain").append(matrixTerminal.html)
    matrixTerminal.input("Admin@Admin:~$ ", function (comando) {
        matrixTerminal.print(comando)
        //Proceso de recibir comandos
        //Comunicar con Python para abrir archivos y operarlos
        //Interpretar y operar en base a comandos, OWR archivos del usuario
    })
}
function defineMatrix(matrixTerminal) {
    matrixTerminal.setHeight("200px")
    matrixTerminal.setWidth('1200px')
    matrixTerminal.setTextColor("#00FF41")
}
