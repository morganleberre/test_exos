import sys
import os

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import *
import pytest


def test_addition_racinecarré():
    A = 10
    B = 10

    resultat = Addition(A, B)
    assert resultat == 20

    assert RacineCarrée(resultat) == pytest.approx(4.47, abs=1e-2)


def test_multiplication_division():
    A = 10
    B = 10

    resultat = Mutiplication(A, B)
    assert resultat == 100

    assert Division(resultat, 10) == 10


def test_addition_mutiplication():
    A = 10
    B = 20
    resultat = Addition(A, B)
    assert resultat == 30

    C = 5
    ResultatMutiplication = Mutiplication(resultat, C)
    assert ResultatMutiplication == 150


def test_soustraction_racinecarree_exception():
    A = 10
    B = 20
    resultat = Soustraction(A, B)  # Devrait donner -10
    with pytest.raises(ValueError):
        RacineCarrée(resultat)
