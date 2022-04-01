def compose(func1, func2):
    def inner(arg):
        return func1(func2(arg))
    return inner


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


print(compose(mul3, add5)(1))
print(compose(add5, mul3)(1))
print(compose(mul3, str)(1))
print(compose(str, mul3)(1))


# def compose(f, g):
#     return lambda x: f(g(x))

