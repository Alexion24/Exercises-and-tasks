n, m = input().split()
n, m = int(n), int(m)

matrix = [[0] * m for i in range(n)]
# print(matrix)

counter = 0
di = 0
dj = 1
i = 0
j = 0
direction = 'right'

while counter < n * m:
    counter += 1
    # print(matrix[i][j])
    matrix[i][j] = counter
    # print(matrix[i][j])
    # print(counter, di, dj, direction, 'i =', i, 'j=', j)
    if (j == m - 1 or matrix[i][j+1] > 0) and direction == 'right':
        di, dj, direction = 1, 0, 'down'
    if (i == n - 1 or matrix[i+1][j] > 0) and direction == 'down':
        di, dj, direction = 0, -1, 'left'
    if (j == 0 or matrix[i][j-1] > 0) and direction == 'left':
        di, dj, direction = -1, 0, 'up'
    if (i == 0 or matrix[i-1][j] > 0) and direction == 'up':
        di, dj, direction = 0, 1, 'right'
    i += di
    j += dj

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()