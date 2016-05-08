__author__ = 'Julián'

class Estudiante():
    def __init__(self, dni, nombre):
        self.__dni = dni
        self.__nombre = nombre

    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return "{0} con DNI {1}\n".format(self.nombre, self.dni)

class Asignatura():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = {}
        self.__notas = {}

    @property
    def nombre(self):
        return self.__nombre

    @property
    def estudiantes(self):
        return self.__estudiantes

    @property
    def notas(self):
        return self.__notas

    def __str__(self):
        return "Asignatura: {0}, \n" \
               "Estudiantes: {1}".format(self.nombre, self.estudiantes)

    def matricula(self, Estudiante):
        self.__estudiantes.update({Estudiante.dni:Estudiante.nombre})

    def califica(self, Nota):
        self.__notas.update({Nota.dni:Nota.nota})

    def __str__(self):
        return "Asignatura: {0}" \
               "Estudiantes: {1}\n" \
               "Notas: {2}\n".format(self.nombre, self.estudiantes, self.notas)

class Nota():
    def __init__(self, dni, nota):
        self.__dni = dni
        self.__nota = nota

    @property
    def dni(self):
        return self.__dni

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def setNota(self, value):
        self.__nota = value

    def __str__(self):
        return "DNI: {0}, \n" \
               "Nota: {1}".format(self.dni,self.nota)

e1 = Estudiante(12345678, "Palotes, Perico de los")
e2 = Estudiante(12345679, "Con Tomate, Pan")
print("{0}\n{1}\n".format(e1, e2))
a1 = Asignatura("ALS")
a1.matricula(e1)
a1.matricula(e2)
a1.califica(Nota(e1.dni, 7.5))
a1.califica(Nota(e2.dni, 8))
print(a1)
