# Frecuencia de palabras
# Mostrar por pantalla la frecuencia de aparición de las palabras del archivo
# Las palabras siempre está separadas por espacios
# Pasos:
# 1 - Eliminar los signos de puntuación
# 2 - Interpretar cada palabra separada por espacios

import string

# Leer archivo
file = open("archivo.txt", "rU")
lines = file.readlines()
file.close()

s = str(lines)
s = s.replace("\\n", "")
s = s.replace(".", "")
s = s.replace(",", "")
s = s.replace(":", "")
s = s.replace("[", "")
s = s.replace("]", "")
s = s.replace("'", "")

rep = dict()
words = s.split(" ")

for word in words:
    if isinstance(rep.get(word), int):
        rep[word] = rep.get(word) + 1
    else:
        rep[word] = 1

#for k, v in rep.items():
    #print(str.format("{0} : {1}", k , v))

print(sorted(rep.items(), key = lambda x : x[0]))