from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.SUMMER_ADD_CONSUMPTION)

        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    @abstractmethod
    def SUMMER_ADD_CONSUMPTION(self):
        pass

# There is another solution to this task w/o property. We can just write pass in the abstractmethods drive and refuel_>
# And we can implement the logic of the methods in the child classes using hardociding of the var(summer_consumption and fuel leakage)

class Car(Vehicle):
    SUMMER_ADD_CONSUMPTION = 0.9

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):
    SUMMER_ADD_CONSUMPTION = 1.6

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 2)
    #This is the arrange part. We are creating an instance of the class like property.
    #Everytime we run a test, it will guarantee us that we will use the original data of the obj.
    # It will not save the data from the previous test.

    def test_car_drive_with_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 71)

    def test_car_drive_with_not_enough_fuel(self):
        self.car.drive(60)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_car_refuel(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_quantity, 110)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 5)

    def test_truck_drive_with_enough_fuel(self):
        self.truck.drive(10)
        self.assertEqual(self.truck.fuel_quantity, 34)

    def test_truck_drive_with_not_enough_fuel(self):
        self.truck.drive(60)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_truck_refuel(self):
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 109.5)


if __name__ == "__main__":
    unittest.main()
