n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
check_list = list(range(1, n+1))
flag = True
for i in range(n):
    rows = sorted(matrix[i])
    cols = sorted([matrix[j][i] for j in range(n)])
    if rows != check_list or cols != check_list:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')