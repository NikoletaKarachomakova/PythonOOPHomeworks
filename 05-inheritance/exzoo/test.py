from exzoo.animal import Animal
from exzoo.mammal import Mammal
from exzoo.reptile import Reptile
from exzoo.bear import Bear
from exzoo.gorilla import Gorilla
from exzoo.snake import Snake
from exzoo.lizard import Lizard


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
