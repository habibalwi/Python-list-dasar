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
