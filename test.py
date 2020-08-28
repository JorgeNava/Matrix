import os
separarPath = ".files/Jorge/dirA/dirB".split("/")
words = 0
pathDirectorioActual = ""
for word in separarPath:
    if words < len(separarPath)-1:
        words += 1
        pathDirectorioActual += word + "/"
    else:
        pathDirectorioActual = pathDirectorioActual.rstrip("/")
        break
print(pathDirectorioActual)

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
