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
print(" ")
if (User=="Y" or User=="y"):
    def codeOwner(nama):
        print("Tugas Kelompok =", nama)

    def fungsiPrint(valueDrPrint):
        for i in valueDrPrint:
            print(i)

    Matriks1 = []
    Matriks2 = []

    for i in range(1):
            a, b, c = [int(x) for x in input("Input 3 Angka Untuk Matriks 1 Baris ke-1: Format 1,2,3\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks = [a, b, c]
            Matriks1.append(valMatriks)
            
            d, e, f = [int(x) for x in input("Input Baris ke-2:\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks = [d, e, f]
            Matriks1.append(valMatriks)

            d, e, f = [int(x) for x in input("Input Baris ke-3:\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks = [d, e, f]
            Matriks1.append(valMatriks)

    print(" ")
    print("\r+\r")
    print(" ")

    for i in range(1):
            a, b, c = [int(x) for x in input("Input 3 Angka Untuk Matriks 2 Baris 1:\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks = [a, b, c]
            Matriks2.append(valMatriks)
            
            d, e, f = [int(x) for x in input("Input Baris ke-2:\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks2 = [d, e, f]
            Matriks2.append(valMatriks2)
            
            x, y, z = [int(x) for x in input("Input Baris ke-3:\n").split(',' or ', ' or ' ,' or ' , ')]
            valMatriks3 = [x, y, z]
            Matriks2.append(valMatriks3)

    print(" ")
    print("Loading Data... Please Wait...")
    print(" ")
    print("Nilai Matriks 1 mu :")
    fungsiPrint(Matriks1)
    print(" ")
    print("Nilai Matriks 2 mu :")
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
    codeOwner("Haekal Sastradilaga : 19210677 \nNadif : 19, Fauzan : 19, Rifkhy : 19, Fariz : 19")
