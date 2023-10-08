#Muhammad Abiya Makruf - 1301213157 - MTA
#TP MODUL 4

import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8008')

inputMenu = -1

while inputMenu != 0 :
    print("1. Daftar Calon")
    print("2. Voting")
    print("0. Exit")
    inputMenu = int(input("Masukkan pilihan menu: "))

    if inputMenu == 1:
        print(s.daftarCalon())
    elif inputMenu == 2:
        print("\n","="*15,"Selamat data di pemilihan ketua BEM","="*15)
        print("Silahkan masukkan angka")
        inputVoting = int(input("Masukkan pilihan vote: "))
        while inputVoting != 1 and inputVoting != 2:
            print("Pilihan tidak tersedia")
            inputVoting = int(input("Masukkan pilihan vote: "))
        print(s.voting(inputVoting))
    else:
        print()

print(s.hasilVoting())