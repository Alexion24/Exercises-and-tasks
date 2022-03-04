def fib(number):
    fib1 = 0
    fib2 = 1
    result = [fib1, fib2]
    for i in range(number):
        fib_n = fib2 + fib1
        result.append(fib_n)
        fib2, fib1 = fib_n, fib2
    return result[number]


print(fib(10))


# def fib(index):
#     if index <= 0:
#         return 0
#     elif index == 1:
#         return 1
#     return fib(index - 1) + fib(index - 2)

