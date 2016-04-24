import math

# Exercise 1
def get_data():
    sequence = []
    print("Write a sequence of numbers (type 0 for exit): ")

    while True:
        number = int(input())
        if number != 0:
            sequence.append(number)
        else:
            break

    return sequence

def get_mean(sequence):
    aux = 0

    for x in sequence:
        aux += x

    return aux / len(sequence)

def get_max(sequence):
    max = sequence[0]

    for i in sequence:
        if(max < i):
            max = i

    return max

def get_min(sequence):
    min = sequence[0]

    for i in sequence:
        if(min > i):
            min = i

    return min

def get_typical_deviation(sequence):
    aux = 0

    for x in sequence:
        aux += math.pow(x, 2)

    mean = get_mean(sequence)
    variance = aux / len(sequence) - math.pow(mean, 2)

    return variance

def calc():
    sequence = get_data()
    print("Mean: {mean}, Max: {max}, Min: {min}, Deviation: {deviation}".format(mean = get_mean(sequence), max = get_max(sequence), min = get_min(sequence), deviation = get_typical_deviation(sequence)))

#calc()

# Exercise 2
def get_expr():
    print("Write a expression: ")
    expr = input().split()

    return expr

def get_result(expr):
    if len(expr) > 1:
        x = int(expr[len(expr) - 2])
        y = int(expr[len(expr) - 1])
        op = expr[len(expr) - 3]

        if op == '+':
            res = x + y
        elif op == '-':
            res = x - y
        elif op == '*':
            res = x * y
        else:
            res = x / y

        #del expr[len(expr) - 3 : len(expr) - 1]
        del expr[len(expr) - 1]
        del expr[len(expr) - 1]
        del expr[len(expr) - 1]

        expr.append(res)

        return get_result(expr)
    else:
        return expr

def calc2():
    print("Result: {res}".format(res = get_result(get_expr())))

calc2()
