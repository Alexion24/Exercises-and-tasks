def binary_sum(str_num1, str_num2):
    result = int(str_num1, 2) + int(str_num2, 2)
    return bin(result)[2:]


print(binary_sum('1101', '101'))
