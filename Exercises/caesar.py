text = input()
# alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for num in range(0, 25):
    result = ''
    for c in text:
        for i in range(len(alphabet)):
            if c.lower() == alphabet[i]:
                c = alphabet[(i - num) % len(alphabet)]
                break
        result += c
    print(result.capitalize())