from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.SUMMER_ADD_CONSUMPTION)

        if self.fuel_quantity > needed_fuel:
            self.fuel_quantity -= needed_fuel
        return

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    @abstractmethod
    def SUMMER_ADD_CONSUMPTION(self):
        pass
    # we are saying that every other class should have this parameter. Property helps us to access it like an attribute.(getter)
    # we can move the whole implementation of drive method into class Vehicle. If we do this, we will not repeat the method.
    # we will not change anything for this method in the other classes.
    # so there is no need method "drive" to be an abstract one. It can be just a method.
    # if we keep it as an abstract, we should initialize it in the other classes. To call it with super() function.


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


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

