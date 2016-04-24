# Conjuntos
# Crear un conjunto
conjunto = set()

# Añadir elementos a un conjunto
conjunto.add(1)
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)

# Mostrar un conjunto
print(conjunto)

# Comprobar si un elemento está en un conjunto
print(5 in conjunto)
print(2 in conjunto)
print(3 not in conjunto)

# Recorrer un conjunto
for elemento in conjunto:
    print(elemento)

# Longitud conjunto
print(len(conjunto))

# Pasar un conjunto a una lista
l = list(conjunto)
for i in range(len(conjunto)):
    print(l[i])