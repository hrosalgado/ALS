__author__ = 'Julián'

def ordena(l):
    ordenada = list()
    for i in l:
        if len(ordenada) == 0:
            ordenada.insert(0,i)
        else:
            for x in l:
                if i < x:
                    ordenada.insert(l.index(x),i)
                    break
    return ordenada

print(ordena([1,3,2,5,4]))