from project.animals.animal import *
from project.food import *

class Owl(Bird):
    gaining = 0.25

    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):
    gaining = 0.35

    def make_sound(self):
        return "Cluck"
