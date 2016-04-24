# Diccionarios
# Crear
temperaturas = {"Ourense" : 5, "Vigo" : 12}
d = dict()

# Mostrar
print(temperaturas)
print(temperaturas["Vigo"])
print(temperaturas.get("León")) # Mejor opción para evitar excepciones en casa de que la clave no exista

# Recorrer
for k in temperaturas.keys():
    print(str.format("{0} : {1}º", k , temperaturas[k]))

for k, v in temperaturas.items():
    print(str.format("{0} : {1}º", k , v))

for v in temperaturas.values():
    print(str.format("{0}º", v))