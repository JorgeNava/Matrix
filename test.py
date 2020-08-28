import os
copias = 0
path_del_archivo_original = "./files/Jorge/dirA" + \
    "/" + "poke" + ".txt"
nombre_copia = "./files/Jorge/dirA"+"/" + \
    "poke" + " copy("+str(copias)+").txt"
while True:
    if os.path.exists(nombre_copia):
        copias += 1
        nombre_copia = "./files/Jorge/dirA"+"/" + \
            "poke" + " copy("+str(copias)+").txt"
    else:
        break
file_handler_original = open(path_del_archivo_original, 'r')
file_handler = open(nombre_copia, 'w')
file_handler.write(file_handler_original.read())
file_handler.close()
file_handler_original.close()
nombre_copia = "a" + " copy("+str(copias) + ")"
"""
FALTA
    PRIORIDAD CONCEPTO
    2   |   GUARDAR INFORMACION EN MEMORIA
    2   |   EXTRAER INFORMACION DE MEMORIA - LINEA 31 usuario.py
    2   |   METER FUNCIONES DE REGISTROS EN app.py (GUSTAVO)
    3   |   CREAR COMANDO PARA MOSTRAR EN QUE CARPETA ESTAMOS
    4   |   CREAR COMANDO PARA ABRIR ARCHIVO TXT start <file_name> usando os.startfile('file.txt')
    5   |   POSIBLE (CREAR COMANDO PARA MOVER ARCHIVO DE LUGAR)
"""
