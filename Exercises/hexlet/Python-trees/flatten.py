def flatten(items):
    result = []

    def inner(items):
        for item in items:
            if isinstance(item, list):
                inner(item)
            else:
                result.append(item)
        return result
    inner(items)
    return result



print(flatten([]))  # []
print(flatten([2, [3, 5], [[4, 3], 2]])) # [2, 3, 5, 4, 3, 2]


# def normalize(item):
#     return flatten(item) if isinstance(item, list) else [item]
#
#
# def flatten(tree):
#     return sum(map(normalize, tree), [])
