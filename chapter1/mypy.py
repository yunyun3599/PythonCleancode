def check_mypy(int_var: int):
    print(int_var)


float_var = 0.1
check_mypy(int_var=float_var)  # type: ignore
