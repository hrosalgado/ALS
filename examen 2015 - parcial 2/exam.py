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

	def a(self):
		return 1

	def b(self):
		return 2

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
def invoke(obj, strMth):
	for i in dir(obj):
		m = getattr(obj, i)
		if callable(m) and m.__name__ == strMth:
			return m()

	return None

print(invoke(p1, 'b'))
print(invoke(p1, 'c'))

# Exercise 4
collatz = lambda n : [] if n == 1 else \
	[n / 2] + collatz(n / 2) if n % 2 == 0 else \
	[3 * n + 1] + collatz(3 * n + 1)

print(collatz(6))

# Exercise 5
import json

class PuntosPartido:
	def __init__(self):
		self.dict = dict()
		self.index = 0

	def add_player(self, player):
		self.dict.update({self.index : [player.dorsal, player.nombre, player.faltas, player.puntos]})
		self.index = self.index + 1

	def __str__(self):
		to_ret = ''

		for v in self.dict.values():
			to_ret += str(v) + '\n'

		return to_ret

	def save(self, name):
		file = open(name + '.json', 'wt')
		to_json = json.dumps(self.dict)
		json.dump(to_json, file)
		file.close()

	def load(self, name):
		file = open(name + '.json', 'rU')
		dict = json.load(file)
		file.close()
		print(dict)

class Player:
	def __init__(self, dorsal, nombre, faltas, puntos):
		self.dorsal = dorsal
		self.nombre = nombre
		self.faltas = faltas
		self.puntos = puntos

	def add_puntos(self, puntos):
		self.puntos += puntos

	def add_faltas(self, faltas):
		self.faltas = faltas

	def __str__(self):
		return str.format('Nombre: {0}, Dorsal: {1}, Faltas: {2}, Puntos: {3}', self.nombre, self.dorsal, self.faltas, self.puntos)

player1 = Player('24', 'Kobe Bryant', 0, 0)

player1.add_puntos(50)
player1.add_faltas(3)

player2 = Player('21', 'Tim Duncan', 4, 35)

p = PuntosPartido()

p.add_player(player1)
p.add_player(player2)

p.save('match')
p.load('match')