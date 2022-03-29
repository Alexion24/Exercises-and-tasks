def merged(*args):
    result = {}
    for i in range(len(args)):
        for k, v in args[i].items():
            result.setdefault(k, set()).add(v)
    return result


print(merged({'A': 1},
             {'B': 2},
             {'C': 3}
             ))
print(merged({'A': 1},
             {'A': 2},
             {'A': 3}
             ))
