class InstallmentSaving26Sequence:
    def __init__(self, base_price):
        self.base_price = base_price
        self._price_list = [base_price * week for week in range(1, 27)]

    def __getitem__(self, week):
        return self._price_list[week]

    def __len__(self):
        return len(self._price_list)


if __name__ == "__main__":
    saving = InstallmentSaving26Sequence(1000)
    week10 = 10
    print(f"Saved price on Week {week10} is {saving[week10 - 1]}")
