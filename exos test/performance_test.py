import time
import random

import pytest

from main import *


def test_performance_multiplication_grands_nombres():
    start_time = time.time()
    result = Mutiplication(10 ** 8, 10 ** 8)
    assert result == 10 ** 16
    end_time = time.time()
    assert end_time - start_time < 0.5  # Vérifie que le calcul prend moins de 0.5s


def test_robustesse_valeurs_aleatoires():
    for _ in range(1000):
        a = random.uniform(-1e10, 1e10)
        b = random.uniform(-1e10, 1e10)
        # Tester des combinaisons aléatoires de addition et multiplication
        assert Addition(a, b) == a + b
        assert Mutiplication(a, b) == a * b
        if b != 0:
            assert Division(a, b) == a / b
        else:
            with pytest.raises(ZeroDivisionError):
                Division(a, b)

        assert Soustraction(a, b) == a - b
