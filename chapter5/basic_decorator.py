def origin():
    print("do something original")


def modifier(func):
    print("do something more")
    return func


print("\n===original function output===")
origin()

print("\n===reassigned function output===")
origin = modifier(origin)
origin()


print("\n===origin2 function using modifier output===")


@modifier
def origin2():
    print("2 - do something original")

origin2()
