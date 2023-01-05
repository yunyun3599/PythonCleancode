class EmployeeInfo():
    """도메인 구현을 상속이 아닌 컴포지션으로 대체한 예"""

    def __init__(self, employee_info):
        self._data = employee_info

    def update_employee_info(self, employ_name, **new_employee_info):
        self._data[employ_name].update(**new_employee_info)

    def __getitem__(self, employ_name):
        return self._data[employ_name]

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    info = EmployeeInfo({
        "Jack": {
            "salary": 50000,
            "department": "marketing"
        },
        "Rose": {
            "salary": 60000,
            "department": "management"
        }
    })
    print(info["Jack"])
    info.update_employee_info("Jack", salary="60000", grade="S")
    print(info["Jack"])
    print(len(info))
    print(dir(info))   # 안쓰는 메서드 너무 많음
