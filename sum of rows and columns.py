x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
row=len(x)
col=len(x[0])
sr=0
sc=0
d=0
for i in range (row):
    for j in range (col):
        sr=sr+x[i][j]
for i in range (row):
    for j in range(col):
        sc=sc+x[i][j]
for k in range(0,row):
    d=d+x[k][k]
print("the sum of rows:", sr)
print("the sum of column is :", sc)
print("the sum of diagonal is :", d)
