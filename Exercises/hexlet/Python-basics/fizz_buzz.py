def fizz_buzz(begin, end):
    result = ''
    for num in range(begin, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            result += 'FizzBuzz '
        elif num % 3 == 0:
            result += 'Fizz '
        elif num % 5 == 0:
            result += "Buzz "
        else:
            result += f"{num} "
    return result.strip()


print(fizz_buzz(11, 20))
