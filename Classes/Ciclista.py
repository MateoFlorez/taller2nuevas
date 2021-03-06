class Ciclista:

    def __init__(self):
        self.__nombre = None
        self.__edad = None
        self.__pais = None
        self.__equipo = None
        self.__tiempo = None

    # GETTERS
    @property
    def nombre(self):
        return(self.__nombre)
    
    @property
    def edad(self):
        return(self.__edad)

    @property
    def pais(self):
        return(self.__pais)

    @property
    def equipo(self):
        return(self.__equipo)

    @property
    def tiempo(self):
        return(self.__tiempo)

    # SETTERS
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self,edad):
        if(edad < 0):
            print('La edad no puede ser negativa.')
        else:
            self.__edad = edad

    @pais.setter
    def pais(self,pais):
        self.__pais = pais

    @equipo.setter
    def equipo(self,equipo):
        self.__equipo = equipo

    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo < 0):
            print('El tiempo debe ser en minutos y no puede ser negativo.')
        else:
            self.__tiempo = tiempo