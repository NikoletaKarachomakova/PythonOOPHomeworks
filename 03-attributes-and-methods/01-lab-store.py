class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        capacity = size // 2
        return cls(name, type, capacity)

    def add_item(self, item_name: str):
        if sum(self.items.values()) + 1 <= self.capacity:
            if item_name in self.items:
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1
            return f"{item_name} added to the store"
        else:
            return f"Not enough capaity in the store"   # NOTE: typo in capacity, may be a  problem

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items:
            if self.items[item_name] - amount >= 0:
                return f"{amount} {item_name} removed from the store"
            else:
                return f"Cannot remove {amount} {item_name}"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"