# Las tuplas sólo permiten lectura, no escritura. Son inmutables
t = tuple()

origen = (0, 0)

print(origen)
print(len(origen), ": ", origen[0], " ", origen[1])

print(origen[0:-1])

l = [1, 2, 3]
print(l)
# Convertir lista a tupla
print(tuple(l))

# Convertir tupla a lista
print(list(origen))

def add_delta(p, d):
    """
    Sumar un delta al par de coordenadas
    :param p: El par de coordenadas como tupla
    :param d: El delta, como entero
    """
    return (p[0] + d, p[1] + d)

o = (0, 0)
print(add_delta(o, 5))