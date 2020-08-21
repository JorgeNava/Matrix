from datetime import date
from directorio import Directorio
from inodos import Inodo
import os
lists_Size = 100


class Usuario:
    _Nombre = ""
    _Contraseña = ""
    _LIL = []
    _LBL = []
    _Inodo = []
    _Directorio = []
    _InodoDelDirectorioActual = 0
    _InodoDelDirectorioPapa = 0
    _NombreDelDirectorioActual =""
    def __init__(self, _Nombre, _Contraseña):
        self._Nombre = _Nombre
        self._Contraseña = _Contraseña
        self._InodoDelDirectorioActual = 0
        self._NombreDelDirectorioActual =_NombreDelDirectorioActual
        self._InodoDelDirectorioPapa = 0
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
    *Actualizamos la informacion dentro del directorio actual
    *Actualizamos archivo
   """
    inodo_del_archivo = buscarInodoPorNombreArchivo(nombre_del_archivo)
    self._Inodo[inodo_del_archivo]._Nombre = nuevo_nombre_del_archivo
    actualizarNombresDeArchivosEnDirectorios(inodo_del_directorio_actual)
    actualizarArchivo(inodo_del_archivo)
   # LLAMAR A FUNCION ACTUALIZAR DIRECTORIO
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
    num_inodo =0
    for inodo in self._Inodo:
        if inodo._Nombre == nombre_del_archivo:
            break
        else:
            num_inodo+=1
    return num_inodo


def actualizar_dir_actual_cada_CD(self, nombre_del_directorio):
    """ Algoritmo: ES PARA ACTUALIZAR EL ATRIBUTO _InodoDelDirectorioActual CADA VEZ QUE SE HAGA CD
    *Recorrer lista _Directorio hasta que el nombre de uno de ellos coincidia con el ingresado
    *devolver numero de inodo
   """
   num_dir =0
    for directorio in self._Directorio:
        if directorio._NombreDir == nombre_del_directorio:
            self._NombreDelDirectorioActual = nombre_del_directorio
            self._InodoDelDirectorioActual = num_dir
            break
        else:
            num_dir+=1

def actualizarArchivo(self, inodo_del_archivo):
    """ Algoritmo:
    *Es llamado por otras funciones
    *Modificamos la fecha de modificacion del inodo correspondiete
    *Modificamos el tamaño del inodo correspondiente
   """
    self._Inodo[inodo_del_archivo]._Fecha_ult_modificacion = day.today().strftime("%d/%m/%Y")
    self._Inodo[inodo_del_archivo]._Tamanio = os.path.getsize(os.path.abspath(self._NombreDelDirectorioActual+"/"+self._Inodo[inodo_del_archivo]._Nombre+".txt")) 

def crearDirectorio(self, nombre_del_directorio):
    """
    # El usuarios ingresa createdir <nombre_del_directorio>
    # Se busca un directorio libre dentro del arreglo de directorios del usuario
    # Obtener un inodo de la LIL este sera inodo_del_nuevo_directorio
    # inodo_del_nuevo_directorio sera puesto dentro del primer directorio libre que se encuentre de la lista de directoris del usuario
    # Se añadira el nombre_del_directorio al atributo de este directorio
    # Se actualizara su atributo _Libre a False
    # Actualizamos nuestra lista de inodos _Inodo con la inforamción que se acaba de ocupar
    """


def actualizarNombresDeArchivosEnDirectorios():
    """ SE VA A UTILIZAR EN RENOMBRAR
    * Se introduce el inodo del directorio al cual queremos actualizar los nombres de sus archivos
    * Buscamos ese directorio dentro de nuestro lista de directorios _Directorio 
    * Buscamos los inodos de sus archivos dentro del arreglo _Inodos[]
    * Actualizamos los valores de _Nombre[] de acuerdo a su igual en el arreglo del usuario _Inodo[]
    """
    numDir = 0
    numNombre = 0
    for directorio_a_comparar in self._Directorio:
        if self._InodoDelDirectorioActual == directorio_a_comparar._InodoDir: # se selecciona el directorio que vamos a usar
            for inodoDentroDelDirectorio in directorio_a_comparar._Inodos:
                if inodoDentroDelDirectorio != -1: # se filtran los inodos que estan ligados a archivos 
                    self._Directorio[numDir]._Nombre[numNombre] = self._Inodo[inodoDentroDelDirectorio]._Nombre
                    numNombre+=1
                else:
                    break
        numDir+=1
            

def borrarDirectorio(self, inodo_del_directorio):
    """
    * Buscamos el directorio que corresponda con el inodo ingresado
    * Inicializamos de vuelta todos sus valores a 0 o null
    * Dar de baja la información de su inodo en el arreglo _Inodo del usuario
    * Se devuelve su inodo a LIL
    """


def renombrarDirectorio(self, nombre_del_directorio, nuevo_nombre_del_directorio):
    """ Algoritmo:
    *el usuario corre renameDir <nombre>
    *Buscar el inodo del del directorio deseado
    *Cambiamos el nombre del directorio al nuevo nombre, para buscarlo usamos su inodo
    *Actualizamos la informacion dentro del directorio actual
    *Actualizamos fecha_de_modificacion y otras cosas (si hay mas cosas que actualizar)
   """


def moverADirectorio(self, nombre_del_siguiente_directorio):
    """ Algoritmo:
    * Se guarda el inodo del directorio actual en el atributio _Inodo_del_directorio_papa del usuario
    * Buscamos el inodo del directorio siguiente en base a su nombre y se guarda en _InodoDelDirectorioActual del usuario
    """


def liberarInodo(self, inodo_a_liberar):
    """ Algoritmo
    * Usamos ese inodo_a_liberar como indice de _Inodo[] del usario
    * Devolvemos todos sus atributos a 0 o null
    * Se agrega ese inodo_a_liberar a _LIL[]
    """
