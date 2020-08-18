import os

filename = "./files/Jorge/"
filename += input("Nombre del archivo: ")
filename += ".txt"

file = open(filename, "w")
file.write("Primera linea" + os.linesep)
file.write("Segunda línea")
file.write("Segunda línea")
file.write("Segunda línea")
file.close()
