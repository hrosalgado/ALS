# 1
print("¡Hola, mundo!.")

# 2
print("Dime tu nombre: ")
name = input()
print("Hola {name}".format(name = name))

# 3
def get_name():
    print("Dime tu nombre: ")
    return input()

def show_name(name):
    print("Hola {name}".format(name = name))

show_name(get_name())

# 4
def get_numbers():
    print("Introduce la coordenada x: ")
    x = input()
    print("Introduce la coordenada y: ")
    y = input()
    return [x, y]

def coordinate():
    numbers = get_numbers()
    # Dos formas
    print("( {x} , {y} )".format(x = numbers[0], y = numbers[1]))
    #print("( " + str(numbers[0]) + " , " + str(numbers[1]) + " )")

coordinate()

# 5
def get_number():
    flag = False
    while(not(flag)):
        print("Introduce un número:")

        try:
            x = float(input())
            flag = True
        except ValueError:
            print("Número erróneo!")

    return x

def get_operator():
    flag = False
    while not(flag):
        print("Introduce la operación a realizar (+, -, *, /, ^): ")
        op = input()
        if op == '+' or op == '-' or op == '*' or op == '/' or op == '^':
            flag = True
        else:
            print("Símbolo erróneo!")

    return op

def calculator(x, y, op):
    if op == '+':
        print("El resultado es: {result}".format(result = x + y))
    elif op == '-':
        print("El resultado es: {result}".format(result = x - y))
    elif op == '*':
        print("El resultado es: {result}".format(result = x * y))
    elif op == '/':
        try:
            print("El resultado es: {result}".format(result = x / y))
        except:
            print("No puedes dividir por cero!")
    else:
        print("El resultado es: {result}".format(result = x ** y))

calculator(get_number(), get_number(), get_operator())