class HistorySaveAttribute:
    def __init__(self, history_list_name):
        self.history_list_name = history_list_name
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not instance.__dict__.get(self._name):       # 속성이 아직 설정 되어 있지 않은 경우
            instance.__dict__[self._name] = value

        if not instance.__dict__.get(self.history_list_name):   # 변경 사항 저장 리스트 초기화가 아직 안된 경우
            instance.__dict__[self.history_list_name] = [instance.__dict__[self._name]]

        if instance.__dict__[self._name] != value:
            instance.__dict__[self._name] = value
            instance.__dict__[self.history_list_name].append(value)


class Parcel:
    delivery_status = HistorySaveAttribute('delivery_history')

    def __init__(self, item, delivery_status):
        self.item = item
        self.delivery_status = delivery_status


if __name__ == "__main__":
    pants = Parcel('pants', '배송 준비중')
    pants.delivery_status = "출고 완료"
    pants.delivery_status = "배송중"
    print("pants.delivery_status:", pants.delivery_status)
    print("pants.delivery_history:", pants.delivery_history)
