row=int(input())
col=int(input())
matrix=[]
for i in range(row):
    rows=[]
    for i in range(col):
        rows.append(int(input()))
    matrix.append(rows)
for e in matrix:
    print(*e)
summ=0
for i in matrix:
    summ=summ+sum(i)
print(summ)
