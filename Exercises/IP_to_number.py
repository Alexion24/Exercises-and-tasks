from functools import reduce


def get_number(ip):
    ip = [int(c) for c in ip.split('.')]
    print(ip)
    number = ip[0] * 256**3 + ip[1] * 256 ** 2 + ip[2] * 256 + ip[3]
    print(number)
    total = 0
    for i in range(len(ip)):
        total += ip[i] * 256 ** (len(ip) - (i + 1))
    print(total)

    print(reduce(lambda out, x: out * 256 + int(x), ip, 0))


get_number('127.10.10.10')