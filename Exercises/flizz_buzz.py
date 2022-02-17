def flizz_buzz(begin, end):
    result = ''
    for num in range(begin, end + 1):
        if num % 3 == 0:
            result += 'Flizz '
        elif begin == end:
            return result
        elif num % 5 == 0:
            result += "Buzz "
        elif num % 3 == 0 and num % 5 == 0:
            result += ' FlizzBuzz '
        else:
            result += f"{num} "
    return result


print(flizz_buzz(1, 5))
