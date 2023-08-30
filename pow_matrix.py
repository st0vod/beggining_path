from copy import deepcopy
n = int(input())
A = [[int(el) for el in input().split()] for _ in range(n)]
B = A
k = int(input())
matrix = [[0] * n for _ in range(n)]
for _ in range(k-1):
    for i in range(n):
        for j in range(n):
            summa = 0
            for h in range(n):
                if j <= n - 1:
                    summa += A[i][h] * B[h][j]
            matrix[i][j]= summa
    B = deepcopy(matrix)    
for el in matrix:
    print(*el)