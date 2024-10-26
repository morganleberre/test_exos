import unittest
from main import Addition


class TestAddition(unittest.TestCase):

    def test_addition_basique(self):
        A = 10
        B = 10
        self.assertEqual(Addition(A, B), 20)

    def test_addition_negatif(self):
        A = -10
        B = -10
        self.assertEqual(Addition(A, B), -20)  # Correction ici

    def test_addition_0(self):
        A = 10
        B = 0.00
        self.assertEqual(Addition(A, B), 10)

    def test_addition_grand(self):
        A = 1000000
        B = 1000000
        self.assertEqual(Addition(A, B), 2000000)

    def test_addition_petit(self):
        A = 1
        B = 1
        self.assertEqual(Addition(A, B), 2)

    def test_addition_floats(self):
        self.assertAlmostEqual(Addition(0.1, 0.2), 0.3, places=1)

    def test_addition_grand_negatif(self):
        valeur_a = -1000000
        valeur_b = -1000000
        self.assertEqual(Addition(valeur_a, valeur_b), -2000000)

    def test_addition_erreur_type(self):
        with self.assertRaises(TypeError):
            Addition(10, "dix")  # Cas d'erreur attendu
