import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Approval")
print("-------------------------------------------------------------------")

enter = input("Tekan enter untuk melanjutkan...\n")
userChoice = input("Apakah anda ingin melakukan proses Approval 'Pengadaan Barang'?...(Y/N) :")
print("-------------------------------------------------------------------")
print("Pilih File Form Cetak Pengadaan Barang Yang Ingin di Approve...\n")

if(userChoice=="Y" or userChoice=="y"):

    file_path = filedialog.askopenfilename()
    fileReader = PyPDF2.PdfFileReader(file_path)

    print("Please Wait... Creating Form...\n")
    print("Approving Form... Creating Sign...\n")

    pdfTwo = PyPDF2.PdfFileReader(open("eBPM/approve.pdf", "rb"))

    output = PdfFileWriter()

    output.addPage(pdfTwo.getPage(0))
    output.addPage(fileReader.getPage(0))

    outputStream = open(r"eBPM/outputFormApproval/Form Pengadaan (Approved).pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    print("-------------------------------------------------------------------")
    print("File telah tersimpan di folder program eBPM...")
    print("Thank you for using our program...")
    print("-------------------------------------------------------------------")
elif(userChoice=="N" or userChoice=="n"):
    print("Thank you for using our program...")
else:
    print("Please input y/N as instructed...")







""" Copyright to Haekal Sastradilaga"""