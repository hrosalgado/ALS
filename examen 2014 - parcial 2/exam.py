# Exercise 1
import pickle

class Pieza:
	def __init__(self, id, nombre):
		self.__id = id
		self.__nombre = nombre

	@property
	def id(self):
		return self.__id
	
	@id.setter
	def id(self, id):
		self.__id = id

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nombre):
		self.__nombre = nombre

	def __str__(self):
		return str.format('{0} , {1}', self.id, self.nombre)

def load():
	f = open('piezas.dat', 'rb')
	p = pickle.load(f)
	f.close()
	return p

def save(dictPiezasa):
	f = open('piezas.dat', 'wb')
	pickle.dump(dictPiezas, f)
	f.close()

dictPiezas = dict()

p1 = Pieza(1, 'a')
p2 = Pieza(2, 'b')
p3 = Pieza(3, 'c')

dictPiezas.update({p1.id : p1})
dictPiezas.update({p2.id : p2})
dictPiezas.update({p3.id : p3})

save(dictPiezas)

piezas = load()
for v in piezas.values():
	print(v)

# Exercise 2
class ListaOrdenada:
	def __init__(self):
		self.__lista = list()

	@property
	def lista(self):
		return self.__lista

	@lista.setter
	def lista(self, lista):
		self.lista = lista

	def inserta(self, elem):
		self.lista.append(elem)
		self.lista.sort()

	def to_list(self):
		return self.lista

	def borra_en(self, elem):
		self.lista.remove(elem)

import unittest

class TestListaOrdenada(unittest.TestCase):
	def setUpClass():
		print('Empieza el test...')
		
	# Test insertar
	def test_insertar(self):
		lista = ListaOrdenada()

		self.assertTrue(len(lista.to_list()) == 0)

		lista.inserta(1)

		self.assertTrue(len(lista.to_list()) == 1)
		self.assertTrue(lista.to_list()[0] == 1)

		lista.inserta(3)
		lista.inserta(2)

		self.assertTrue(lista.to_list()[1] == 2)

	# Test eliminar
	def test_eliminar(self):
		lista = ListaOrdenada()

		lista.inserta(1)
		lista.inserta(2)
		lista.inserta(3)

		lista.borra_en(1)
		self.assertTrue(len(lista.to_list()) == 2)

		self.assertTrue(lista.to_list()[0] == 2)
		self.assertTrue(lista.to_list()[1] == 3)

	def tearDownClass():
		print('Finaliza el test...')

#unittest.main()

# Exercise 3
def obj2str(obj):
	print(str.format('{0}:', obj.__class__.__name__))
	for i in dir(obj):
		m = getattr(obj, i)
		if(callable(m)):
			print(str.format('\t{0}()', m.__name__))
		elif obj.__getattribute__(i):
			print(str.format('\t{0} = {1}', i, m))

p = Pieza(1, 'a')
obj2str(p)

# Exercise 4
tribo = lambda n : 0 if n <= 1 else \
    1 if n == 2 or n == 3 else \
    tribo(n-1) + tribo(n-2) + tribo(n-3)
    
tribonacci = lambda n : [] if n <= 0 else \
    [0] if n == 1 else \
    [0,1] if n == 2 else \
    [0,1,1] if n == 3 else \
    tribonacci(n-1) + [tribo(n)]

n = 8
print("tribonacci({0}) = {1}".format(n, tribonacci(n)))

# Exercise 5
import json

temperaturas = {'Madrid' : 25, 'Ourense' : 35, 'Vigo' : 22}

to_json = json.dumps(temperaturas)

# To save
file = open('temperaturas.json', 'wt')
json.dump(to_json, file)
file.close()

# To load
file = open('temperaturas.json', 'rU')
temperaturas2 = json.load(file)
file.close()

print(temperaturas2)