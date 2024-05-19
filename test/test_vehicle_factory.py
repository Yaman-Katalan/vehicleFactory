from vehicle_factory.car import Car
from vehicle_factory.motorcycle import Motorcycle
import pytest

@pytest.fixture
def new_car():
    return Car("BMW", "electric", "green")

@pytest.fixture
def new_motorcycle():
    return Motorcycle("Honda", "gas")

def test_car(new_car):
    expected = "BMW"
    actual = new_car._model_name
    assert actual == expected

def test_motorcycle(new_motorcycle):
    expected = "Honda"
    actual = new_motorcycle._model_name
    assert actual == expected
