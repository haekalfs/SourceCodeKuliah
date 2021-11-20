

matriks=([1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4])
#isi matriks 4x4
for a in range(4):
    for j in range(4):
        if a==j:
            matriks[a][j]=1
        if a<j:
            matriks[a][j]=0
        if a>j:
            matriks[a][j]=0


print(matriks[a][j])
