from persona import Persona
import unittest

class TestPersona(unittest.TestCase):
    # Se ejecuta sólo una vez al principio
    def setUpClass():
        print('Comenzando del todo...')

    # Se ejecuta antes de cada test
    def setUp(self):
        print('Comenzando...')

    # Test 1
    def test_persona_str(self):
        print('Testing...')

    # Test 2
    def test_persona_other(self):
        print('Testing 2...')

    # Se ejecuta después de cada test
    def tearDown(self):
        print('Finalizando...')

    # Se ejecuta sólo una vez al final
    def tearDownClass():
        print('Finalizando del todo...')

    # Test Persona
    def test_persona_str(self):
        self.assertEqual('Baltasar (18).', str(Persona('Baltasar', 18)))

    def test_persona_constructor(self):
        p = Persona('Baltasar', 18)
        self.assertEqual(18, p.edad)
        self.assertTrue(18 == p.edad)

unittest.main()