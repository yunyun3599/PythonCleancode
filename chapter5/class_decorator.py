from dataclasses import dataclass


class PriceDiscounter:
    def __init__(self, discount_rates: dict):
        self.discount_rates = discount_rates

    def discount(self, discount_items):
        return {
            item: getattr(discount_items, item) * (1 - discount_rate)
            for item, discount_rate in self.discount_rates.items()
        }


class Discount:
    def __init__(self, **discount_rates):
        self.discounter = PriceDiscounter(discount_rates)

    def __call__(self, discount_items):
        discount_items.discount = self.discounter.discount
        return discount_items


@Discount(
    shirt=0.1,  # 10% 할인
    pants=0.3,  # 30% 할인
    dress=0.5   # 50% 할인
)
class Clothes:
    def __init__(self):
        self.shirt = 30000
        self.pants = 20000
        self.dress = 50000


@Discount(
    data_shirt=0.1,  # 10% 할인
    data_pants=0.3,  # 30% 할인
    data_dress=0.5   # 50% 할인
)
@dataclass
class DataclassClothes:
    data_shirt = 30000
    data_pants = 20000
    data_dress = 50000


if __name__ == "__main__":
    clothes = Clothes()
    discounted_clothes = clothes.discount(clothes)
    print("discounted clothes: ", discounted_clothes)

    data_clothes = DataclassClothes()
    data_discounted_clothes = data_clothes.discount(data_clothes)
    print("data class | discounted clothes: ", data_discounted_clothes)
