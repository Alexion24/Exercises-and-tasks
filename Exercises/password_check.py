# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    flag_upper = False
    flag_lower = False
    flag_digit = False
    for c in password:
        if c.isupper() and c.isalpha():
            flag_upper = True
        if c.islower() and c.isalpha():
            flag_lower = True
        if c.isdigit():
            flag_digit = True
    return flag_upper and flag_lower and flag_digit




# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))