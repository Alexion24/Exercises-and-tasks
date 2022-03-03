import math


def is_power_of_three(number):
    if number == 0:
        return False
    else:
        result = math.log(number, 3)
        return result == int(result)


print(is_power_of_three(0))