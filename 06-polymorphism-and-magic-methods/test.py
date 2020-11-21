class Account:
    def __init__(self, owner: str, amount=0):  # this is how we implement optional arguments(by setting default value)
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
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

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.balance})"

    def __len__(self):
        return len(self._transactions)

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
