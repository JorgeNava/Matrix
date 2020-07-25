import os

filename = "./users/"
filename += input("Username: ")
filename += ".txt"

file = open(filename, "w")
file.write("Primera linea" + os.linesep)
file.write("Segunda línea")
file.write("Segunda línea")
file.write("Segunda línea")
file.close()
