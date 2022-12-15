class InstallmentSaving26:
    def __init__(self, base_price):
        self.base_price = base_price
        self.this_week_price = base_price
        self.week_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.week_count >= 26:
            raise InstallmentSavingMaturityException
        self.week_count += 1
        self.this_week_price = self.base_price * self.week_count
        return self.week_count, self.this_week_price


class InstallmentSavingMaturityException(Exception):
    pass


if __name__ == "__main__":
    saving = InstallmentSaving26(1000)
    for i in range(1, 4):
        try:
            for week, price in saving:
                print(f"Week {week}: save {price} won")
        except InstallmentSavingMaturityException:
            print(f"{i}. saving is done")

