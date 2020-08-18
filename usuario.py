from datetime import date
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
            self._Inodo.append(Inodo("", 0, "", "", True, ""))
            self._Directorio.append(Directorio())


def crearArchivo(self, nombre_del_archivo, inodo_del_directorio_actual):
    """ Algoritmo:
    *el usuario corre creatf <nombre>
    *Se saca el primer inodo de LIL
    *Se crea el objeto inodo con sus respectivos datos para ese archivo
    *Se añade en el directorio correspondiente la información del nuevo archivo (inodo, nombre)
    """
    """
    SE USARA EN CREATF Y COPY
    """
    # Extremos el primer Inodo libre de LIL
    inodo_del_nuevo_archivo = self._LIL[0].pop

    # Asignamos los nuevos valores al inodo extraido
    self._Inodo[inodo_del_nuevo_archivo]._Nombre = nombre_del_archivo
    self._Inodo[inodo_del_nuevo_archivo]._Fecha_de_creacion = date.today(
    ).strftime("%d/%m/%Y")
    self._Inodo[inodo_del_nuevo_archivo]._Fecha_ult_modificacion = date.today(
    ).strftime("%d/%m/%Y")
    self._Inodo[inodo_del_nuevo_archivo]._Libre = False
    self._Inodo[inodo_del_nuevo_archivo]._Permisos = "rwx"

    # Asignamos los nuevos valores al directorio correspondiente
    self._Directorio[inodo_del_directorio_actual]._Inodos.append(
        inodo_del_nuevo_archivo)
    self._Directorio[inodo_del_directorio_actual]._Nombre.append(
        nombre_del_archivo)
    self._Directorio[inodo_del_directorio_actual]._Libre = False


def renameFile(self, nombre_del_archivo, inodo_del_directorio_actual, nuevo_nombre_del_archivo):
    """ Algoritmo:
    *el usuario corre rename <nombre>
    *Buscar el inodo de ese archivo
    *Cambiamos el nombre del inodo correspondiente al nuevo nombre
    *Actualizamos archivo
   """
    # actualizarArchivo


def borrarArchivo(self, nombre_del_archivo, inodo_del_directorio_actual):
    """ Algoritmo:
    *Buscamos el inodo del archivo que se desea borrar
    *Borramos la información de este archivo del directorio en el que se encuentre (dir_actual)
    *Borramos la información del inodo que poseia
    *Liberar el inodo que poseia 
    *Agregar inodo liberado a LIL
   """


def editFile(self, nombre_del_archivo, inodo_del_directorio_actual, nuevo_nombre_del_archivo):
    """ Algoritmo:
    *el usuario corre edit <nombre>
    *Buscar el inodo de ese archivo
    *Actualizamos archivo
   """
    # actualizarArchivo


def buscarInodoPorNombreArchivo(self, nombre_del_archivo):
    """ Algoritmo:
    *Recorrer lista _Inodo hasta que el nombre de uno de ellos coincidia con el ingresado
    *devolver numero de inodo
   """


def buscar_inodo_del_dir_actual(self, nombre_del_directorio):
    """ Algoritmo:
    *Recorrer lista _Directorio hasta que el nombre de uno de ellos coincidia con el ingresado
    *devolver numero de inodo
   """


def actualizarArchivo(self, inodo_del_archivo, inodo_del_directorio_actual):
    """ Algoritmo:
    *Es llamado por otras funciones
    *Modificamos la fecha de modificacion del inodo correspondiete
    *Modificamos el tamaño del inodo correspondiente
   """
