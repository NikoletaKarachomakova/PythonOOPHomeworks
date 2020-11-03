class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.price -= ingredient_price * quantity
        self.ingredients[ingredient] -= quantity

    def pizza_ordered(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        self.ordered = True
        list_ingr = [f'{k}: {v}' for k, v in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(list_ingr)} and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))
