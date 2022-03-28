def gen_diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        if key not in dict1:
            result[key] = 'added'
        elif key not in dict2:
            result[key] = 'deleted'
        elif dict1[key] == dict2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result


print(gen_diff({"one": "eon", "two": "two", "four": True},
               {"two": "own", "zero": 4, "four": True}))
