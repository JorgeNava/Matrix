from usuario import Usuario
from directorio import Directorio
from inodos import Inodo

lists_Size = 100


class testClass:

    def __init__(self, _Nombre, _Contraseña):
        self._Nombre = _Nombre
        self._Contraseña = _Contraseña
        self._InodoDelDirectorioActual = 0
        self._InodoDelDirectorioPapa = 0
        self._NombreDelDirectorioActual = ""
        self._LIL = []
        self._LBL = []
        self._Inodo = []
        self._Directorio = []
        self._PathDirectorios = []
        self.myInit()

    def myInit(self):
        self._PathDirectorios.append({0: self._Nombre})
        for i in range(lists_Size):
            self._LIL.append(i)
            self._LBL.append(i)
            self._Inodo.append(Inodo("", 0, "", "", True, ""))
            self._Directorio.append(Directorio())


testObje = testClass("Jorge", "CIso")

print(len(testObje._Inodo))
print(testObje._Inodo[0]._Tamanio)


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
