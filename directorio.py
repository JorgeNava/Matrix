class Directorio:
    _Inodos = []
    _Nombre = []
    _Libre = 0

    def __init__(self, _Inodos, _Nombre, _Libre):
        self._Inodos = _Inodos
        self._Nombre = _Nombre
        self._Libre = _Libre
    
    def __str__(self):
        return "{} {} {}".format(self._Inodos,self._Nombre,self._Libre)
    
