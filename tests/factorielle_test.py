import sys
import os

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from  main import factorielle
import unittest

class TestFactorielle(unittest.TestCase):
    def test_factoriellenegatif(self):
        with self.assertRaises(ValueError):
            factorielle(-1)

    def test_factoriellepositif(self):
        self.assertEqual(factorielle(5), 120)

    def test_factorielle1(self):
        self.assertEqual(factorielle(1), 1)

    def test_factorielle0(self):
        self.assertEqual(factorielle(0), 1)
