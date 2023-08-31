def chess_transformer(coords):
    alpha_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return int(coords[1]) - 1, alpha_coords.index(coords[0])

row, col = chess_transformer(input())

chess_matrix = [['.'] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (row == i or col == j) or ((row - i)*(row - i) == (col - j)*(col - j)) or (-1 <= row - i <= 1 and -1 <= col - j <= 1):       
            chess_matrix[i][j] = '*'       
chess_matrix[row][col] = 'Q'
chess_matrix.reverse()

for el in chess_matrix:
    print(*el)