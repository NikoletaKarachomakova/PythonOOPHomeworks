from Gym.customer import Customer
from Gym.trainer import Trainer
from Gym.equipment import Equipment
from Gym.exercise_plan import ExercisePlan
from Gym.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.add(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add(subscription, self.subscriptions)

    def add(self, obj_for_add, in_list):
        if obj_for_add not in in_list:
            in_list.append(obj_for_add)

    def subscription_info(self, subscription_id: int):
        all_info = []

        for sub in self.subscriptions:
            if sub.id == subscription_id:
                all_info.append(str(sub))

            customer_id = sub.customer_id
            customer = self.get_object(customer_id, self.customers)
            all_info.append(str(customer))

            trainer_id = sub.trainer_id
            trainer = self.get_object(trainer_id, self.trainers)
            all_info.append((str(trainer)))

            plan_id = sub.exercise_id
            plan = self.get_object(plan_id, self.plans)

            equipment_id = plan.equipment_id
            equip = self.get_object(equipment_id, self.equipment)
            all_info.append(str(equip))
            all_info.append(str(plan))

        return "\n".join(all_info)

    def get_object(self, id, list):
        for item in list:
            if item.id == id:
                return item
