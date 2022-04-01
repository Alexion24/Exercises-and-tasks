def find_index_of_nearest(num, items):
    if not items:
        return None
    nearest = items[0]
    number = items[0]
    for c in items:
        diff = abs(num - c)
        if diff == 0:
            return items.index(c)
        if diff < nearest:
            nearest = diff
            number = c
    return items.index(number)


print(find_index_of_nearest(2, []) is None)
print(find_index_of_nearest(0, [15, 10, 3, 4]))
print(find_index_of_nearest(4, [7, 5, 3, 2]))
print(find_index_of_nearest(4, [7, 5, 4, 4, 3]))


# def find_index_of_nearest(number, source):
#     if source:
#         diff = list(map(lambda x: abs(x - number), source))
#         return diff.index(min(diff))
