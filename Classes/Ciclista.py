class Ciclista:

    def __init__(self):
        self.__nombre = None
        self.__edad = None
        self.__pais = None
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
    def tiempo(self):
        return(self.__tiempo)