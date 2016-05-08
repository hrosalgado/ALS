__author__ = 'Julián'

fibo = lambda n : 0 if n <= 1 else \
    1 if n == 2 else \
    fibo(n-1) + fibo(n-2)

fibonacci = lambda n : [] if n <= 0 else \
    [0] if n == 1 else \
    [0,1] if n == 2 else \
    fibonacci(n-1) + [fibo(n)]


print("fibonacci(9) = {0}".format(fibonacci(9)))

tribo = lambda n : 0 if n <= 1 else \
    1 if n == 2 or n == 3 else \
    tribo(n-1) + tribo(n-2) + tribo(n-3)

tribonacci = lambda n : [] if n <= 0 else \
    [0] if n == 1 else \
    [0,1] if n == 2 else \
    [0,1,1] if n == 3 else \
    tribonacci(n-1) + [tribo(n)]

n = 8
print("tribo({0}) = {1}".format(n, tribo(n)))
print("tribonacci({0}) = {1}".format(n, tribonacci(n)))