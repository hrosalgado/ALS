# Exercise 1
def sort_list(list):
    sort = []

    while len(list) > 0:
        minElement = min(list)
        sort.append(minElement)
        list.remove(minElement)

    return sort

# Exercise 2
def histogram(list):
    for x in list:
        if x > 0 and x < 10:
            print('*')
        elif x >= 10 and x < 100:
            x = str(x)
            num = int(x[0:1])
            show = ''
            for i in range(num + 1):
                show += '*'
            print(show)
        elif x >= 100:
            show = ''
            for i in range(12):
                show += '*'
            print(show)

# Exercise 3
def minus_set(set1, set2):
    result = set()

    for x in list(set1):
        flag = False
        for y in list(set2):
            if(x == y):
                flag = True
                break
        if not flag:
            result.add(x)

    print(result)

# Exercise 4
class Student:
    def __init__(self, dni, name):
        self.__dni = dni
        self.__name = name

    @property
    def dni(self):
        return self.__dni

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return str.format('Dni: {0}, Name: {1}', self.dni, self.name)

class Subject:
    def __init__(self, name):
        self.__name = name
        self.__students = dict()
        self.__marks = list()

    @property
    def name(self):
        return self.__name

    @property
    def students(self):
        return self.__students

    @property
    def marks(self):
        return self.__marks

    def add(self, student):
        self.__students[student.dni] = student.name

    def doMark(self, mark):
        self.__marks.append(mark)

    def __str__(self):
        toRet = 'Asignatura: ' + self.name + '\n'

        for k, v in self.students.items():
            toRet += 'Nombre: ' + v + ', Dni: ' + k + '\n'

        return toRet

class Mark:
    def __init__(self, dni, mark):
        self.__dni = dni
        self.mark = mark

    @property
    def dni(self):
        return self.__dni

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        self.__mark = value

    def __str__(self):
        return str.format('Dni: {0}, Nota: {1}', self.dni, self.mark)

# Exercise 5
# igual que ejercicio 5 examen 2014

# Main
# Exercise 1
print(sort_list([3, 0, 4, 2, 1]))

# Exercise 2
histogram([20, 50, 40])

# Exercise 3
minus_set({1, 2, 3}, {1, 3, 4})

# Exercise 4
student = Student('12346578A', 'Manolo')
subject = Subject('Maths')
subject.add(student)
print(subject)
mark = Mark('12345678A', 10)
subject.doMark(mark)
print(subject.marks[0])

# Exercise 5
# igual que ejercicio 5 examen 2014