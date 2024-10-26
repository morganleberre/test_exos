import unittest


def factorielle(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result




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
