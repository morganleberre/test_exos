import unittest
from math import sqrt


def factorielle(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def Manipulationchaines(n):
    return n[::-1]  # Inversion de la chaîne


def Addition(a, b):
    return a + b


def RacineCarrée(nombre):
    return sqrt(nombre)


def calcul_taxes(prix, taux_taxe):
    return prix + (prix * taux_taxe)


def Division(a, b):
    return a / b


def Mutiplication(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les deux paramètres doivent être des nombres")
    return a * b


def Soustraction(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les deux paramètres doivent être des nombres")
    return a - b


if __name__ == '__main__':
    unittest.main()
