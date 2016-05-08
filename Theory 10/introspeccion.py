class A:
	def __init__self():
		self.x = 0

	def foo(self):
		print('foo')

	def fie(self):
		print('fie')

	def __getattr__(self, s):
		return lambda: s

	def __getattribute__(self, s):
		return lambda: True

a = A()

print(dir(A))
print(dir(a))

print(callable(a.fie))
print(callable(a.x))

print(getattr(a, 'x'))
print(getattr(a, 'foo'))

def dump(obj):
	for s in dir(obj):
		m = getattr(obj, s)
		if(callable(m)):
			print(s + '()')
		else:
			print(m)

print(dump(a))
'''a.x = 5
print(dump(a))'''

#print(a.hola())
#print(a.foo)