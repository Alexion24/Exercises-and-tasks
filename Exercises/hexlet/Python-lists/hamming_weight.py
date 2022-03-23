def hamming_weight(number):
    return str(bin(number)).count('1')


print(hamming_weight(101))
