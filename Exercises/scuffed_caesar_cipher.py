from string import punctuation

text = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

list_of_text = [c for c in text.split()]


def ceasar(text):
    result = ''
    counter = 0
    for c in text:
        if c.isalpha():
            counter += 1
    for c in text:
        for i in range(len(alphabet)):
            if c.lower() == alphabet[i]:
                new_c = alphabet[(i + counter) % len(alphabet)]
                if c == c.upper():
                    result += new_c.upper()
                else:
                    result += new_c
                    break
            if c in punctuation:
                result += c
                break
    return result


result = []
for c in list_of_text:
    for w in c:
        result.append(ceasar(c))
        break
result = ' '.join(result)
print(result)
