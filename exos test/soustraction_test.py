import unittest
from main import Soustraction


class TestSoustraction(unittest.TestCase):

    def test_Soustraction_basique(self):
        A = 10
        B = 10
        self.assertEqual(Soustraction(A, B), 0)

    def test_Soustraction_negatif(self):
        A = -10
        B = -10
        self.assertEqual(Soustraction(A, B), 0)  # Correction ici

    def test_Soustraction_0(self):
        A = 10
        B = 0.00
        self.assertEqual(Soustraction(A, B), 10)

    def test_Soustraction_grand(self):
        A = 1000000
        B = 1000000
        self.assertEqual(Soustraction(A, B), 0)

    def test_Soustraction_petit(self):
        A = 1
        B = 1
        self.assertEqual(Soustraction(A, B), 0)

    def test_Soustraction_floats(self):
        self.assertAlmostEqual(Soustraction(0.1, 0.2), -0.1 , places=1)

    def test_Soustraction_grand_negatif(self):
        valeur_a = -1000000
        valeur_b = -1000000
        self.assertEqual(Soustraction(valeur_a, valeur_b), 0)

    def test_Soustraction_erreur_type(self):
        with self.assertRaises(TypeError):
            Soustraction("a", 5)  # Cas d'erreur attendu
