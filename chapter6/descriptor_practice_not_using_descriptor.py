class Parcel:
    def __init__(self, item, current_status):
        self.item = item
        self._current_status = current_status
        self._delivery_history = [current_status]

    @property
    def current_status(self):
        return self._current_status

    @current_status.setter
    def current_status(self, new_status):
        if new_status != self._current_status:
            self._current_status = new_status
            self._delivery_history.append(new_status)

    @property
    def delivery_history(self):
        return self._delivery_history


if __name__ == "__main__":
    pants = Parcel("pants", "배송 준비중")
    pants.current_status = "출고 완료"
    pants.current_status = "배송중"
    print(pants.delivery_history)
