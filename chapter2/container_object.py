class OpeningHours:
    def __init__(self, open_at, close_at):
        self.open_at = open_at
        self.close_at = close_at

    def __contains__(self, hour):
        return self.open_at <= hour <= self.close_at


class AmusementPark:
    def __init__(self, open_at, close_at):
        self.open_at = open_at
        self.close_at = close_at
        self.opening_hours = OpeningHours(self.open_at, self.close_at)

    def __contains__(self, hour):
        return hour in self.opening_hours


if __name__ == "__main__":
    amusement_park = AmusementPark(10, 21)
    time_list = [9, 10, 15, 20, 23]
    for time in time_list:
        print(f"The amusement is open at {time}? - {time in amusement_park}:")
