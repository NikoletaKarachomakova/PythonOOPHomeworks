from projects.cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Bari")

    def test_cat_is_initialized_correcty(self):
        self.assertEqual(self.cat.name, "Bari")

    def test_cat_size_increased_after_eating(self):
        old_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size - 1, old_size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_after_it_is_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(exc.exception.args[0], "Already fed.")

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(exc.exception.args[0], 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()