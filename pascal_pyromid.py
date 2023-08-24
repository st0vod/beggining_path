def pascale():
    n = int(input()) + 1
    p = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = p[i-1][j-1] +p[i-1][j]
        p.append(row)
    return p[n-1]

print(pascale())