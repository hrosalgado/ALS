__author__ = 'Julián'

def resta_conjuntos(c1, c2):
    toret = set()
    flag = True
    for i in c1:
        if c2.__contains__(i) == False:
            toret.add(i)
    return toret


c1 = set([1,2,3])
c2 = set([3,4])
print(resta_conjuntos(c1,c2))