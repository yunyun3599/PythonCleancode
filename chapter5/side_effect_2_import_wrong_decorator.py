import time

from side_effect_2_logic_placed_outside import wrong_time_calc


@wrong_time_calc
def sample_func(n):
    for _ in range(n):
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(2)
    print("start operating")
    sample_func(2)
    sample_func(1)
