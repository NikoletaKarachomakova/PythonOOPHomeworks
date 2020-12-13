class Account:
    def __init__(self, owner: str, amount=0):  # this is how we implement optional arguments(by setting default value)
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        available_money = self.amount + sum(self._transactions)
        return available_money

    @staticmethod
    def validate_transaction(account: "Account", amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"
    # This should be static method. It doesn't need self also we don't. We will call it through the class
    # We will not give as an argument self. We will pass only the two needed arguments

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.balance})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, key):
        return self._transactions[key]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_customer_name = self.owner + "&" + other.owner
        new_cust_start_amount = self.amount + other.amount
        new_customer = Account(owner=new_customer_name, amount=new_cust_start_amount)
        new_customer._transactions = self._transactions + other._transactions
        return new_customer


import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account('bob', 10)

    def test_transaction_should_be_only_int(self):
        with self.assertRaises(ValueError):
            self.acc.add_transaction(1.1)

    def test_transaction_is_added_correctly(self):
        self.acc.add_transaction(20)
        self.acc.add_transaction(-40)
        self.assertEqual(2, len(self.acc._transactions))

    def test_balance_is_changed_correctly(self):
        self.acc.add_transaction(20)
        self.acc.add_transaction(40)
        self.assertEqual(70, self.acc.balance)

    def test_validate_transaction_balance_should_not_be_negative(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.acc, -20)

    def test_validate_transaction_is_returning_new_balance(self):
        new_balance = Account.validate_transaction(self.acc, 20)
        self.assertEqual(new_balance, "New balance: 30")

    def test_is_valid_transaction_a_static_method(self):
        import types
        self.assertTrue(isinstance(self.acc.validate_transaction, types.FunctionType))

    def test_custom_str(self):
        self.assertEqual(str(self.acc), "Account of bob with starting amount: 10")

    def test_custom_repr(self):
        self.assertEqual(repr(self.acc), "Account(bob, 10)")

    def test_custom_len(self):
        self.acc.add_transaction(20)
        self.assertEqual(len(self.acc), 1)

    def test_custom_iter(self):
        self.acc.add_transaction(20)
        self.acc.add_transaction(20)
        for t in self.acc._transactions:
            self.assertEqual(t, 20)

    def test_custom_get_item(self):
        self.acc.add_transaction(20)
        self.acc.add_transaction(50)
        self.assertEqual(self.acc._transactions[1], 50)

    def test_custom_greater(self):
        self.acc2 = Account('john')
        self.acc.add_transaction(50)
        self.acc2.add_transaction(40)
        self.assertTrue(self.acc.balance > self.acc2.balance)
        self.assertGreater(self.acc.balance, self.acc2.balance)

    def test_custom_greater_or_equal(self):
        self.acc2 = Account('john')
        self.acc.add_transaction(50)
        self.acc2.add_transaction(60)
        self.assertTrue(self.acc.balance >= self.acc2.balance)
        self.assertGreaterEqual(self.acc.balance, self.acc2.balance)

    def test_custom_add(self):
        self.acc2 = Account('john')
        self.acc.add_transaction(50)
        self.acc2.add_transaction(70)
        self.acc_3 = self.acc + self.acc2
        self.assertEqual(self.acc_3.owner, "bob&john")
        self.assertEqual(self.acc_3.balance, 130)
        self.assertEqual(str(self.acc_3), "Account of bob&john with starting amount: 10")

    def test_custom_reserved(self):
        self.acc.add_transaction(50)
        self.acc.add_transaction(70)
        self.assertEqual(list(reversed(self.acc._transactions)), [70, 50])


if __name__ == "__main__":
    unittest.main()