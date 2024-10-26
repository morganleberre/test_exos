import unittest
from main import Mutiplication

class TestMutiplication(unittest.TestCase):

    def test_mutiplication_basique(self):
        A = 10
        B = 10
        self.assertEqual(Mutiplication(A, B), 100)

    def test_mutiplication_negatif(self):
        A = -10
        B = -10
        self.assertEqual(Mutiplication(A, B), 100)  # Correction ici

    def test_mutiplication_0(self):
        A = 10
        B = 0.00
        self.assertEqual(Mutiplication(A, B), 0)

    def test_mutiplication_grand(self):
        A = 1000000
        B = 1000000
        self.assertEqual(Mutiplication(A, B), 1000000000000)

    def test_mutiplication_petit(self):
        A = 1
        B = 1
        self.assertEqual(Mutiplication(A, B), 1)

    def test_mutiplication_floats(self):
        self.assertAlmostEqual(Mutiplication(0.1, 0.2), 0.02, places=1)

    def test_mutiplication_grand_negatif(self):
        valeur_a = -1000000
        valeur_b = -1000000
        self.assertEqual(Mutiplication(valeur_a, valeur_b), 1000000000000)

    def test_mutiplication_erreur_type(self):
        with self.assertRaises(TypeError):
            Mutiplication("a", 5)  # Cas d'erreur attendu
