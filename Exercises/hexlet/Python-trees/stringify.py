def print_dict(data, depth, get_indent):
    indent = get_indent(depth)
    string = ''
    for key, value in data.items():
        if isinstance(value, dict):
            result = print_dict(value, depth + 1, get_indent)
            string += f'{indent}{key}: {{\n{result}{indent}}}\n'
        else:
            string += f'{indent}{key}: {value}\n'
    return string


def stringify(data, replacer=' ', space=1):
    depth = 0
    get_indent = lambda d: d * space * replacer
    if isinstance(data, dict):
        result = print_dict(data, depth + 1, get_indent)
        return f'{{\n{result}}}'
    else:
        return str(data)


print(stringify('hello'))  # значение приведено к строке, но не имеет кавычек
# hello
print(stringify(True))
# True
print(stringify(5))
# 5

data = {"hello": "world", "is": True, "nested": {"count": 5}}
print(stringify(data))  # то же самое что stringify(data, ' ', 1)
# {
#   hello: world
#   is: True
#   nested: {
#    count: 5
#   }
# }
print(stringify(data, '|-', 2))  # символ, переданный вторым аргументом повторяется столько раз, сколько указано третьим аргументом
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }


# from itertools import chain
#
#
# def stringify(value, replacer=' ', spaces_count=1):
#
#     def iter_(current_value, depth):
#         if not isinstance(current_value, dict):
#             return str(current_value)
#
#         deep_indent_size = depth + spaces_count
#         deep_indent = replacer * deep_indent_size
#         current_indent = replacer * depth
#         lines = []
#         for key, val in current_value.items():
#             lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
#         result = itertools.chain("{", lines, [current_indent + "}"])
#         return '\n'.join(result)
#
#     return iter_(value, 0)
