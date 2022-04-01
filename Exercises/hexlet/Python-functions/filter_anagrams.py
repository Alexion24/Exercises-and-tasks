from collections import Counter


def filter_anagrams(item, anagrams):
    result = []
    for anagram in anagrams:
        if Counter(item) == Counter(anagram):
            result.append(anagram)
    return result


print(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
print(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))


# def normalized(string):
#     return list(sorted(string))
#
#
# def filter_anagrams(word, words):
#     norm = normalized(word)
#     return filter(lambda item: normalized(item) == norm, words)

