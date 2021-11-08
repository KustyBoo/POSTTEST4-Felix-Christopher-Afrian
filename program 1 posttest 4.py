# program edit menu

import sys


def menu_berubah() :
    menu_makanan = [
    ["nasi goreng","mie goreng","lontong sayur"],
    ["teh es","teh hangat","jeruk es","jeruk hangat","air mineral"]
    ]

    makanan = ["nasi goreng","mie goreng","lontong sayur"]
    tengah_makanan = len(makanan) // 2

    minuman = ["teh es","teh hangat","jeruk es","jeruk hangat","air mineral"]
    tengah_minuman = len(minuman) // 2
    print ("|===============================================================|")
    print ("|======Silahkan pilih menu yang telah tersedia di bawah ini=====|")
    print ("|===============================================================|")
    print ("|Menu Makanan :                 Harga :                         |")
    print ("|1. nasi Goreng                 Rp18.000                        |")
    print ("|2. mie Goreng                  Rp22.000                        |")
    print ("|3. lontong Sayur               Rp17.000                        |")
    print ("|===============================================================|")
    print ("|===============================================================|")
    print ("|Menu Minuman :                 Harga :                         |")
    print ("|1. teh es/hangat               Rp 6.000                        |")
    print ("|2. jeruk es/hangat             Rp 8.000                        |")
    print ("|3. air mineral                 Rp 5.000                        |")
    print ("|===============================================================|")
    print ("|===============================================================|")
    x = input("|Apakah anda ingin mengedit menu makanan atau menu minuman?\n|Ketik \"makanan\" untuk mengubah menu makanan atau \"minuman\" untuk mengubah menu minuman = ")
    if x == "makanan" or x == "Makanan" or x == "MAKANAN" :
        print ("|Daftar menu makanan : ")
        print (*makanan, sep=", ")
        print ("|Apakah anda ingin menambahkan menu makanan? (ketik \"tambah\")")
        print ("|Apakah anda ingin menghapus menu makanan? (ketik \"hapus\")")
        print ("|Apakah anda ingin mengganti nama menu makanan? (ketik \"ganti\")")
        masuk = input("|Silahkan ketik pilihan anda disini = ")
        for x in masuk :
            if masuk == "tambah" or masuk == "Tambah" or masuk == "TAMBAH" :
                tambah = input("|Silahkan pilih apakah anda ingin menambahkan menu makanan di tengah atau di akhir\n|Ketik \"tengah\" atau \"akhir\" = ")
                if tambah == "tengah" or tambah == "Tengah" or tambah == "TENGAH" :
                    tengah = input("|Silahkan masukkan nama makanan = ")
                    makanan = makanan[0:tengah_makanan] + [tengah] + makanan[tengah_makanan:]
                    print ("|Berikut daftar menu makanan yang telah anda tambah = ")
                    print (makanan)
                    print ("|Apakah anda ingin menambahkan menu makanan lain di tengah? ketik \"tambah\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "Exit" or masuk == "EXIT" :
                        print ("|Terima kasih, selamat tinggal !|")
                        sys.exit()
                elif tambah == "akhir" or tambah == "AKHIR" or tambah == "Akhir" :
                    tambah1 = input("|Silahkan masukkan nama makanan = ")
                    makanan.append(tambah1)
                    menu_makanan[0].append(tambah1)
                    print ("|Berikut daftar menu makanan yang telah anda tambah = ")
                    print (makanan)
                    print ("|Apakah anda ingin kembali menambahkan menu makanan lain? (ketik \"tambah\" atau jika anda ingin memberhentikan program, ketik \"exit\"")
                    masuk = input("|Ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "Exit" or masuk == "EXIT" :
                        print ("|Berikut daftar menu makanan yang telah anda edit = ")
                        for x in menu_makanan :
                            print (*x, sep=", ")
                        print ("|Terima kasih, selamat tinggal !|")
                        sys.exit()
                
            elif masuk == "hapus" or masuk == "HAPUS" or masuk == "Hapus" :
                hapus = input("|Silahkan masukkan nama menu makanan yang akan dihapus = ")
                if hapus == "nasi goreng" :
                    makanan.remove("nasi goreng")
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin menghapus menu makanan lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "mie goreng" :
                    makanan.remove("mie goreng")
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin menghapus menu makanan lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "lontong sayur" :
                    makanan.remove("lontong sayur")
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin menghapus menu makanan lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
            elif masuk == "ganti" or masuk == "Ganti" or masuk == "GANTI" :
                ganti = input("|Silahkan masukkan nama menu makanan yang akan diganti = ")
                if ganti == "nasi goreng" :
                    ganti1 = input("|Silahkan masukkan nama makanan penggantinya = ")
                    makanan[0] = (ganti1)
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin mengganti menu makanan lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif ganti == "mie goreng" :
                    ganti1 = ganti1 = input("|Silahkan masukkan nama makanan penggantinya = ")
                    makanan[1] = (ganti1)
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin mengganti menu makanan lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif ganti == "lontong sayur" :
                    ganti1 = input("|Silahkan masukkan nama makanan penggantinya = ")
                    makanan[2] = (ganti1)
                    print ("|Berikut daftar menu makanan setelah diganti = ")
                    print (makanan)
                    print ("|Apakah anda ingin mengganti menu makanan lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
    elif x == "minuman" or x == "MINUMAN" or x == 'Minuman' :
        print ("|Daftar menu minuman : ")
        print (*minuman, sep=", ")
        print ("|Apakah anda ingin menambahkan menu minuman? (ketik \"tambah\")")
        print ("|Apakah anda ingin menghapus menu minuman? (ketik \"hapus\")")
        print ("|Apakah anda ingin mengganti nama menu minuman? (ketik \"ganti\")")
        masuk = input("|Silahkan ketik pilihan anda disini = ")
        for x in masuk :
            if masuk == "tambah" or masuk == "Tambah" or masuk == "TAMBAH" :
                tambah = input("|Silahkan pilih apakah anda ingin menambahkan menu minuman di tengah atau di akhir\n|Ketik \"tengah\" atau \"akhir\" = ")
                if tambah == "tengah" or tambah == "Tengah" or tambah == "TENGAH" :
                    tengah = input("|Silahkan masukkan nama minuman = ")
                    minuman = minuman[0:tengah_minuman] + [tengah] + minuman[tengah_minuman:]
                    print ("|Berikut daftar menu minuman yang telah anda tambah = ")
                    print (minuman)
                    print ("|Apakah anda ingin menambahkan menu minuman lain di tengah? ketik \"tambah\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "Exit" or masuk == "EXIT" :
                        print ("|Terima kasih, selamat tinggal !|")
                        sys.exit()
                elif tambah == "akhir" or tambah == "AKHIR" or tambah == "Akhir" :
                    tambah1 = input("|Silahkan masukkan nama minuman = ")
                    minuman.append(tambah1)
                    menu_makanan[1].append(tambah1)
                    print ("|Berikut daftar menu minuman yang telah anda tambah = ")
                    print (minuman)
                    print ("|Apakah anda ingin kembali menambahkan menu minuman lain? (ketik \"tambah\" atau jika anda ingin memberhentikan program, ketik \"exit\"")
                    masuk = input("|Ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "Exit" or masuk == "EXIT" :
                        print ("|Berikut daftar menu makanan yang telah anda edit = ")
                        for x in menu_makanan :
                            print (*x, sep=", ")
                        print ("|Terima kasih, selamat tinggal !|")
                        sys.exit()
                        
            elif masuk == "hapus" or masuk == "HAPUS" or masuk == "Hapus" :
                hapus = input("|Silahkan masukkan nama menu minuman yang akan dihapus = ")
                if hapus == "teh es" :
                    minuman.remove("teh es")
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin menghapus menu minuman lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "teh hangat" :
                    minuman.remove("teh hangat")
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin menghapus menu minuman lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "jeruk es" :
                    minuman.remove("jeruk es")
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin menghapus menu minuman lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "jeruk hangat" :
                    minuman.remove("jeruk hangat")
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin menghapus menu minuman lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif hapus == "air mineral" :
                    minuman.remove("air mineral")
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin menghapus menu minuman lain? ketik \"hapus\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
            elif masuk == "ganti" or masuk == "Ganti" or masuk == "GANTI" :
                ganti = input("|Silahkan masukkan nama menu minuman yang akan diganti = ")
                if ganti == "teh es" :
                    ganti1 = input("|Silahkan masukkan nama minuman penggantinya = ")
                    minuman[0] = (ganti1)
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin mengganti menu makanan lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif ganti == "teh hangat" :
                    ganti1 = ganti1 = input("|Silahkan masukkan nama minuman penggantinya = ")
                    minuman[1] = (ganti1)
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin mengganti menu minuman lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif ganti == "jeruk es" :
                    ganti1 = input("|Silahkan masukkan nama minuman penggantinya = ")
                    minuman[2] = (ganti1)
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin mengganti menu minuman lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                            print ("|Terima kasih, selamat tinggal !|")
                            sys.exit()
                elif ganti == "jeruk hangat" :
                    ganti1 = input("|Silahkan masukkan nama minuman penggantinya = ")
                    minuman[3] = (ganti1)
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin mengganti menu minuman lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                        print ("|Terima kasih, selamat tinggal !|")
                        sys.exit()    
                elif ganti == "air mineral" :
                    ganti1 = input("|Silahkan masukkan nama minuman penggantinya = ")
                    minuman[4] = ganti1
                    print ("|Berikut daftar menu minuman setelah diganti = ")
                    print (minuman)
                    print ("|Apakah anda ingin mengganti menu minuman lain? ketik \"ganti\" atau \"exit\" untuk keluar = ")
                    masuk = input("|Silahkan ketik jawaban anda disini = ")
                    if masuk == "exit" or masuk == "EXIT" or masuk == "Exit" :
                        print("|Terima kasih, selamat tinggal !|")
                        sys.exit()

def main_menu () :
    print ("       /   \                          /  \                          ")
    print ("      /  /\ \                        / /\ \                         ")
    print ("     /  /  \ \                      / /  \ \                        ") 
    print ("    /  /    \ \                    / /    \ \                       ")
    print ("   /  /      \ \                  / /      \ \                      ")
    print ("  /  /        \ \    KustyBoo    / /        \ \                     ")
    print (" /  /          \ \______________/ /          \ \                    ")
    print("|                                               |                   ")
    print("|         000                     000           |                   ")
    print("|        0 | 0                   0 | 0          |                   ")
    print("|        0 | 0                   0 | 0          |                   ")
    print("|        0 | 0          |        0 | 0          |                   ")
    print("|          0           |           0            |                   ")
    print("|                       |                       |                   ")
    print("|                                               |                   ")
    print("|             ||      |||||      ||             |                   ")
    print("|              ||    ||   ||    ||              |                   ")
    print("|               ||||||     ||||||               |                   ")
    print("|                                               |                   ")
    print("|                                               |                   ")
    print("|_______________________________________________|                   ")
    print("|===================== uwu =====================|")
    print ("|-----------------------------------------------|")
    print ("|-----Halo, Selamat Datang di Program Menu------|")
    print ("|-------Made by Felix Christopher Afrian--------|")
    print ("|-----------------------------------------------|")
    print ("|------------Type \"mulai\" to enter--------------|")
    x = input("|ketik mulai = ")
    while x == "mulai" or x == "MULAI" or x == "Mulai" :
        if x == "mulai" or x == "Mulai" or x == "MULAI" :
            menu_berubah()
        else :
            print ("system error, please restart the program")
    return


main_menu()         