import math


def format_segment(segment):
    word = f'{segment["word"]}s' if segment['count'] > 1 else segment['word']
    return f'{segment["count"]} {word}'


def format_duration(number):
    if number == 0:
        return 'now'

    list_of_dicts = [
        {'count': 60, 'word': 'second'},
        {'count': 60, 'word': 'minute'},
        {'count': 24, 'word': 'hour'},
        {'count': 365, 'word': 'day'},
        {'count': math.inf, 'word': 'year'}
    ]

    segments = []
    i = 0
    while number > 0:
        segment = number % list_of_dicts[i]['count']
        number = number // list_of_dicts[i]['count']
        if segment != 0:
            segments.append(
                {'count': math.floor(segment), 'word': list_of_dicts[i]['word']}
            )
        i += 1

    segments = segments[::-1]
    result = ''
    if len(segments) == 1:
        result += f'{format_segment(segments[0])}'
    else:
        for i in range(len(segments)):
            if segments[i] == segments[-1]:
                result += f'and {format_segment(segments[i])}'
            elif segments[i] == segments[-2]:
                result += f'{format_segment(segments[i])} '
            else:
                result += f'{format_segment(segments[i])}, '

    return result


print(format_duration(3600))
print(format_duration(7200))