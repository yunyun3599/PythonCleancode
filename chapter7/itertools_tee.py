import itertools

UPPER_LIMIT = 10 ** 10


class SalaryCalculatorWithFilter:
    def __init__(self, salary_list):
        self.salary_list = salary_list
        self.max_salary = 0
        self.round_max_salary = 0

    def calculate(self):
        _max, _round_max = itertools.tee(self.salary_list, 2)
        self.max_salary = max(_max)
        self.round_max_salary = max(round(salary, -2) for salary in _round_max)
        return self


def load_generator_data(path):
    with open(path) as f:
        for line in f:
            *_, salary = line.partition(",")
            yield int(salary)


if __name__ == "__main__":
    data_path = "./salary_data.csv"
    data_generator = load_generator_data(path=data_path)
    calculator = SalaryCalculatorWithFilter(data_generator).calculate()
    print("filter_calculator.max_salary", calculator.max_salary)
    print("filter_calculator.round_max_salary", calculator.round_max_salary)
