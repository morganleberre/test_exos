import unittest
from math import *
from main import RacineCarrée


class TestAddition(unittest.TestCase):

    def test_RacineCarre_basique(self):
        A = 10
        self.assertAlmostEqual(RacineCarrée(A), 3.16, places=1)

    def test_RacineCarre_negatif(self):
        with self.assertRaises(ValueError):
            RacineCarrée(-10)

    def test_RacineCarre_0(self):
        A = 0.00
        self.assertEqual(RacineCarrée(A), 0)

    def test_RacineCarre_grand(self):
        A = 1000000

        self.assertEqual(RacineCarrée(A), 1000)

    def test_RacineCarre_petit(self):
        A = 1
        self.assertEqual(RacineCarrée(A), 1)

    def test_RacineCarre_grand_negatif(self):
        with self.assertRaises(ValueError):
            RacineCarrée(-1000000)

    def test_RacineCarre_erreur_type(self):
        with self.assertRaises(TypeError):
            RacineCarrée("dix")  # Cas d'erreur attendu
