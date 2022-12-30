import logging
from chapter3.exception import NotValidSeatException, NotEnoughBalanceException

logger = logging.getLogger()


class Seat:
    def __init__(self):
        self.seat = [[True] * 5 for _ in range(5)]

    def get_seat(self, row, col):
        if 0 < row < len(self.seat) and 0 < col < len(self.seat[row]) and self.seat[row][col]:
            self.seat[row][col] = False
        else:
            logger.info("예매 불가능한 좌석입니다.")
            raise NotValidSeatException


class Payment:
    def __init__(self, balance):
        self._balance = balance

    def pay(self, price):
        if self._balance >= price:
            self._balance -= price
        else:
            logger.info("잔액이 부족합니다.")
            raise NotEnoughBalanceException


class Ticketing:
    def __init__(self, price):
        self.seat = Seat()
        self.price = price

    def reserve(self, row, col, payment):
        self.seat.get_seat(row, col)
        payment.pay(self.price)


if __name__ == "__main__":
    ticketing = Ticketing(20000)
    check_card = Payment(30000)
    ticketing.reserve(6, 1, check_card)
    ticketing.reserve(1, 2, check_card)
    ticketing.reserve(1, 2, check_card)
    ticketing.reserve(1, 2, check_card)
