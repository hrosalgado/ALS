__author__ = 'Julián'

class Aparato():
    def __init__(self, codigo, nombre, modelo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__modelo = modelo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def modelo(self):
        return self.__modelo

    def __str__(self):
        return "Codigo: {0}, Nombre: {1}, Modelo: {2}, ".format(self.codigo, self.nombre, self.modelo)

class AparatoNacional(Aparato):
    def __init__(self, codigo, nombre, modelo, provincia):
        super().__init__(codigo, nombre, modelo)
        self.__prov = provincia

    @property
    def prov(self):
        return self.__prov

    def __str__(self):
        return super().__str__() + "Provincia: {0}".format(self.prov)

class AparatoImportacion(Aparato):
    def __init__(self, codigo, nombre, modelo, pais):
        super().__init__(codigo, nombre, modelo)
        self.__pais = pais

    @property
    def pais(self):
        return self.__pais

    def __str__(self):
        return super().__str__() + "Pais: {0}".format(self.pais)

