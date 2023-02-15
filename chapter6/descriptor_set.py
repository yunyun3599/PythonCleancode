class OccupiedSeatException(Exception):
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

    def check_valid_seat(self, target_row, target_col):
        if target_row < 0 or target_col < 0 or target_row >= self.row or target_col >= self.col:
            raise ValueError(f"올바르지 않은 좌석 번호입니다. (가능한 좌석행: 0행-{self.row - 1}, 가능한 좌석열: 0열-{self.col - 1})")
        if self.seat[target_row][target_col]:
            raise OccupiedSeatException("이미 선점된 좌석입니다.")
        return True

    def __set__(self, instance, value: tuple):
        target_row = value[0]
        target_col = value[1]
        if self.check_valid_seat(target_row, target_col):
            self.seat[target_row][target_col] = True


class Book:
    seat = Seat(5, 5)


if __name__ == "__main__":
    book = Book()
    print(book.seat)
    book.seat = (1, 2)
    print(book.seat)
    book.seat = (1, 2)
