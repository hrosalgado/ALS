__author__ = 'Julián'

from Piece import Piece

def obj2str(obj):
    print("{0}:".format(obj.__class__.__name__))
    for i in dir(obj):
        m = getattr(obj, i)
        if callable(m):
            print("\t{0}()".format(m.__name__))
        elif obj.__getattribute__(i):
            print("\t{0} = {1}".format(i, m))

l = Piece(1, "p1")
obj2str(l)