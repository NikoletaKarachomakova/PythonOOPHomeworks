from WildCatZoo.lion import Lion
from WildCatZoo.tiger import Tiger
from WildCatZoo.cheetah import Cheetah
from WildCatZoo.keeper import Keeper
from WildCatZoo.caretaker import Caretaker
from WildCatZoo.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animlal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__animal_capacity -= 1
            self.__budget -= price
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            type_of_worker = type(worker).__name__
            return f"{worker.name} the {type_of_worker} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        old_count = len(self.workers)
        self.workers = [w for w in self.workers if w.name != worker_name]
        new_count = len(self.workers)
        if old_count > new_count:
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needs = sum([a.needs for a in self.animals])
        if self.__budget >= total_needs:
            self.__budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        NEW_LINE = '\n'

        return f"""You have {total_animals_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(str(l) for l in lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(str(t) for t in tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(str(c) for c in cheetahs)}"""

    def workers_status(self):
        total_workers = len(self.workers)
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        NEW_LINE = '\n'

        return f"""You have {total_workers} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(str(l) for l in keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(str(t) for t in caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(str(c) for c in vets)}"""

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
