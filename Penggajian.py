def penggajian() :
    from texttable import Texttable
    table1 = Texttable ()
    no = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "y"
    
    while (jawab1 == 'y'):
        nama1.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'manager') :
            gaji.append(7000000)
            jawab1 = input("\nTambah Lagi? ")
            
        elif (jab == 'hrd') :
            gaji.append(5000000)
            jawab1 = input("\nTambah Lagi? ")
            
        elif (jab == 'direktur') :
            gaji.append(10000000)
            jawab1 = input("\nTambah Lagi? ")
            
        else :
            print ("=======Jabatan Tidak Ditemukan=======")
            jawab1 = input("\nTambah Lagi? ")
            
    no+=1
        
    
    for i in range (no) :

        table1.add_rows([['No','Nama','Jabatan','Gaji'],
                         [i+1, nama1[i],jabatan[i],gaji[i]]])                      
    print(table1.draw())

