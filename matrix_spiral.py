

row, col = map(int, input().split())
matrix = [[0] * col for _ in range(row)]

i = 1
x = 0
y = -1
d_row = 0
d_col = 1

while i <= row * col:
    if 0 <= x + d_row < row and 0 <= y + d_col < col and matrix[x + d_row][y + d_col] == 0:
        x += d_row
        y += d_col
        matrix[x][y] = i
        i += 1
    else:
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1
    
for h in range(row):
    for el in matrix[h]:
        print(str(el).ljust(3), end='')
    print()

