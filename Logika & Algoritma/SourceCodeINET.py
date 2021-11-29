def cetak_matriks(matriks):
 for row in matriks:
  print (row)

def panjang_matriks(matriks):
 return len(matriks[0])

def lebar_matriks(matriks):
 return len(matriks)

def hitung_matriks(mat_a, mat_b):
    temp_row = []
    temp_mat = []
    for i in range(0, lebar_matriks(mat_a)):
        for j in range(0, panjang_matriks(mat_a)):
            temp_row.append(mat_a[i][j] * mat_b[i][j]) #symbol + dapat diganti dengan * bila ingin menghitung perkalian
        temp_mat.append(temp_row)
        temp_row = []
    return temp_mat

matriks_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriks_b = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print ("MATRIKS A : ")
cetak_matriks(matriks_a)

print ("\nMATRIKS B : ")
cetak_matriks(matriks_b)

print ("\nHASIL PENJUMLAHAN MATRIKS : ")
hasil = hitung_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)
