def is_degenerated(segment):
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    return x1 == x2 and y1 == y2


def is_vertical(segment):
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    return x1 == x2 and y1 != y2


def is_horizontal(segment):
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    return x1 != x2 and y1 == y2


def is_inclined(segment):
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    return x1 != x2 and y1 != y2


line1 = (42, 1), (42, 2)


print(is_vertical(line1))
print(is_inclined(line1))
print(is_horizontal(line1))
print(is_degenerated(line1))
