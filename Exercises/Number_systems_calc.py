num = int(input())
base_num = ''
base = 2
while num > 0:
    base_num = str(num % base) + base_num
    num //= base
print(base_num)