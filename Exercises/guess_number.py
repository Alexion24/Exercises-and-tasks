import random


def is_valid_right_num(n):
    return n.isdigit() and int(n) >= 2


def is_valid(num, n):
    return num.isdigit() and 1 <= int(num) <= n


def is_valid_answer(answer):
    return answer == 'да' or answer == 'нет'


def game():
    print('Добро пожаловать в числовую угадайку', '\n')
    print('Введите целое число >= 2, до которого мы будем угадывать (правую границу):')
    while True:
        n = input()
        if not is_valid_right_num(n):
            print('Попробуйте ввести целое число ещё раз!')
        else:
            n = int(n)
            break
    result_num = random.randint(1, n)
    print(f'Введите число от 1 до {n}:')
    tries_count = 0
    while True:
        num = input()
        if not is_valid(num, n):
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
        else:
            num = int(num)
            if num < result_num:
                print('Ваше число меньше загаданного, попробуйте ещё разок')
                tries_count += 1
            elif num > result_num:
                print('Ваше число больше загаданного, попробуйте ещё разок')
                tries_count += 1
            elif num == result_num:
                print('Вы угадали, поздравляем!', '\n')
                print('Ваше число попыток:', tries_count, '\n')
                if tries_count > 7:
                    print(f'Ну ты и кадр, сейчас бы число с {tries_count} попыток угадать 4HEader', '\n')
                print('Спасибо, что играли в числовую угадайку. Ещё увидимся...', '\n')
                break


def game_menu():
    game()
    while True:
        print('Хотите сыграть ещё?', 'да/нет')
        answer = input()
        if not is_valid_answer(answer):
            print('Я верю, что у тебя получится ввести "да" или "нет"')
        else:
            if answer == 'да':
                game()
            if answer == 'нет':
                print('Удачи!!!')
                break


game_menu()
