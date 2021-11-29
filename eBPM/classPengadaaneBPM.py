from prettytable import PrettyTable
from fpdf import FPDF
tblForm = PrettyTable()

#mylist
listProcurement = []
totalHarga = []

class PengadaanBarang:
    def barang(brg):
        global noPO
        global namaProduk
        global jumlahProduk
        global danaRequested
        global hargaBarang
        print("-------------------------------------------------------------------")
        print("                          eBPM Procurement")
        print("-------------------------------------------------------------------")
        noPO = input("Input Nomor PO (Purchase Order)... Exp : (001,002...)\n")
        namaProduk = input("Input Nama Barang yang akan diadakan : ")
        jumlahProduk = int(input("Input Jumlah Barang               : "))
        hargaBarang = int(input("Input Harga Satuan Barang         : "))
        danaRequested = int(input("Input Dana yang direquest         : "))
        print("-------------------------------------------------------------------\n")
        totalHarga.append(hargaBarang * jumlahProduk)
        tblForm.field_names = ("Nomor PO", "Nama Barang", "Jumlah", "Harga Satuan", "Dana Requested")
        tblForm.add_row([noPO,namaProduk,jumlahProduk,'{:,}'.format(hargaBarang),'{:,}'.format(danaRequested)])

def createPDF():
    global pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    pdf.cell(200, 10, txt = "Form Pengadaan eBPM", 
            ln = 1, align = 'C')
    
    pdf.cell(200, 10, txt = "Kelompok 1 19.1C.11 UBSI",
            ln = 2, align = 'C')

    pdf.cell(200, 20, txt = "________________________________________________________________",
         ln = 10, align = 'A')

    pdf.cell(200, 10, txt = "Nomor PO :",
            ln = 11, align = 'A')
    
    pdf.cell(200, 10, txt = noPO,
            ln = 11, align = 'A')

    pdf.cell(200, 10, txt = "Nama Produk :",
            ln = 13, align = 'A')
    
    pdf.cell(200, 10, txt = namaProduk,
            ln = 13, align = 'A')

    pdf.cell(200, 10, txt = "Jumlah Produk :",
            ln = 15, align = 'A')
    
    pdf.cell(200, 10, txt = str('{} - pcs'.format(jumlahProduk)),
            ln = 15, align = 'A')

    pdf.cell(200, 10, txt = "Harga Produk :",
            ln = 17, align = 'A')
    
    pdf.cell(200, 10, txt = str('Rp. {:,}'.format(hargaBarang)),
            ln = 17, align = 'A')

    pdf.cell(200, 10, txt = "Dana Request :",
            ln = 19, align = 'A')
    
    pdf.cell(200, 10, txt = str('Rp. {:,}'.format(danaRequested)),
            ln = 19, align = 'A')

    pdf.cell(200, 10, txt = "________________________________________________________________",
         ln = 20, align = 'A')
    pdf.cell(200, 10, txt = "Copyright to : Mahasiswa UBSI",
            ln = 21, align = 'C')

def startProgram():
    for i in range(jumlahPengadaan):
        print ("\nForm Pengadaan ke - " + str(i+1))
        PengadaanBarang().barang() #Calling Class "PengadaanBarang"
        Sum = sum(totalHarga)
        createPDF()
        pdf.output('Form Pengadaan eBPM' + str(i) + '.pdf') 
    #Output
    print("\nComputing... Please Wait... Creating Form....")
    print("-------------------------------------------------------------------")
    print("                         eBPM Procurement")
    print("-------------------------------------------------------------------")
    print(tblForm)
    print("Total Biaya Pengadaan Barang : Rp.",'{:,}'.format(Sum))
    print("Thank You For Using Our Program, Please wait for Approval by Directors.\n")

#Start
print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Procurement")
print("-------------------------------------------------------------------")

enter = input("Apakah anda yakin ingin melakukan pengadaan barang?...(Y/N)\n")
jumlahPengadaan = int(input("Berapa form pengadaan barang?...\n"))

print("\nLoading...")

#Running Program
if(enter=="Y" or enter=="y"):
    startProgram()
else:
    print("Thank you for using our program... Good Bye...")





""" Copyright to Haekal Sastradilaga"""