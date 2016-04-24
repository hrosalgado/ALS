f = open('file.txt', 'rU')
# Forma 1
#l = f.readlines()
#for x in l:
#    print(x)

# Forma 2
l = list()
for line in f:
    l.append(line)
print(l)

f.close()

# Pickle ----
import pickle

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return str.format('{0} ({1})', self.nombre, self.edad)

def guardar():
    p1 = Persona('Héctor', 20)
    p2 = Persona('David', 20)
    f = open('personas.bin', 'wb')
    #pickle.dump(p1, f)
    pickle.dump([p1, p2], f)
    f.close()

def cargar():
    f = open('personas.bin', 'rb')
    p = pickle.load(f)
    #print(p)
    f.close()
    return p

guardar()
l = cargar()
for x in l:
    print(x)