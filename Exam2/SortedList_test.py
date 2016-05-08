__author__ = 'Julián'

import unittest
import SortedList

class SortedListTest(unittest.TestCase):
    def setUp(self):
        self.lista = SortedList.SortedList()

    def test_insert(self):
        self.lista.insert(2)
        self.assertTrue(self.lista.to_list() == [2], "Incorrect insert")

    def test_delete(self):
        self.lista.insert(2)
        self.lista.delete(2)
        self.assertTrue(self.lista.to_list() == [], "Incorrect delete")

if __name__ == "__main__":
    unittest.main()