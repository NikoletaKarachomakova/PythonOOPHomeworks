from projects.worker import Worker
import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Nikoleta", 100, 20)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "Nikoleta")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 20)

    def test_worker_energy_is_incremented_after_rest_method(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_worker_raised_exception_if_works_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_increased_after_working_method(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_energy_decreased_after_working_method(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(old_energy - 1, self.worker.energy)

    def  test_worker_getinfo_method_returns_correct_info(self):
        expected_output = "Nikoleta has saved 0 money."
        result = self.worker.get_info()
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

