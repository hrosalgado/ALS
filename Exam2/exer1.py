__author__ = 'Julián'

import os

class Piece:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return "id: {0}, name: {1}".format(self.__id, self.__name)

    @id.setter
    def id(self, value):
        self.__name = value

    @id.setter
    def name(self, value):
        self.__name = value


dictPieces = {}
piece1 = Piece("1", "piece1")
piece2 = Piece("2", "piece2")
dictPieces[1] = piece1
dictPieces[3] = piece2

print(piece1)
print(piece2)

def load(file):
    f = open(file, "rU")
    pieces = f.readlines()
    for k in pieces:
        print(k)

def save(file, data):
    f = open(file, "wt")
    f.write(data)
    f.close()

save("data.dat", dictPieces.__str__())
load("data.dat")