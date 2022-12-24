class SampleObject:
    def __init__(self, something):
        self.something = something

    def __getattr__(self, item):
        print(f"{item} is an invalid attribute")


if __name__ == "__main__":
    sample_object = SampleObject("something")
    print(sample_object.something)  # something
    print(sample_object.nothing)    # None

