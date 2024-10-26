import unittest
from  main import  Manipulationchaines



class TestChaine(unittest.TestCase):
    def test_inversion_chaine(self):
        s = "Hello"
        self.assertEqual(Manipulationchaines(s), "olleH")

    def test_inversion_chaines_vide(self):
        s = ""
        self.assertEqual(Manipulationchaines(s), "")

    def test_inversion_chaines_espaces(self):
        s = "Hello World"
        self.assertEqual(Manipulationchaines(s), "dlroW olleH")

    def test_inversion_chaines_specials(self):
        s = "12345!@#$%"
        self.assertEqual(Manipulationchaines(s), "%$#@!54321")
