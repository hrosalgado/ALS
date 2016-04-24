class Punto:
	x = 0
	y = 0

	def __str__(self):
		return str.format('{0} , {1}', self.x, self.y)

p1 = Punto()
print(p1.x)
p1.y = 5

print(str(p1))


class Punto3D:
	x = 0
	y = 0
	z = 0

	def __str__(self):
		return str.format('{0} , {1} , {2}', self.x, self.y, self.z)

p2 = Punto3D()
print(str(p2))

p2.x = 1
print(str(p2))

p2.__class__ = Punto
print(str(p2))

p1.__class__ = Punto3D
print(str(p1))

p2.__class__ = Punto3D
print(str(p2))

p2.z = 9
print(str(p2))

p2.__class__ = Punto
print(str(p2))
print(dir(p2))