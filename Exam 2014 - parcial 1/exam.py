# Exercise 1
def is_Palindrome(text):
    aux = ''

    for x in range(len(text) - 1, -1, -1):
        aux += text[x]

    return aux == text

# Exercise 3
def inverse_list(elements):
    reverse = list()

    for x in range(len(elements) - 1, -1, -1):
        reverse.append(elements[x])

    return reverse

# Exercise 4
class Point:
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

    def __str__(self):
        return str.format('( {0} , {1} )', self.x, self.y)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    @p1.setter
    def p1(self, value):
        self.__p1 = value

    @p2.setter
    def p2(self, value):
        self.__p2 = value

    def __str__(self):
        return str.format('Start: {0}\nEnd: {1}', str(self.p1), str(self.p2))

class Polygon:
    def __init__(self, points):
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value

    def __str__(self):

        used = list()
        unused = list()
        first = True

        for item in self.points:
            if first:
                used.append(item)
                first = False
            else:
                unused.append(item)


        while len(used) < len(self.points):
            for item in unused:
                if item.x == used[-1].y and self.has_next(item, unused) and not used.__contains__(item):
                    used.append(item)

        toret = ''
        for i in used:
            toret += str(i)

        return  toret

    def has_next(self, item, list):
        for elem in list:
            if item.y == elem.x and elem != item:
                return True

        return False


# Exercicse 5
class Student:
    def __init__(self, dni, name, mail):
        self.dni = dni
        self.name = name
        self.mail = mail

    @property
    def dni(self):
        return self.__dni

    @property
    def name(self):
        return self.__name

    @property
    def mail(self):
        return self.__mail

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @name.setter
    def name(self, value):
        self.__name = value

    @mail.setter
    def mail(self, value):
        self.__mail = value

    def __str__(self):
        return str.format('Dni: {0}, Name: {1}, Mail: {2}', self.dni, self.name, self.mail)

class NormalStudent(Student):
    def __init__(self, dni, name, mail, province):
        Student.__init__(self, dni, name, mail)
        self.province = province

    @property
    def province(self):
        return self.__province

    @province.setter
    def province(self, value):
        self.__province = value

    def __str__(self):
        return Student.__str__(self) + ', Province: ' + str(self.province)

class ErasmusStudent(Student):
    def __init__(self, dni, name, mail, country):
        Student.__init__(self, dni, name, mail)
        self.country = country

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    def __str__(self):
        return Student.__str__(self) + ', Country: ' + str(self.country)

# Main
# Exercise 1
print('Exercise 1')
print(is_Palindrome('radar'))

# Exercise 3
print('Exercise 3')
print(inverse_list([1, 2, 3]))

# Exercise 4
print('Exercise 4')
p1 = Point(0, 0)
p2 = Point(0, 100)
p3 = Point(100, 100)
p4 = Point(100, 0)
line = Line(p1, p2)
polygon = Polygon([p1, p2, p3, p4])
print(polygon)

# Exercicse 5
print('Exercise 5')
normalStudent = NormalStudent('12345678A', 'Paco', 'a@a.es', 'Ourense')
erasmusStudent = ErasmusStudent('87654321B', 'Ana', 'b@b.es', 'Pontevedra')

print(normalStudent)
print(erasmusStudent)