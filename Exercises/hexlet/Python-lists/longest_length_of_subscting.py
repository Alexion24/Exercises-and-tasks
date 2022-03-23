def find_longest_length(text):
    all_variants = []
    result = []
    for i in range(len(text)):
        for j in range(1, len(text) + 1 - i):
            all_variants.append(text[i:i + j])
    for c in all_variants:
        if len(c) == len(set(c)):
            result.append(c)
    if result:
        return len(max(result, key=len))
    else:
        return 0


print(find_longest_length('qweqrty'))
print(find_longest_length('a'))
print(find_longest_length('abcddef'))
print(find_longest_length('abbccddeffg'))
print(find_longest_length(''))