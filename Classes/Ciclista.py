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
        print('Digita el nombre: ')
        self.__nombre = input(nombre)

    @edad.setter
    def edad(self,edad):
        if(edad < 0):
            print('La edad no puede ser negativa.')
        else:
            print('Digita el edad: ')
            self.__edad = input(edad)

    @pais.setter
    def pais(self,pais):
        print('Digita el pais: ')
        self.__pais = input(pais)

    @equipo.setter
    def equipo(self,equipo):
        print('Digita el equipo: ')
        self.__equipo = input(equipo)

    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo < 0):
            print('El tiempo debe ser en minutos y no puede ser negativo.')
        else:
            print('Digita el tiempo: ')
            self.__tiempo = input(tiempo)