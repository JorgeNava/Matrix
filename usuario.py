from directorio import Directorio
from inodos import Inodo

lists_Size = 100


class Usuario:
    _Nombre = ""
    _Contraseña = ""
    _LIL = []
    _LBL = []
    _Inodo = []
    _Directorio = []
    _InodoDelDirectorioActual = 0

    def __init__(self, _Nombre, _Contraseña):
        self._Nombre = _Nombre
        self._Contraseña = _Contraseña
        self._InodoDelDirectorioActual = 0
        for i in range(lists_Size):
            self._LIL.append(i)
            self._LBL.append(i)
            self._Inodo.append(Inodo("", 0, "", "", 1, ""))
            self._Directorio.append(Directorio(1))
