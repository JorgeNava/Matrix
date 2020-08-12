class Directorio:
    _NombreDir = ""  # Nombre del directorio
    _InodoDir = 0  # Inodo del directorio
    _Inodos = []  # Inodos de los archivos que guarda este directorio
    _Nombre = []  # Nombre de los archivos que guarda este directorio
    _Libre = 0  # Estado del directorio 0 si no existe ese, 1 si ya existe

    def __init__(self, _Libre):
        self._Libre = _Libre

    def __str__(self):
        return "{} {} {}".format(self._Inodos, self._Nombre, self._Libre)

#    def crearDirectorio(self, nombre_del_directorio, inodo_del_directorio):
        # El usuarios ingresa createdir <nombre_del_directorio>
        # Se busca un directorio libre dentro del arreglo de directorios del usuario "esta parte va en usuario"
        # inodo_del_directorio es obtenido desde el obj usuario y se le agega al inodod de este directorio
        # El campo libre de este directorio pasa a estar ocupado, que es 0
        # Nota: quitar inodo de LIL
        # Nota: Actualizar los datos en el arreglo de clase Inodo del usuario con los datos de este nuevo directorio

#    def agregarArchivoADirectorio(self, inodo_del_archivo, nombre_del_archivo):
        # EL usuario llama creatf <nombre_de_archivo> despues de moverse usando cd a este directorio
        # inodo_del_archivo  se saca de la LIL y se le asigna dentro de este directorio
        # inodo_del_archivo y nombre_Del_archivo se actualiza dentro del arreglo Inodo del usuario
