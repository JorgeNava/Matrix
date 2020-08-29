import os
import pickle
from usuario import Usuario
# LISTO
"""strin = "./files/Jorge/poke.txt"
openPath = strin.replace("/", "\\")
os.startfile(openPath)"""
"""
FALTA
    PRIORIDAD CONCEPTO

"""
"""
usr = Usuario("Gustavo", "cisco")
#usr._Directorio[0]._Inodos = [10,15,42,47,26,34,15,98,58,10]
memoryFile = "./files/memorias/Gustavo.txt"
memoryData = open(memoryFile,'wb')
pickle.dump(usr,memoryData)
memoryData.close()
"""
"""
memoryFile = "./files/memorias/Gustavo.txt"
memoryData = open(memoryFile,'rb')
usr2 = pickle.load(memoryData)

print(usr2._Directorio[0]._NombreDir)
print(usr2._Directorio[0]._Nombre)
print(usr2._Directorio[0]._Inodos)
memoryData.close()"""
