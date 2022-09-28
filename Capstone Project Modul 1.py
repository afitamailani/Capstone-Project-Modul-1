datapasien = {}

kode=1

def tambah():
    sub_menu = 0
    while(sub_menu != 2):
        print("-------  Menambah Data Pasien  -------")
        print("**************************************")
        print(" 1. Tambah Data Pasien                ")
        print(" 2. Kembali Ke Menu Utama             ")
        print("**************************************")
        sub_menu = int(input('Silahkan Pilih Sub Menu Tambah Data Pasien [1-2] : '))
        
        if sub_menu == 1:
            
            key = input("Masukkan NRM : ")
            if key in datapasien:
                print("Maaf NRM telah terdaftar!")
            else:
                nama = input("Masukkan nama : ")
                usia = input("Masukkan usia : ")
                poli = input("Masukkan poli : ")
                domisili = input("masukan domisili : ")
                no_telepon = input("masukan no telepon : ")
                
                temp = {"nama":nama,"usia":usia,"poli":poli,"domisili":domisili,"no_telepon":no_telepon} 
                
                yakin='A'
                while (yakin != 'NO' or yakin !='no'):
                    yakin = input("Apakah Data Akan Disimpan? (YES/NO) : ")
                    if(yakin=='yes' or yakin=='YES'):
                        datapasien.update({key : temp}) 
                        print("Data Baru Tersimpan!")
                        break

def lihat():
    sub_menu = 0
    while(sub_menu != 3):
        print ("-------  Report Data Pasien  -------")
        print ("**************************************")
        print (" 1. Lihat Seluruh Data               ")
        print (" 2. Lihat Data Tertentu              ")
        print (" 3. Kembali Ke Menu Utama             ")
        print ("**************************************")
        sub_menu = int(input('Silahkan Pilih Sub Menu Lihat Data Pasien [1-3] : '))
        
        if sub_menu==1:
            if(len(datapasien)>0):
                i = 0
                for NRM, pasien in datapasien.items():
                    print("%d. NRM : %s, nama : %s, usia : %s, poli : %s, domisili: %s, no_telepon: %s" % (i+1,NRM,pasien['nama'],pasien['usia'],pasien['poli'],pasien['domisili'],pasien['no_telepon'] ))
            else:
                print("Pasien Tidak terdaftar")
        elif sub_menu==2:
            NRM = input('Masukan NRM :')
            if NRM in datapasien:
                print("Data Pasien Dengan NRM "+NRM)
                print("1. NRM : %s, nama : %s, usia : %s, poli : %s, domisili : %s, no_telepon : %s" % (NRM,datapasien[NRM]['nama'],datapasien[NRM]['usia'],datapasien[NRM]['poli'],datapasien[NRM]['domisili'],datapasien[NRM]['no_telepon'] ))
            else:
                print("Pasien Tidak terdaftar")

def ubah():
    sub_menu = 0
    while(sub_menu != 2):
        print ("-------  Mengubah Data Pasien  -------")
        print ("**************************************")
        print (" 1. Ubah Data Pasien                  ")
        print (" 2. Kembali Ke Menu Utama             ")
        print ("**************************************")
        sub_menu = int(input('Silahkan Pilih Sub Menu Ubah Data Pasien [1-2] : '))
        
        if sub_menu == 1:
            
            key = input("Masukkan NRM : ")
            if key in datapasien:
                print("Data Pasien Dengan NRM "+key)
                print("1. NRM : %s, nama : %s, usia : %s, poli : %s, domisili : %s, no_telepon : %s" % (key,datapasien[key]["nama"],datapasien[key]["usia"],datapasien[key]["poli"], datapasien[key]["domisili"], datapasien[key]["no_telepon"] ))
                
                yakin='A'
                while (yakin != 'NO' or yakin !='no'):
                    yakin = input("Tekan YES jika ingin lanjut Update, tekan NO jika ingin batalkan? (YES/NO) : ")
                    if(yakin=='yes' or yakin=='YES'):
                        col = input("Masukan keterangan yang akan diedit:")
                        if col in datapasien[key]:
                            new_value = input("Masukan %s Baru : "%col)
                            y_up='A'
                            while (y_up != 'NO' or y_up !='no'):
                                y_up = input("Apakah Data akan diupdate? (YES/NO) : ")
                                if(y_up=='yes' or y_up=='YES'):
                                    datapasien[key][col] = new_value
                                    print("Data Pasien Berhasil di Update!")
                                    break
                                elif(y_up=='no' or y_up=="NO"):
                                    print("Data Pasien Gagal di Update!")
                        else:
                            print("Maaf Keterangan tidak ada!")
                            
                        break
                            
                    elif(yakin=='NO' or yakin !='no'):
                        print("Data Tidak Jadi di Update!")                
            else:
                print("Maaf Data dengan NRM %s tidak terdaftar!"%(key))
                

def hapus():
    sub_menu = 0
    while(sub_menu != 2):
        print ("------- Menghapus Data Pasien  -------")
        print ("**************************************")
        print (" 1. Hapus Data Pasien                 ")
        print (" 2. Kembali Ke Menu Utama             ")
        print ("**************************************")
        sub_menu = int(input('Silahkan Pilih Sub Menu Hapus Data Pasien [1-2] : '))
        
        if sub_menu == 1:
            key = input("Masukkan NRM : ")
            if key in datapasien:
                yakin='A'
                while (yakin != 'NO' or yakin !='no'):
                    yakin = input("Apakah Data yakin dihapus? (YES/NO) : ")
                    if(yakin=='yes' or yakin=='YES'):
                        del datapasien[key]
                        print("Data Pasien Terhapus!")
                        break
                    elif(yakin=='no' or yakin=="NO"):
                        print("Data Pasien Gagal dihapus!")
            else:
                print("Data dengan NRM %s tidak dapat ditemukan!"%(key))
            

while kode !=5 :
    print ("------- Data Pasien RS Hasan Sadikin -------")
    print ("**************************************")
    print (" 1. Report Data Pasien                ")
    print (" 2. Tambah Data Pasien      ")
    print (" 3. Ubah Data Pasien         ")
    print (" 4. Hapus Data Pasien        ")
    print (" 5. Keluar                       ")
    print ("**************************************")
    kode = int(input('Silahkan Pilih Main Menu [1-5] : '))

    if kode == 1:
        lihat()
    elif kode ==2:
        tambah()
    elif kode == 3:
        ubah()
    elif kode == 4:
        hapus()
    elif kode == 5:
        print("Terimakasih")
        break
    else :
        print("Pilihan salah, tolong cek kembali!")
        