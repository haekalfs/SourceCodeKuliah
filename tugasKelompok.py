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