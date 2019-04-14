from getpass import getpass
nama = "habib"
kunci = "123456"
lagi='y'
a=0
while lagi=='y':
    print("\tSILAHKAN LOGIN")
    print("")
    username = input("Masukkaan Username : ")
    password = getpass("Masukkan Password : ")
    if username == nama and password == kunci :
        print ("PASSWORD BENAR")
        break
    elif username == nama or password == kunci :
        print ("\tSALAH SATU DARI USERNAME DAN PASSWORD SALAH")
    else:
        print ("\tSALAH SATU DARI USERNAME DAN PASSWORD SALAH")
        
from Perhitungan.Penggajian import penggajian
from Perhitungan.Kalkulator import kalkulator
from Perhitungan.Inputnilai import inputnilai
from Perhitungan.Pembayaran import pembayaran

def start():
    print ("====================SILAHKAN PILIH=====================")
    print("1. DATA GAJI KARYAWAN")
    print("2. INPUTNILAI MAHASISWA")
    print("3. PROGRAM KALKULATOR SEDERHANA")
    print("4. PEMBAYARAN MAHASISWA")
    print("5. EXIT")
    pilihan = input("\nMasukan Pilihan (1-5)?  ")
    if   pilihan == '1' :
         penggajian()
    elif pilihan == '2' :
         inputnilai()
    elif pilihan == '3' :
         kalkulator()
    elif pilihan == '4' :
         pembayaran()
    elif pilihan == '5' :
        print("TERIMA KASIH")
    else :
        print ("\n!!! Pilihan Tidak Ditemukan !!!")
    tambahan()

def tambahan() :
    tambah = input ("\nKembali Ke Menu Awal (y/t)? ")
    if tambah == 'y' :
        start()
        
    print ("TERIMAKASIH") ; input("")
   
start()
