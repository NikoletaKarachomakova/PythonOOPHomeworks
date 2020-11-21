from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        can_be_feed = True

        if type(self).__name__ == "Mouse" and type(food).__name__ not in ["Vegetable", "Fruit"]:
            can_be_feed = False

        elif type(self).__name__ == "Cat" and type(food).__name__ not in ["Vegetable", "Meat"]:
            can_be_feed = False

        elif type(self).__name__ in ["Tiger", "Dog", "Owl"] and type(food).__name__ != "Meat":
            can_be_feed = False

        if can_be_feed:
            self.weight += (food.quantity * self.gaining)
            self.food_eaten += food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

    @property
    @abstractmethod
    def gaining(self):
        pass


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return "{type} [{name}, {weight}, {living_region}, {food_eaten}]".format(
            type=type(self).__name__,
            name=self.name,
            weight=self.weight,
            living_region=self.living_region,
            food_eaten=self.food_eaten
        )


class Bird(Animal):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return "{type} [{name}, {wing_size}, {weight}, {food_eaten}]".format(
            type=type(self).__name__,
            name=self.name,
            wing_size=self.wing_size,
            weight=self.weight,
            food_eaten=self.food_eaten
        )