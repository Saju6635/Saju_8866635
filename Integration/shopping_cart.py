class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] += price
        else:
            self.items[item_name] = price

    def calculate_total_cost(self):
        total_cost = sum(self.items.values())
        return total_cost
