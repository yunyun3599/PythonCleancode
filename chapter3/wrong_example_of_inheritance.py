import collections


class EmployeeInfo(collections.UserDict):
    """데이터 구조를 도메인 객체로 만든 잘못된 상속의 예"""

    def update_employee_info(self, employ_name, **new_employee_info):
        self[employ_name].update(new_employee_info)


if __name__ == "__main__":
    employee_info = EmployeeInfo({
        "Jack": {
            "salary": 50000,
            "department": "marketing"
        }
    })
    print(employee_info)
    employee_info.update_employee_info("Jack", grade="S")
    print(employee_info)
    print(dir(employee_info))   # 안쓰는 메서드 너무 많음
