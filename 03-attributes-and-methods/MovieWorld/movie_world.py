from MovieWorld.dvd import DVD
from MovieWorld.customer import Customer


class MovieWorld:
    def __init__(self, name:str):
        self.name = name
        self.customers = []   # customers as objects
        self.dvds = []   # dvds as objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = self.get_customer(customer_id)
        current_dvd = self.get_dvd(dvd_id)

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd not in current_customer.rented_dvds and current_dvd.is_rented is True:
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = self.get_customer(customer_id)
        current_dvd = self.get_dvd(dvd_id)

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        else:
            return f"{current_customer.name} does not have that DVD"

    def get_customer(self, customer_id):
        for cust in self.customers:
            if cust.id == customer_id:
                current_customer = cust
                return cust

    def get_dvd(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                current_dvd = dvd
                return dvd

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))
        return "\n".join(customers + dvds)
