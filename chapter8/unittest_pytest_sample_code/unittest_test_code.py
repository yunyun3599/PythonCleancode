import sys
import os
import unittest
sys.path.append(os.getcwd())
from item_cart import Cart, Item
from exceptions import ItemAlreadyInCartException, NoItemInCartException


class TestCartItem(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = [
            ([Item('A', 10000), Item('B', 20000)], 30000),
            ([], 0)
        ]

    def test_add_item(self):
        cart = Cart()
        cart.add_item(Item("keyboard", 30000))
        self.assertEqual(cart.item_list[0], Item("keyboard", 30000))

    def test_add_already_exist_item(self):
        cart = Cart()
        item = Item("keyboard", 30000)
        cart.add_item(item)
        self.assertRaises(ItemAlreadyInCartException, cart.add_item, item)

    def test_delete_item(self):
        cart = Cart()
        item = Item("keyboard", 30000)
        cart.add_item(item)
        cart.delete_item(item)
        self.assertEqual(cart.item_list, [])

    def test_delete_not_exist_item(self):
        cart = Cart()
        item = Item("keyboard", 30000)
        self.assertRaisesRegex(NoItemInCartException, f"{item.name} is not in the cart", cart.delete_item, item)

    def test_price(self):
        cart = Cart()
        for item_list, result in self.test_data:
            with self.subTest(item_list=item_list):
                cart.item_list = item_list
                price = cart.price
                self.assertEqual(price, result)

    def test_price_with_error(self):
        # 문제 되는 데이터에 대한 오류 메세지 출력됨
        try:
            cart = Cart()
            error_included_data = self.test_data + [([Item('A', 10000), Item('B', 20000)], 10000)]
            for item_list, result in error_included_data:
                with self.subTest(item_list=item_list):
                    cart.item_list = item_list
                    price = cart.price
                    self.assertEqual(price, result)
        except AssertionError:
            print(sys.exc_info())
            pass
