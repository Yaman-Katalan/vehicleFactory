from factory import Factory
from car import Car
from motorcycle import Motorcycle

obj1 = Car("BMW", "electric", "green")
obj1 = Car("BMW", "electric", "green")
obj2 = Car("Toyota", "electric", "black")
obj2 = Car("Toyota", "electric", "black")

obj3 = Motorcycle("Honda", "gas")
obj4 = Motorcycle("BM", "diesel")
obj4 = Motorcycle("BM", "diesel")

print(Car.get_count())
print(Motorcycle.get_count())
print(Factory.get_count())