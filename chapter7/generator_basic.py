UPPER_LIMIT = 10 ** 10


class SalaryCalculator:
    def __init__(self, salary_list):
        self.salary_list = salary_list
        self.min_salary = UPPER_LIMIT
        self.max_salary = 0
        self._total_salary = 0
        self._employee_count = 0

    def calculate(self):
        for salary in self.salary_list:
            self.min_salary = min(self.min_salary, salary)
            self.max_salary = max(self.max_salary, salary)
            self._total_salary += salary
            self._employee_count += 1

    @property
    def avg_salary(self):
        return self._total_salary / self._employee_count


def load_list_data(path):
    salary_list = []
    with open(path) as f:
        for line in f:
            *_, salary = line.partition(",")
            salary_list.append(int(salary))
    return salary_list


def load_generator_data(path):
    with open(path) as f:
        for line in f:
            *_, salary = line.partition(",")
            yield int(salary)


if __name__ == "__main__":
    data_path = "./salary_data.csv"

    data_list = load_list_data(path=data_path)
    data_generator = load_generator_data(path=data_path)

    salary_list_calculator = SalaryCalculator(data_list)
    salary_list_calculator.calculate()
    print("salary_list_calculator.avg_salary", salary_list_calculator.avg_salary)

    salary_generator_calculator = SalaryCalculator(data_generator)
    salary_generator_calculator.calculate()
    print("salary_generator_calculator.avg_salary", salary_generator_calculator.avg_salary)



