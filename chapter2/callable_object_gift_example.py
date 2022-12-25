class Gift:
    def __init__(self):
        self.version_a = 0
        self.version_b = 0
        self.version_c = 0

    def __call__(self, *orders):
        for order in orders:
            if order == "version_a":
                self.version_a += 1
            elif order == "version_b":
                self.version_b += 1
            elif order == "version_c":
                self.version_c += 1
            else:
                print(f"{order} is not available")

        print(f"<Order Status>\n "
              f"- version_a: {self.version_a}\n "
              f"- version_b: {self.version_b}\n "
              f"- version_c: {self.version_c}\n")


if __name__ == "__main__":
    gift = Gift()
    gift("version_a")
    gift("version_b", "version_b", "version_c")
    lst = ["version_c", "version_c", "version_c"]
    gift(*lst)
    gift("version_d")
