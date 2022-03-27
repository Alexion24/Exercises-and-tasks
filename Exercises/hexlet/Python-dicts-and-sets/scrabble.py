from collections import Counter


def scrabble(item1, item2):
    item1, item2 = item1.lower(), item2.lower()
    diff = Counter(item1) & Counter(item2)
    if diff != Counter(item2):
        return False
    return True


print(scrabble('rkqodlw', 'world'))
print(scrabble('scriptingjava', 'JavaScript'))