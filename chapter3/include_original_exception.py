from exception import NotValidSeatException


class Seat:
    def __init__(self):
        self.seat = [[True] * 5 for _ in range(5)]

    def get_seat(self, row, col):
        try:
            if not self.seat[row][col]:
                raise AlreadyOccupiedSeatException("이미 선택된 좌석입니다.")
            self.seat[row][col] = False
            print(f"{row}행 {col}열 좌석 선택 완료")
        except IndexError as e:
            raise WrongSeatNumberException("좌석 번호 오류") from e


class AlreadyOccupiedSeatException(NotValidSeatException):
    pass


class WrongSeatNumberException(NotValidSeatException):
    pass


if __name__ == "__main__":
    seat = Seat()
    seat.get_seat(1, 1)
    # seat.get_seat(1, 1)
    seat.get_seat(6, 6)
