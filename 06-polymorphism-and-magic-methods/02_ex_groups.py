from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Can't sum different types")
        return Person(name=self.name, surname=other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __add__(self, other):
        persons_in_new_group = self.people + other.people
        return Group(name="???", people=persons_in_new_group)

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, key: int):
        return f"Person {key}: {str(self.people[key])}"


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Nikoleta", "Ivanova")

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertEqual(result, "Nikoleta Ivanova")

    def test_custom_add_person_with_not_valid_type_for_person(self):
        self.person_2 = Person("Spas", "Minkov")
        self.person_3 = self.person_1 + self.person_2
        self.assertEqual(str(self.person_3), "Nikoleta Minkov")


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Nikoleta", "Ivanova")
        self.person_2 = Person("Spas", "Minkov")
        self.group_1 = Group("First group", [self.person_1, self.person_2])

    def test_custom_add(self):
        self.person_3 = Person("Bari", "Minkov")
        self.group_2 = Group("Second group", [self.person_3])
        self.group_3 = self.group_1 + self.group_2
        self.assertEqual(self.group_3.people, [self.person_1, self.person_2, self.person_3])

    def test_custom_len(self):
        self.assertEqual(len(self.group_1), 2)

    def test_custom_repr(self):
        self.assertEqual(str(self.group_1), "Group First group with members Nikoleta Ivanova, Spas Minkov")

    def test_custom_get_item(self):
        result = "Person 0: Nikoleta Ivanova"
        self.assertEqual(str(self.group_1[0]), result)

if __name__ == "__main__":
    unittest.main()