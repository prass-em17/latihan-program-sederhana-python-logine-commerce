
#I
from os import system
import time
import datetime
import threading
from datetime import datetime
import sys

#data
user={"emoney":300000, "token":0, "name":"pras", "pin":"0987", "unvalid":0}
#fungsi
#menu awal

def main():
    while True:
        print("        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===    Silahkan Pilih Menu Yang Tersedia     ===~~~~~~~")
        print("        ================================================       ")
        print("        ===   1. Top Up                              ===       ")
        print("        ===   2. Skin Bundle                         ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ===   4. Voucher                             ===       ")
        print("        ================================================       ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            topup()
            break
        if plhn == 2:
            print("")
            print("")
            print("")
            skin()
            break
        if plhn == 3:
            exit()
        if plhn == 4:
            print("")
            print("")
            print("")
            timer()
        else :
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")

def vchr():
    while True:
        print("        ===                 VOUCHER                  ===~~~~~~~~")
        print("        ================================================        ")
        print("        ===   1. Token 35            Rp. 50.000      ===        ")
        print("        ===   2. Token 75            Rp. 120.000     ===        ")
        print("        ===   3. Token 150           Rp. 225.000     ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")

def invchr():
    while True:
        print("        ================================================       ")
        print("        ===      Silahkan Masukkan Kode Voucher      ===~~~~~~~~")
        print("        ================================================        ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))


def topup():
    while True: 
        print("        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===       Silahkan Pilih Nominal Top Up      ===~~~~~~~~")
        print("        ================================================        ")
        print("        ======== Nominal ============== Harga ==========        ")
        print("        ===   1. Token 35            Rp. 50.000      ===        ")
        print("        ===   2. Token 75            Rp. 120.000     ===        ")
        print("        ===   3. Token 150           Rp. 225.000     ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            tkn35()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 2:
            print("")
            print("")
            print("")
            tkn75()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 3:
            print("")
            print("")
            print("")
            tkn130()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 4:
            exit()
        else :
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")

def skin():
    while True:
        print("        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===        Silahkan Pilih Skin Bundle        ===~~~~~~~~")
        print("        ================================================        ")
        print("        ======== Skin ================= Harga ==========        ")
        print("        ===   1. Skin M416 Volcano    60 Token       ===        ")
        print("        ===   2. Skin AKM Draconic    95 Token       ===        ")
        print("        ===   3. Skin AWP Pharaoh    140 Token       ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            skn1()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 2:
            print("")
            print("")
            print("")
            skn2()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 3:
            print("")
            print("")
            print("")
            skn3()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 4:
            exit()
        else :
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
        


#ulang
def ulangpin():
    while True: 
        print("        ===   1. Masukkan Pin Lagi                   ===       ")
        print("        ===   2. Keluar                              ===       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            break
        elif ulang == 2:
            exit()
def ulang1():
    while True: 
        print("        ===    Apakah anda ingin mengulang lagi?     ===       ")
        print("        ================================================       ")
        print("        ===   1. Kembali                             ===       ")
        print("        ===   2. Ke Menu Utama                       ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ================================================       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            topup()
            break
        elif ulang == 2:
            print("")
            print("")
            print("")
            main()
            break
        elif ulang == 3:
            exit()
        else :
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            break

def ulang2():
    while True: 
        print("        ===    Apakah anda ingin mengulang lagi?     ===       ")
        print("        ================================================       ")
        print("        ===   1. Kembali                             ===       ")
        print("        ===   2. Ke Menu Utama                       ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ================================================       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            skin()
            break
        elif ulang == 2:
            print("")
            print("")
            print("")
            main()
            break
        elif ulang == 3:
            exit()
        else :
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            break

#TOPUP
def tkn35():
    if(int(user["emoney"]) < 50000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 50000
        user["emoney"] = c
        d =int(user["token"]) + 35
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

def tkn75():
    if(int(user["emoney"]) < 120000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 120000
        user["emoney"] = c
        d =int(user["token"]) + 75
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

def tkn130():
    if(int(user["emoney"]) < 225000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 225000
        user["emoney"] = c
        d =int(user["token"]) + 150
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

#SKIN
def skn1():
    if(int(user["token"]) < 60) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["token"]) - 60
        user["token"] = c
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

def skn2():
    if(int(user["token"]) < 95) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["token"]) - 95
        user["token"] = c
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

def skn3():
    if(int(user["token"]) < 140) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["token"]) - 140
        user["token"] = c
        print("        ================================================       ")
        print("                  Pembelian anda telah berhasil")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 


def timer():
    global timerku
    timerku = 5
    for x in range (5):
        timerku = timerku - 1
        sleep(1)
    valid = int(user["unvalid"]) + 1
    

#WELCOME
jam = datetime.now()
waktu = int(jam.strftime("%H"))
print (jam.strftime("[ TANGGAL = %d/%b/%Y ]      [ WAKTU = %H:%M:%S ]"))
while True :
    namein = input("Masukkan Username Anda : ")
    pinin = input("Masukkan PIN Anda : ")
    if namein == user["name"] and pinin == user["pin"]:
        print("        ================================================        ")
        print("                        Pin Anda Benar ")
        print("        ================================================        ")
        break
    else :
        print("        ================================================        ")
        print("                        Pin Anda Salah ")
        print("               Silahkan Masukkan PIN Anda Kembali")
        print("        ================================================        ")
        ulangpin()

usia = int(input("Masukkan Usia Anda : "))
if waktu >= 0 and waktu <= 10 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 0 and waktu <= 10 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 0 and waktu <= 10 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")


main()

