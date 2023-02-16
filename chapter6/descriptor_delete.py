class SeatException(Exception):
    pass


class Seat:
    def __init__(self, row, col, name=None):
        self._name = name
        self.row = row
        self.col = col
        self.seat = [[False] * self.col for i in range(self.row)]

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        formatted_seat = ""
        for i in self.seat:
            formatted_seat += f"{str(i)}\n"
        return formatted_seat

    def __set__(self, instance, value: tuple):
        user_id = value[0]
        target_row = value[1]
        target_col = value[2]
        if self.check_empty_seat(target_row, target_col) and self.check_seat_range(target_row, target_col):
            self.seat[target_row][target_col] = user_id

    def __delete__(self, instance):
        user_id = instance.user_id
        row = instance.row
        col = instance.col
        if self.check_seat_range(row, col):
            if self.seat[row][col] is user_id:
                self.seat[row][col] = False
            else:
                raise SeatException("본인이 예매한 좌석이 아닙니다!")

    def check_seat_range(self, target_row, target_col):
        if target_row < 0 or target_col < 0 or target_row >= self.row or target_col >= self.col:
            raise ValueError(f"올바르지 않은 좌석 번호입니다. (가능한 좌석행: 0행-{self.row - 1}, 가능한 좌석열: 0열-{self.col - 1})")
        return True

    def check_empty_seat(self, target_row, target_col):
        if self.seat[target_row][target_col]:
            raise SeatException("이미 선점된 좌석입니다.")
        return True


class Book:
    seat = Seat(5, 5)

    def __init__(self):
        self.user_id = None
        self.row = None
        self.col = None

    def book_seat(self, user_id, row, col):
        self.user_id = user_id
        self.row = row
        self.col = col
        self.seat = (self.user_id, self.row, self.col)

    def cancel_seat(self, user_id, row, col):
        self.user_id = user_id
        self.row = row
        self.col = col
        del self.seat


if __name__ == "__main__":
    book = Book()
    print(book.seat)
    book.book_seat('user_a', 1, 2)
    book.book_seat('user_b', 1, 3)
    print(book.seat)
    book.cancel_seat('user_a', 1, 2)
    print(book.seat)
    book.cancel_seat('user_a', 1, 3)