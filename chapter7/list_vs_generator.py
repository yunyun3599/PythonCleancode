if __name__ == "__main__":
    lst = [i for i in range(10)]
    generator = (i for i in range(10))

    print("max(lst):", max(lst))
    print("max(generator):", max(generator))
    print("max(lst):", max(lst))
    print("max(generator):", max(generator))
