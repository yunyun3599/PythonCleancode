import logging
from chapter3.exception import NotValidSeatException, NotEnoughBalanceException

logger = logging.getLogger()


class Payment:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance


class Ticketing:
    def __init__(self, price):
        self.seat = [[True] * 5 for _ in range(5)]
        self.price = price

    def reserve(self, row: int, col: int, payment: Payment):
        try:
            self.get_seat(row, col)
            self.pay(payment)
            print(f"[{row}행 {col}열] 예매가 완료되었습니다. ")
        except NotValidSeatException:
            print("예매 불가능한 좌석입니다.")
            logger.info("예매 불가능한 좌석입니다.")
            # raise
        except NotEnoughBalanceException:
            print("잔액이 부족합니다.")
            logger.info("잔액이 부족합니다.")
            # raise

    def get_seat(self, row, col):
        if 0 < row < len(self.seat) and 0 < col < len(self.seat[row]) and self.seat[row][col]:
            self.seat[row][col] = False
        else:
            raise NotValidSeatException

    def pay(self, payment):
        if payment.balance < self.price:
            raise NotEnoughBalanceException
        payment.balance -= self.price


if __name__ == "__main__":
    ticketing = Ticketing(10000)
    check_card = Payment(20000)
    ticketing.reserve(6, 1, check_card)
    ticketing.reserve(1, 2, check_card)
    ticketing.reserve(1, 2, check_card)
    ticketing.reserve(1, 2, check_card)
