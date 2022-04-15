def convert(array):
    result = {k: v for k, v in array}
    for k, v in result.items():
        if type(v) == list:
            result[k] = convert(v)
    return result


print(convert([]))
# {}
print(convert([('key2', 'value2'), ('key', 'value')]))
# {'key2': 'value2', 'key': 'value'}
print(convert([
    ('key', [('key2', 'anotherValue')]),
    ('key2', 'value2')
]))
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}



# def to_item(item):
#     key, value = item
#     return key, convert(value) if isinstance(value, list) else value
#
#
# def convert(tree):
#     return dict(map(to_item, tree))


