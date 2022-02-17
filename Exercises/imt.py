def get_index(weight, height):
    return weight / height ** 2


def print_answer(imt):
    if 18.5 <= imt <= 25:
        print(f'Индекс массы тела = {imt:.2f} - Оптимальная масса тела')
    elif imt < 18.5:
        print(f'Индекс массы тела = {imt:.2f} - Недостаточная масса тела')
    else:
        print(f'Индекс массы тела = {imt:.2f} - Избыточная масса тела')


if __name__ == '__main__':
    weight, height = float(input()), float(input())
    print_answer(get_index(weight, height))