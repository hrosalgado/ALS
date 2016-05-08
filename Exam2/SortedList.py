__author__ = 'Julián'

class SortedList:
    def __init__(self):
        self.list = []

    def insert(self, elem):
        self.list.append(elem)

    def to_list(self):
        return self.list

    def delete(self, elem):
        self.list.remove(elem)
