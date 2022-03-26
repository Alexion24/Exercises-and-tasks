def top_3_words(text):
    punctuation = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    for c in text.strip():
        if c == "'" and text.strip().count(c) == len(text.strip()):
            return []
    text = [c.strip(punctuation).lower() for c in text.split()]

    changed_words = []
    for word in text:
        new_word = ''
        for letter in word:
            if letter in punctuation:
                new_word += ' '
            else:
                new_word += letter
        changed_words.append(new_word)

    changed_words = [c.split() for c in changed_words]
    result = []
    for c in changed_words:
        for w in c:
            result.append(w)

    result = sorted(result, key=lambda x: result.count(x), reverse=True)
    answer = []
    for word in result:
        if word not in answer:
            answer.append(word)
        if len(answer) == 3:
            break

    return list(filter(bool, answer))