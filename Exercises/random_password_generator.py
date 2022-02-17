import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

my_random = random.SystemRandom()

chars = ''


def is_valid_number(number):
    return number.isdigit() and int(number) > 0


def is_valid_answer(answer):
    return answer == 'да' or answer == 'нет'


def add_digits():
    global chars
    while True:
        print('Включать ли цифры? да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Попробуйте ввести "да" или "нет"')
        if answer == 'да':
            chars += ''.join(set(digits) - set('Iil1Lo0O'))
            break
        elif answer == 'нет':
            break
    return chars


def add_uppercase():
    global chars
    while True:
        print('Включать ли прописные буквы? да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Попробуйте ввести "да" или "нет"')
        if answer == 'да':
            chars += ''.join(set(ascii_uppercase) - set('Iil1Lo0O'))
            break
        elif answer == 'нет':
            break
    return chars


def add_lowercase():
    global chars
    while True:
        print('Включать ли строчные буквы? да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Попробуйте ввести "да" или "нет"')
        if answer == 'да':
            chars += ''.join(set(ascii_lowercase) - set('Iil1Lo0O'))
            break
        elif answer == 'нет':
            break
    return chars


def add_punctuation():
    global chars
    while True:
        print('Включать ли символы !#$%&*+-=?@^_ ? да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Попробуйте ввести "да" или "нет"')
        if answer == 'да':
            chars += ''.join(punctuation)
            break
        elif answer == 'нет':
            break
    return chars


def add_strange_symbols():
    global chars
    while True:
        print('Включать ли символы Iil1Lo0O ? да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Попробуйте ввести "да" или "нет"')
        if answer == 'да':
            chars += ''.join('Iil1Lo0O')
            break
        elif answer == 'нет':
            break
    return chars


def get_chars():
    global chars
    chars = add_digits() + add_uppercase() + add_lowercase() + add_punctuation() + add_strange_symbols()
    return chars


def get_password_quantity():
    while True:
        print('Какое кол-во паролей вы хотите сгенерировать?')
        num = input()
        if not is_valid_number(num):
            print('Попробуйте ввести целое число больше 0! (кол-во паролей)')
        else:
            num = int(num)
            break
    return num


def get_password_length():
    while True:
        print('Введите длину вашего пароля:')
        pass_length = input()
        if not is_valid_number(pass_length):
            print('Попробуйте ввести целое число больше 0! (кол-во символов в вашем пароле)')
        else:
            pass_length = int(pass_length)
            break
    return pass_length


def get_password(quantity, length, alphabet):
    for i in range(quantity):
        password = ''
        for j in range(length):
            password += my_random.choice(alphabet)
        print('Ваш вариант пароля', password)


get_password(get_password_quantity(), get_password_length(), get_chars())
