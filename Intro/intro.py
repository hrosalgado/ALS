# Intro

# Mostrar por pantalla
'''print("hola, mundo!")

# E/S
print("Dame tu nombre: ")
nombre = input()
print("Tu nombre es " + nombre)

print("Dame tu edad: ")
edad = int(input())
print("Tu edad es " + str(edad))

# La identación es muy importante
for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        print("impar")

# range(1, 11) : desde 1 hasta 10
# range(1, 11, 2)

i = 1
while i < 11:
    if i % 2 == 0:
        print(i)
    else:
        print("impar")
    i += 1

# Funciones
def es_par(x):
    return x % 2 == 0

i = 0
while i < 11:
    if not(es_par(i)):
        print("impar")
    else:
        print(i)
    i += 1'''

# Creando funciones dentro de funciones
''' Devuelve si un número x es par o no
    :param x: El número a considerar
    :return: True si es par, False en otro caso
'''

'''def es_par(x):
    def modulo(a, b):
        return a % b

    def calcula_modulo():
        return modulo(x, 2)

    return calcula_modulo() == 0

i = 0
while i < 11:
    if not(es_par(i)):
        print("impar")
    else:
        print(i)
    i += 1

# Información acerca de los métodos soportados
i = 0
print(dir(i))

s = "1, 2, 3"
print(s.split(','))'''

# Fibonacci
def fibonacci(x):
    y = 0
    z = 1

    for i in range(x):
        k = y
        y = z
        z = k + z

    return y

print(fibonacci(4))
print(fibonacci(6))
