class Bakery:
    def __init__(self, menu: list):
        self.menu = menu

    def bake(self, bread, price):
        self.__dict__[bread] = price
        print(f"{bread} is baked!!\n")

    def __getattr__(self, order):
        if order in self.menu:
            print(f"{order} is not baked yet")
            return 0
        else:
            raise AttributeError(f"We don't sell {order}.")


if __name__ == "__main__":
    menu_dict = {"croissant": 1.1, "bagel": 1.2, "baguette": 1.5, "brioche": 1.3, "muffin": 1.4}
    budget = 10

    bakery = Bakery(menu_dict.keys())

    print("##Order Croissant##")
    budget -= bakery.croissant
    print(f"left budget: {budget}\n")

    print("##Bake Croissant##")
    bakery.bake("croissant", menu_dict["croissant"])

    print("##Order Croissant##")
    budget -= bakery.croissant
    print(f"left budget: {budget}\n")

    print("##Order Scon##")
    budget -= bakery.scon
