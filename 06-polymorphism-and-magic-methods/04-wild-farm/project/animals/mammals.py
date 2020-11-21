from project.animals.animal import *
from project.food import *


class Mouse(Mammal):
    gaining = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    gaining = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    gaining = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    gaining = 1.00

    def make_sound(self):
        return "ROAR!!!"
