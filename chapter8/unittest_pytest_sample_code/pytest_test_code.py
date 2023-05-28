import sys
import os
import pytest
sys.path.append(os.getcwd())
from item_cart import Cart, Item
from exceptions import ItemAlreadyInCartException, NoItemInCartException


def test_add_item():
    cart = Cart()
    cart.add_item(Item("keyboard", 30000))
    assert cart.item_list[0] == Item("keyboard", 30000)


def test_add_already_exist_item():
    cart = Cart()
    item = Item("keyboard", 30000)
    cart.add_item(item)
    pytest.raises(ItemAlreadyInCartException, cart.add_item, item)


def test_delete_item():
    cart = Cart()
    item = Item("keyboard", 30000)
    cart.add_item(item)
    cart.delete_item(item)
    assert cart.item_list == []


def test_delete_not_exist_item():
    cart = Cart()
    item = Item("keyboard", 30000)
    pytest.raises(NoItemInCartException, cart.delete_item, item)
    with pytest.raises(NoItemInCartException, match=f"{item.name} is not in the cart"):
        cart.delete_item(item)


@pytest.mark.parametrize("item_list, total_price", [([Item('A', 10000), Item('B', 20000)], 30000), ([], 0)])
def test_price(item_list, total_price):
    cart = Cart()
    cart.item_list = item_list
    price = cart.price
    assert price == total_price


# 픽스처를 정의하고 해당 픽스처를 사용할 함수에서 픽스처 이름으로 파라미터 호출해 사용
@pytest.fixture
def price_test_case():
    item_list = [Item('A', 10000), Item('B', 20000)]
    result_price = 30000
    return {"item_list": item_list, "result_price": result_price}


# pricE_test_case라는 픽스처를 호출해서 테스트 데이터로 이용
def test_price_with_fixture(price_test_case):
    cart = Cart()
    new_item = Item('A', 10000)
    cart.item_list = price_test_case["item_list"] + [new_item]
    assert cart.price == price_test_case["result_price"] + new_item.price


def test_price_after_order(price_test_case):
    cart = Cart()
    cart.item_list = price_test_case["item_list"]
    cart.order()
    assert cart.price == 0
