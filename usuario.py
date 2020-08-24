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
    _PathDirectorios = []
    _NombreDelDirectorioActual =""
    def __init__(self, _Nombre, _Contraseña):
        self._Nombre = _Nombre
        self._Contraseña = _Contraseña
        self._InodoDelDirectorioActual = 0
        self._NombreDelDirectorioActual =_NombreDelDirectorioActual
        self._InodoDelDirectorioPapa = 0
        self._PathDirectorios.append({0:"root"})
        for i in range(lists_Size):
            self._LIL.append(i)
            self._LBL.append(i)
            self._Inodo.append(Inodo("", 0, "", "", True, ""))
            self._Directorio.append(Directorio())


def crearArchivo(self, nombre_del_archivo):
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
    inodo_del_nuevo_archivo = self._LIL.pop(0)

    # Asignamos los nuevos valores al inodo extraido
    self._Inodo[inodo_del_nuevo_archivo]._Nombre = nombre_del_archivo
    self._Inodo[inodo_del_nuevo_archivo]._Fecha_de_creacion = date.today(
    ).strftime("%d/%m/%Y")
    self._Inodo[inodo_del_nuevo_archivo]._Fecha_ult_modificacion = date.today(
    ).strftime("%d/%m/%Y")
    self._Inodo[inodo_del_nuevo_archivo]._Libre = False
    self._Inodo[inodo_del_nuevo_archivo]._Permisos = "rwx"

    #buscamos indice en directorio
    indice_del_directorio_actual=buscarIndiceDeDirectorioPorInodo(self._InodoDelDirectorioActual)
    # Asignamos los nuevos valores al directorio correspondiente
    self._Directorio[indice_del_directorio_actual]._Inodos.append(
        inodo_del_nuevo_archivo)
    self._Directorio[indice_del_directorio_actual]._Nombre.append(
        nombre_del_archivo)
    self._Directorio[indice_del_directorio_actual]._Libre = False


def renameFile(self, nombre_del_archivo, nuevo_nombre_del_archivo):
    """ Algoritmo:
    *el usuario corre rename <nombre>
    *Buscar el inodo de ese archivo
    *Cambiamos el nombre del inodo correspondiente al nuevo nombre
    *Actualizamos la informacion dentro del directorio actual
    *Actualizamos archivo
   """
    inodo_del_archivo = buscarInodoPorNombreArchivo(nombre_del_archivo)
    self._Inodo[inodo_del_archivo]._Nombre = nuevo_nombre_del_archivo
    actualizarNombresDeArchivosEnDirectorios(self._InodoDelDirectorioActual)
    actualizarArchivo(inodo_del_archivo)
   # LLAMAR A FUNCION ACTUALIZAR DIRECTORIO
    # actualizarArchivo


def borrarArchivo(self, nombre_del_archivo):
    """ Algoritmo:
    *Buscamos el inodo del archivo que se desea borrar
    *Borramos la información de este archivo del directorio en el que se encuentre (dir_actual)
    *Borramos la información del inodo que poseia
    *Liberar el inodo que poseia 
    *Agregar inodo liberado a LIL
   """
   numDirectorio =0
   numInodo = 0
   inodo_del_archivo = buscarInodoPorNombreArchivo(nombre_del_archivo)
   for directorio in self._Directorio:
        if directorio._InodoDir == self._InodoDelDirectorioActual:
           for inodoArchivo in directorio._Inodos:
                if inodoArchivo == numInodo:
                    self._Directorio[numDirectorio]._Inodos[numInodo] = -1
                    self._Directorio[numDirectorio]._Nombre[numInodo] = ""
                else:
                    numInodo+=1
        else:
            numDirectorio+=1
    
    #Mandamos llamar a liberar inodo
    liberarInodo(inodo_del_archivo)


def editFile(self, nombre_del_archivo):
    """ Algoritmo:
    *el usuario corre edit <nombre>
    *Buscar el inodo de ese archivo
    *Actualizamos archivo
   """
    inodoDelArchivo =buscarInodoPorNombreArchivo(nombre_del_archivo)
    actualizarArchivo(inodoDelArchivo)


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
    *Si el nombre del archivo es .. eliminamos el directorio del diccionario y a inodo actual asignamos los valores del diccionario
    *Si el nombre del archivo es diferente de .. Recorrer lista _Directorio hasta que el nombre de uno de ellos coincidia con el ingresado
   """
    if nombre_del_directorio == "..":
        self._PathDirectorio.pop(len(self._PathDirectorio-1))
        self._InodoDelDirectorioActual = self._PathDirectorio[len(self._PathDirectorio-1)].keys()
        self._NombreDelDirectorioActual = self._PathDirectorio[len(self._PathDirectorio-1)].values()
    else:
        for directorio in self._Directorio:
            if directorio._NombreDir == nombre_del_directorio:
                self._PathDirectorio.append({directorio._InodoDir:directorio._NombreDir})
                self._NombreDelDirectorioActual = nombre_del_directorio
                self._InodoDelDirectorioActual = directorio._InodoDir
                break

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
    numDir=0
    for directorioLibre in self-_Directorio:
        if directorioLibre._Libre == True:
            inodo_del_nuevo_directorio = self._LIL.pop(0)
            self._Directorio[numDir]._InodoDir = inodo_del_nuevo_directorio
            self._Directorio[numDir]._NombreDir = nombre_del_directorio
            self._Directorio[numDir]._Libre = False
            #Se actualiza Inodo ahora
            self._Inodo[inodo_del_nuevo_directorio]._Nombre = nombre_del_directorio
            self._Inodo[inodo_del_nuevo_directorio]._Fecha_de_creacion = date.today().strftime("%d/%m/%Y")
            self._Inodo[inodo_del_nuevo_directorio]._Fecha_ult_modificacion = date.today().strftime("%d/%m/%Y")
            self._Inodo[inodo_del_nuevo_directorio]._Libre = False
            self._Inodo[inodo_del_nuevo_directorio]._Permisos = "rwx"
            break
        else:
            numDir+=1

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
            

def borrarDirectorio(self, nombre_del_directorio):
    """
    * Buscamos el directorio que corresponda con el nombre ingresado
    * Inicializamos de vuelta todos sus valores a 0 o null
    * Dar de baja la información de su inodo en el arreglo _Inodo del usuario
    * Se devuelve su inodo a LIL
    """
    numDir=0
    inodo_del_directorio= buscarInodoPorNombreArchivo(nombre_del_directorio)
    for directorio in self._Directorio:
        if directorio._InodoDir == inodo_del_directorio:
            self._Directorio[numDir]._InodoDir = -1
            self._Directorio[numDir]._NombreDir = ""
            self._Directorio[numDir]._Libre = True
            self._Directorio[numDir]._Inodos.clear()
            self._Directorio[numDir]._Nombre.clear()
            break
         ''' * Dar de baja la información de su inodo en el arreglo _Inodo del usuario
            * Se devuelve su inodo a LIL'''
        else:
            numDir+=1

def renombrarDirectorio(self, nombre_del_directorio, nuevo_nombre_del_directorio):
    """ Algoritmo:
    *el usuario corre renameDir <nombre>
    *Buscar el inodo del del directorio deseado
    *Cambiamos el nombre del directorio al nuevo nombre, para buscarlo usamos su inodo
    *Actualizamos la informacion dentro del directorio actual
    *Actualizamos fecha_de_modificacion y otras cosas (si hay mas cosas que actualizar)
   """

def liberarInodo(self, inodo_a_liberar):
    """ Algoritmo
    * Usamos ese inodo_a_liberar como indice de _Inodo[] del usario
    * Devolvemos todos sus atributos a 0 o null
    * Se agrega ese inodo_a_liberar a _LIL[]
    """
    self._Inodo[inodo_a_liberar]._Nombre = ""
    self._Inodo[inodo_a_liberar]._Tamanio = 0
    self._Inodo[inodo_a_liberar]._Fecha_de_creacion = ""
    self._Inodo[inodo_a_liberar]._Fecha_ult_modificacion = ""
    self._Inodo[inodo_a_liberar]._Libre = True
    self._Inodo[inodo_a_liberar]._Permisos = ""
    self._LIL.append(inodo_a_liberar)
def buscarIndiceDeDirectorioPorInodo(self,inodo_del_directorio):
    numDirectorio =0
    for directorio in self._Directorio:
            if directorio._InodoDir == inodo_del_directorio:
                break
            else:
                numDirectorio+=1
    return numDirectorio
