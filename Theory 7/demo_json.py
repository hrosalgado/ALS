# Demo json
import json

num_alumnos = {'ALS' : 30, 'DIA' : 15, 'DM' : 90}

str_num_alumnos = json.dumps(num_alumnos)
print(str_num_alumnos)

print(json.loads(str_num_alumnos))

# Guardar json
f = open('datos.txt', 'wt')
json.dump(num_alumnos, f)
f.close()

# Recuperar
f = open('datos.txt', 'rU')
num_alumnos = json.load(f)
f.close()

print(num_alumnos)