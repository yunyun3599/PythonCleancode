from itertools import islice

UPPER_LIMIT = 10 ** 10


class SalaryCalculatorWithCondition:
    def __init__(self, salary_list):
        self.salary_list = salary_list
        self.min_salary = UPPER_LIMIT
        self.max_salary = 0
        self._total_salary = 0
        self._employee_count = 0

    def calculate(self):
        for salary in self.salary_list:
            if 2000 <= salary <= 1000000 and self._employee_count <= 100:  # 조건문 추가
                self.min_salary = min(self.min_salary, salary)
                self.max_salary = max(self.max_salary, salary)
                self._total_salary += salary
                self._employee_count += 1

    @property
    def avg_salary(self):
        return self._total_salary / self._employee_count


class SalaryCalculatorWithFilter:
    def __init__(self, salary_list):
        self.salary_list = salary_list
        self.min_salary = UPPER_LIMIT
        self.max_salary = 0
        self._total_salary = 0
        self._employee_count = 0

    def calculate(self):
        for salary in self.salary_list:    # salary 구간이 2000 ~ 100000인 선착 100명에 대해 계산
            self.min_salary = min(self.min_salary, salary)
            self.max_salary = max(self.max_salary, salary)
            self._total_salary += salary
            self._employee_count += 1

    @property
    def avg_salary(self):
        return self._total_salary / self._employee_count


def load_generator_data(path):
    with open(path) as f:
        for line in f:
            *_, salary = line.partition(",")
            yield int(salary)


if __name__ == "__main__":
    data_path = "./salary_data.csv"
    data_generator = load_generator_data(path=data_path)
    condition_calculator = SalaryCalculatorWithCondition(data_generator)
    condition_calculator.calculate()
    print("condition_calculator.avg_salary", condition_calculator.avg_salary)

    data_generator = load_generator_data(path=data_path)
    salary_filtered_generator = islice(filter(lambda salary: 2000 <= salary <= 1000000, data_generator), 101)
    filter_calculator = SalaryCalculatorWithFilter(salary_filtered_generator)
    filter_calculator.calculate()
    print("filter_calculator.avg_salary", filter_calculator.avg_salary)
