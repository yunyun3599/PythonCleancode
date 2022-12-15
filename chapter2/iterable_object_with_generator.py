class InstallmentSaving26WithGenerator:
    def __init__(self, base_price):
        self.base_price = base_price
        self.this_week_price = base_price

    def __iter__(self):
        week_count = 1
        while week_count <= 26:
            yield week_count, week_count * self.base_price
            week_count += 1


if __name__ == "__main__":
    saving = InstallmentSaving26WithGenerator(1000)
    for i in range(1, 4):
        for week, price in saving:
            print(f"Week {week}: save {price} won")
        print(f"{i}. saving is done")


