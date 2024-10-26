import sys
import os

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from main import Division


class TestDivision(unittest.TestCase):

    def test_division_basique(self):
        A = 10
        B = 10
        self.assertEqual(Division(A, B), 1)

    def test_division_negatif(self):
        A = -10
        B = -10
        self.assertEqual(Division(A, B), 1)  # Correction ici

    def test_division_0(self):
        A = 10
        B = 0.00
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(Division(A, B), None)

    def test_division_grand(self):
        A = 1000000
        B = 1000000
        self.assertEqual(Division(A, B), 1)

    def test_division_petit(self):
        A = 1
        B = 1
        self.assertEqual(Division(A, B), 1)

    def test_division_floats(self):
        self.assertAlmostEqual(Division(0.1, 0.2), 0.5, places=1)

    def test_division_grand_negatif(self):
        valeur_a = -1000000
        valeur_b = -1000000
        self.assertEqual(Division(valeur_a, valeur_b), 1)

    def test_division_erreur_type(self):
        with self.assertRaises(TypeError):
            Division(10, "dix")  # Cas d'erreur attendu