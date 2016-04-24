# lambdas

def doble(x):
	'''Calcula el doble del param.
		:param x: El valor a doblar, como entero
		:return: El doble, como entero
	'''
	return x * 2;

doble2 = lambda x: x * 2

print(doble(5))
print(doble2(5))
print('es mayor' if doble(5) > 6 else 'es menor')

factorial = lambda x: 1 if x == 1 \
						else x * factorial(x - 1)

print(factorial(6))


class Punto:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;

Punto.__str__ = lambda self: str.format('{0}, {1}', self.x, self.y)

p1 = Punto(4,2)
print(p1)

fibonacci = lambda n: n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

print('n = 0 -> ' + str(fibonacci(0)))
print('n = 1 -> ' + str(fibonacci(1)))
print('n = 2 -> ' + str(fibonacci(2)))
print('n = 3 -> ' + str(fibonacci(3)))
print('n = 4 -> ' + str(fibonacci(4)))
print('n = 5 -> ' + str(fibonacci(5)))
print('n = 6 -> ' + str(fibonacci(6)))






# ~Lisp
car = lambda l: None if l == None or l == [] else \
				l[0]

cdr = lambda l: [] if l == None or l == [] else \
				l[1 : ]

# Inversa - Devuelve la inversa de una lista
inversa = lambda l: [] if car(l) == None else \
					inversa(cdr(l)) + [car(l)]

print(inversa([1, 2, 3]))




# Map, reduce, filter
# functools

# map -> aplicar una funcion a todos los elementos de una lista
# [1, 2, 3] -> [2, 4, 6]

# filter -> devolver los elementos que cumplen un filtro
# [1, 2, 3] y esPar() -> [2]

# reduce -> devuelve el resultado de aplicar una funcion a los elementos de una lista
# [1, 2, 3] y suma(a, b) -> 6

map = lambda l, f: [] if car(l) == None else \
						[f(car(l))] + map(cdr(l), f)

print(map([1, 2, 3], doble))
print(map([1, 2, 3], doble2))


filter = lambda l, f: [] if car(l) == None else \
						[car(l)] + filter(cdr(l), f) if f(car(l)) else \
						filter(cdr(l), f)

print(filter([1, 2, 3, 4], lambda x: x % 2 == 0))


reduce = lambda l, f: car(l) if car(cdr(l)) == None else \
						f(car(l), reduce(cdr(l), f))

print(reduce([1, 2, 3], lambda x, y: x + y))