def chess_transformer(coords):
    alpha_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return int(coords[1]), alpha_coords.index(coords[0]) + 1

n = input()
row, col = chess_transformer(n)

chess_matrix = [['.'] * 8 for _ in range(8)]
chess_matrix[row-1][col-1] = 'N'
for i in range(1, 9):
    for j in range(1, 9):
        if (row - i) ** 2 + (col - j) ** 2 == 5:
            chess_matrix[i-1][j-1] = '*'       
chess_matrix.reverse()
for el in chess_matrix:
    print(*el)