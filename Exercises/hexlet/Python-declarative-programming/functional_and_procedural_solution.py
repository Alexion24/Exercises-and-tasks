def odds_from_odds(items):
    items = [items[i] for i in range(0, len(items), 2)]
    result = []
    print(items)
    for c in items:
        result.append([c[i] for i in range(0, len(c), 2)])
    return result


def keep_odds_from_odds(items):
    for i in range(len(items)-1, -1, -1):
        if i % 2 != 0:
            items.pop(i)
    print(items)
    for c in items:
        for i in range(len(c)-1, -1, -1):
            if i % 2 != 0:
                c.pop(i)


test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test2 = [[1, 2, 3, 4, 5], ['d', 'o', 'g'], [100, 200, 300, 400], [], []]
test3 = [
            [1, 2, 3, 4, 5],
            ['c', 'a', 't'],
            ['d', 'o', 'g'],
            [100, 200, 300, 400],
            [True, False],
            [],
            [],
        ]

print(odds_from_odds(test1))
print(odds_from_odds(test3))
print(odds_from_odds([]))
print(odds_from_odds([[]]))

keep_odds_from_odds(test1)
keep_odds_from_odds(test2)
keep_odds_from_odds(test3)
print(test1)
print(test2)
print(test3)
keep_odds_from_odds(test1)
keep_odds_from_odds(test2)
keep_odds_from_odds(test3)
print(test1)
print(test2)
print(test3)
keep_odds_from_odds([])
keep_odds_from_odds([[]])

# from operator import itemgetter
#
# odds = itemgetter(slice(None, None, 2))
# # ^ функция, которая вычисляет срез [::2] от аргумента
#
#
# def odds_from_odds(list_of_lists):
#     return list(map(odds, odds(list_of_lists)))
#
#
# def keep_odd(some_list):
#     del some_list[1::2]  # noqa: WPS420
#     # Инструкция "del", это очень низкоуровневое действие и напрямую
#     # использовать его мы не рекомендуем. Но другого способа очистить
#     # срез "по месту", да ещё и за одно действие нет,
#     # поэтому "del" здесь уместен.
#     # Наш линтер за "del" ругает, поэтому пришлось отключить предупреждение!
#
#
# def keep_odds_from_odds(list_of_lists):
#     keep_odd(list_of_lists)  # отбрасываем чётные списки первого уровня
#     for one_list in list_of_lists:  # затем в каждом из оставшихся списков...
#         keep_odd(one_list)  # ...отбрасываем чётные элементы
