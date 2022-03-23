def length_of_last_word(text):
    text = text.split()
    if text:
        return len(text[-1])
    else:
        return 0


print(length_of_last_word('hello\t\nworld'))
