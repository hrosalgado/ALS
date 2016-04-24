# CLases y objetos

import math

class Punto:
    # Atributos estáticos
    org_x = 0
    org_y = 0

    # Métodos estáticos
    @staticmethod
    def get_org():
        # return Punto(0, 0)
        return Punto(Punto.org_x, Punto.org_y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    # ==
    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y

    # !=
    def __neg__(self, p2):
        return not(self.__eq__(p2))

    # +
    def __add__(self, other):
        return Punto(self.x + p2.x, self.y + p2.y)

    # -
    def __sub__(self, p2):
        return Punto(self.x - p2.x, self.y - p2.y)

    # *
    def __mul__(self, p2):
        return 'jaja'

    def get_distancia(self, p2):
        coord_x = self.x - p2.x
        coord_y = self.y - p2.y

        return math.sqrt(coord_x ** 2 + coord_y ** 2)

    def __str__(self):
        return str.format('{0} , {1}', self.x, self.y)

p1 = Punto(5, 6)
print(p1)

print(dir(p1))
print(str(p1.x) + ' , ' + str(p1.y))

print(isinstance(p1, Punto))
print(isinstance(p1, str))

p2 = Punto(10, 11)
p3 = Punto(5, 6)
p4 = Punto(10, 11)
print(p2, p3, p4)
print(p2 == p3)
print(p2 == p4)
print(p3 == p4)
print(p2 != p3)
print(p2 + p3)
print(p2 - p3)
print(p2 * p3)
# Llamada la método estático
print(Punto.get_org())

# Para saber los atributos y los métodos de la clase
for m_name in dir(p1):
    m = getattr(p1, m_name)
    if callable(m):
        print('Method: ' + m_name)
    else:
        print('Attribute: ' + m_name + ' = ' + str(m))

print(getattr(Punto, 'get_org')())
print(getattr(Punto, '__str__')(p1))
print(getattr(p1, '__str__')())

p1.z = 7
Punto.__str__ = lambda self: str(self.x) + ' , ' + str(self.y) + ' , ' + str(self.z)
print(p1)

print('Distancia p1 a p2: ' + str(p1.get_distancia(p2)))