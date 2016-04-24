# Creación de listas
l = []
l2 = list()

l = [1, 2, 3]

# Concatenar elementos
l.append(4)

# Tamaño
print(len(l))

# Último elemento
l[len(l) - 1]
l[-1]

# Slice
print(l[1:3])  # 2,3
print(l[::-1])  # Lista invertida

# Recorrer listas
for x in l:
    print(x)

for x in range(len(l)):
    print(l[x])

print(list(range(6)))
print(list(range(2, 6, 2)))

for i, x in enumerate(l):
    print(str.format("{0} : {1}", i, x))

l3 = []
for i in range(10):
    l3.append(chr(ord('a') + i))

print(l3)

l4 = []
for i in range(10):
    l += [chr(ord('a') + i)]

print(l)

# Menú
def menu():
    opc = -1

    while (opc not in range(3)):
        print("0. Salir")
        print("1. Listar")
        print("2. Añadir")

        opc = int(input("Dame opc: "))

    return opc

# print(menu())

# Duplicar lista
print([1, 2, 3] * 2)

# Eliminar un elemento de una lista
l5 = [1, 2, 3]
del l5[1]
print(l5)

################## Ejercicios
# primos(n) : Devuelve los n primeros números primos en una lista
def isPrime(n):
    if n == 1:
        return False
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i = i + 1

    return True

def prime(n):
    l = list()

    i = 2
    while len(l) < n:
        if isPrime(i):
            l.append(i)
        i += 1

    print("Números primos: " + str(l))

prime(4)

# Programación dinámica
lista_primos = [2, 3, 5, 7]
def primos(n):
    i = lista_primos[-1] + 1

    while len(lista_primos) < n:
        if(isPrime(i)):
            lista_primos.append(i)
        i += 1

    return lista_primos[0 : n]

print(primos(6))