import unittest

from  main import calcul_taxes


class TestTaxes(unittest.TestCase):
    def test_taxes_10(self):
        prix = 150
        taux_taxes = 0.10
        self.assertEqual(calcul_taxes(prix, taux_taxes), 165)  # Correction ici

    def test_taxes_20(self):
        prix = 150
        taux_taxes = 0.20
        self.assertEqual(calcul_taxes(prix, taux_taxes), 180)  # Correction ici

    def test_taxes_5(self):
        prix = 150
        taux_taxes = 0.05  # Correction ici
        self.assertEqual(calcul_taxes(prix, taux_taxes), 157.5)  # Ceci est correct

    def test_taxes_0(self):
        prix = 150
        taux_taxes = 0.00
        self.assertEqual(calcul_taxes(prix, taux_taxes), 150)  # Correction ici
