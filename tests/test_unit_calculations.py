import pytest

from app.crud import perform_calculation


def test_addition():
    assert perform_calculation(2, 3, "+") == 5


def test_subtraction():
    assert perform_calculation(5, 2, "-") == 3


def test_multiplication():
    assert perform_calculation(4, 3, "*") == 12


def test_division():
    assert perform_calculation(10, 2, "/") == 5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        perform_calculation(1, 0, "/")


def test_exponentiation():
    assert perform_calculation(2, 3, "^") == 8


def test_invalid_operation():
    with pytest.raises(ValueError):
        perform_calculation(1, 2, "%")
