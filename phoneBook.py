# ===== PROGRAM PHONE BOOK =====
# NIM   : 221524052
# NAMA  : NAIA SITI AZ-ZAHRA
# KELAS : 1B - TI4

phoneBook = {}

def displayMenu():
    print("===== Menu Aplikasi Phone Book =====")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Update Kontak")
    print("5. Display Kontak")
    print("6. Keluar")
    print()

def addContact():
    print("Tambahkan Nama dan Nomor Telepon")
    nama = input("Nama: ")
    nomor = input("Nomor Telepon: ")
    phoneBook[nama] = nomor

    with open("phoneBook.txt", "a") as file:
        notes = ""
        for i in phoneBook:
            notes = i + " " + phoneBook[i] + "\n"
        file.write(notes)
        
    #file.close()
    print("Data Berhasil Ditambahkan")
    print()

def deleteContact():
    print("Hapus Nama dan Nomor Telepon")
    nama = input("Nama: ")
    with open("phoneBook.txt", "r") as file :
        lines = file.readlines()
        
    with open("phoneBook.txt", "w") as file :
        deleted = False
        for line in lines :
            if line.startswith(nama + " "):
                deleted = True
            else :
                file.write(line)
        
        if deleted:
            del phoneBook[nama]
            print("Data Berhasil Dihapus")
        else:
            print(nama, "Data Tidak Ditemukan")
            
    print()

def updateContact():
    print("Update Nama dan Nomor Telepon")
    nama = input("Nama: ")
    if nama in phoneBook:
        nomor = input("Nomor Telepon: ")
        phoneBook[nama] = nomor

        with open("phoneBook.txt", "w") as file:
            for i in phoneBook:
                file.write(i + " " + phoneBook[i] + "\n")

            print("Data Berhasil Diperbarui")
            print()
    else:
            print(nama, "Data Tidak Ditemukan")
            print()

def searchContact():
    print("Cari Nama dan Nomor Telepon")
    nama = input("Nama: ")
    if nama in phoneBook:
        print("Nomor Telepon adalah", phoneBook[nama])
        print()
    else :
        print("Data", nama, "Tidak Ditemukan")
        print()
        
def displayContact():
    print("Menampilkan Daftar Nama dan Nomor Telepon")
    try:
        with open("phoneBook.txt", "r") as file:
            file_contents = file.read()
        if len(file_contents) == 0:
            print("Daftar Kontak Masih Kosong")
        else:
            print(file_contents)
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        
    # input("Press Enter to continue ...")
    print()

# Baca isi file phoneBook.txt dan simpan ke dictionary phoneBook
with open("phoneBook.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            nama, nomor = line.split()
            phoneBook[nama] = nomor

""" ========================= MAIN PROGRAM ========================= """

displayMenu()
pilihan = 0

while pilihan != "6":
    pilihan = str(input("Masukkan Pilihan (1 - 6) : "))
    if pilihan == "1":
        addContact()
        displayMenu()
        
    elif pilihan == "2":
        deleteContact()
        displayMenu()
        
    elif pilihan == "3":
        searchContact()
        displayMenu()
        
    elif pilihan == "4":
        updateContact()
        displayMenu()
        
    elif pilihan == "5":
        displayContact()
        displayMenu()
        
    elif pilihan != "6":
        displayMenu()
        displayMenu()        
