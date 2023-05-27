from dataclasses import dataclass
from exceptions import NoItemInCartException, ItemAlreadyInCartException


@dataclass
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name


class Cart:
    def __init__(self):
        self.item_list = []

    @property
    def price(self):
        return sum([item.price for item in self.item_list])

    def add_item(self, item):
        if item in self.item_list:
            raise ItemAlreadyInCartException(f"{item.name} is already in the cart")
        self.item_list.append(item)

    def delete_item(self, item):
        if item not in self.item_list:
            raise NoItemInCartException(f"{item.name} is not in the cart")
        self.item_list.remove(item)

    def order(self):
        print(f"Order all items in the cart: {[item.name for item in self.item_list]}")
        self.item_list = []
