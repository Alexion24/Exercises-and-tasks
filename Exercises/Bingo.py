import random

bingo = []
numbers = set()
while len(numbers) < 25:
    numbers.add(random.randint(1, 75))
bingo = [list(numbers)[i::5] for i in range(5)]


# print(bingo)
bingo[2][2] = 0

for c in bingo:
    print(*c, sep='\t')
# print(bingo)