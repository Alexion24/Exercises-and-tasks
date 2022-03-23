def is_continuous_sequence(sequence):
    flag = True
    if len(sequence) <= 1:
        flag = False
    for i in range(len(sequence) - 1):
        if sequence[i+1] - sequence[i] != 1:
            flag = False
    return flag


print(is_continuous_sequence([10, 11, 12, 14, 15]))
