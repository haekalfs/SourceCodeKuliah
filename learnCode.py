print("Soal Matriks Logika & Algoritma")
Enter = input("Tekan Enter Untuk Melanjutkan...")
print("Contoh Soal :")

def fungsiPrint(valueDrPrint):
    for i in valueDrPrint:
        print(i)

matriks1 = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8],
]

matriks2 = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8],
]

print("Matriks 1 :")
fungsiPrint(matriks1)
print(" ")
print("Matriks 2 :")
fungsiPrint(matriks1)
print(" ")

def hitungMatriks(valMatriks1, valMatriks2):
    for i in range(0, len(valMatriks1)):
        kolomMatriks = []
        for j in range(0, len(valMatriks1[0])):
            kolomMatriks.append(valMatriks1[i][j] + valMatriks2[i][j])
        print(kolomMatriks)

print("Hasil Matriks 1 + Matriks 2 :")
hitungMatriks(matriks1, matriks2)

print(" ")

User = input("Hitung Nilai Matriks dengan Inputan (Y/N) : ")
if (User=="Y" or User=="y"):
    def codeOwner(nama):
        print("Tugas Kelompok =", nama)

    def fungsiPrint(valueDrPrint):
        for i in valueDrPrint:
            print(i)

    a, b, c, d, e, f, g, h, i = [int(x) for x in input("Input 9 Angka Untuk Matriks 1 Ordo 3x3:\n").split(',' or ', ' or ' ,' or ' , ')]
    Matriks1 = [[a, b, c],[d, e, f], [g, h, i]]

    a2, b2, c2, d2, e2, f2, g2, h2, i2 = [int(x) for x in input("Input 9 Angka Untuk Matriks 2 Ordo3x3:\n").split(',' or ', ' or ' ,' or ' , ')]
    Matriks2 = [[a2, b2, c2],[d2, e2, f2], [g2, h2, i2]]

    print(" ")
    print(" ")
    print("Nilai Matriks 1 :")
    fungsiPrint(Matriks1)
    print(" ")
    print("Nilai Matriks 2 :")
    fungsiPrint(Matriks2)
    print(" ")

    def hitungMatriks(valMatriks1, valMatriks2):
        for i in range(0, len(valMatriks1)):
            kolomMatriks = []
            for j in range(0, len(valMatriks1[0])):
                kolomMatriks.append(valMatriks1[i][j] + valMatriks2[i][j])
            print(kolomMatriks)

    print("Hasil dari Penjumlahan Matriks mu yaitu :")
    hitungMatriks(Matriks1, Matriks2)

    print(" ")
    codeOwner("Haekal : Ketua \nNadif, Fauzan, Rifkhy, Fariz : Anggota")
