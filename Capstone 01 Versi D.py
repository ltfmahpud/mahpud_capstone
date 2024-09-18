#Salam pembuka
print("\nSelamat datang di Database Jakarta Lezaat")
print("\"Lidah bergoyang, Hidup panjang, Hati pun sanang\"")

#Variabel Database
database_v4 = {
        "JTM-01": {
            "Nama": "Soto Betawi H. Ma'ruf",
            "Lokasi": "Rawamangun",
            "Bestseller": "Soto Betawi",
            "Price": range(30000, 50000), #Dalam IDR
            "Review_google": 4.5, #Skala 1-5
            "Repeat_order": 70, #Persentase customer yang melakukan repeat order
            "Porsi_sayur": 30, #Persentase porsi sayur di hidangan 
            "Menu_kolesterol": 40 #Persentase menu kolesterol tinggi terhadap total menu 
        },
        "JPS-02": {
            "Nama": "Nasi Goreng Kambing Kebon Sirih",
            "Lokasi": "Menteng",
            "Bestseller": "Nasi Goreng Kambing",
            "Price": range(40000, 60000),
            "Review_google": 4.4,
            "Repeat_order": 65,
            "Porsi_sayur": 20,
            "Menu_kolesterol": 10
        },
        "JTM-03": {
            "Nama": "Restoran Sederhana",
            "Lokasi": "Cempaka Putih",
            "Bestseller": "Ayam Penyet",
            "Price": range(25000, 45000),
            "Review_google": 4.3,
            "Repeat_order": 60,
            "Porsi_sayur": 25,
            "Menu_kolesterol": 30
        },
        "JUT-04": {
            "Nama": "Kedai Tepi Laut",
            "Lokasi": "Ancol",
            "Bestseller": "Ikan Bakar",
            "Price": range(50000, 100000),
            "Review_google": 4.6,
            "Repeat_order": 75,
            "Porsi_sayur": 40,
            "Menu_kolesterol": 20
        },
}


#Fungsi A-READ data
def lihat_data ():
    while True:
        print("\nLihat Data Section\n--")
        print("1. Lihat seluruh database")
        print("2. Cari data menggunakan ID")
        print("3. Kembali ke Menu Utama")
        pilihan_read = int(input("Pilih action (1-3): "))
        if pilihan_read == 1: #Opsi 1.Lihat Seluruh Database
            if database_v4 != 0:
                print (f"\nDatabase updated:")
                for x in database_v4:
                    print(f"\nID : {x}")
                    for y,z in database_v4[x].items():
                        print (f"{y} : {z}")
            else:
                print("Mohon maaf, data tidak ditemukan")
                break

        elif pilihan_read == 2: #Opsi 2.Cari data by ID
            id_lihat = input("Input ID data: ")
            if id_lihat in database_v4.keys():
                print (f"\nBerikut data {id_lihat}:")
                for x,y in database_v4[id_lihat].items():
                    print(f"{x} : {y}")
            else:
                print("Data yang anda cari tidak ditemukan")

        elif pilihan_read == 3: #Opsi 3.Kembali ke Menu Utama
            break

#Fungsi B-ADD data
def tambah_data ():
    while True:
        print("\nTambah Data Section\n--")
        print("1. Tambah data")
        print("2. Kembali ke Menu Utama")

        pilihan_add = int(input("Pilih action (1-2): "))
        if pilihan_add == 1: #Opsi 1.Tambah Data
            id_tambah = input("Buat ID: ")
            if id_tambah in database_v4.keys():
                print("Data already exists")
                break
            else:
                inputan_tambah = {
                "Nama": input("Nama: "),
                "Lokasi": input("Lokasi: "),
                "Bestseller": input("Menu Bestseller: "),
                "Price": range(int(input("Harga menu termurah (IDR): ")), int(input("Harga menu termahal (IDR): "))),
                "Review_google": input("Review Google (skala 1-5): "),
                "Repeat_order": input("Repeat Order (%): "),
                "Porsi_sayur": int(input("Sayur terhadap hidangan (%): ")),
                "Menu_kolesterol": int(input("Menu kolesterol terhadap total Menu: ")),
                }
            while True:
                lanjut_save = input(f"Simpan data {inputan_tambah['Nama']} di database? (Yes, No)")
                if lanjut_save.lower() == "yes":
                    database_v4[id_tambah] = inputan_tambah
                    print(f"Data {inputan_tambah["Nama"]} berhasil disimpan di database")
                    break
                elif lanjut_save.lower() == "no":
                    break
                else:
                    print("Inputan anda tidak dikenal")

        elif pilihan_add == 2: #Opsi 2.Kembali ke Menu Utama
            break

#Fungsi C-EDIT data
def ubah_data ():
    while True:
        print("\nUbah Data Section\n--")
        print("1. Ubah data")
        print("2. Kembali ke Menu Utama")

        pilihan_ubah = int(input("Pilih action (1-2): "))
        if pilihan_ubah == 1: #Opsi 1.Edit Data
            id_ubah = input("\nID data yang akan diubah: ")
            
            if id_ubah in database_v4.keys():
                for x,y in database_v4[id_ubah].items():
                    print(f"{x} : {y}")
                while True:
                    lanjut_ubah = input(f"\nApakah ingin melanjutkan untuk mengubah data tersebut? (Yes, No): ")
                    if lanjut_ubah.lower() == "yes":
                        while True:
                            kolom_ubah = input("Input kolom yang hendak diubah: ")
                            if kolom_ubah.capitalize() in database_v4[id_ubah]:
                                break
                            else:
                                print("Kolom yang anda maksud tidak ditemukan, ulangi kembali")
                        isi_ubah = input("Input informasi baru pada kolom tersebut: ")
                        database_v4[id_ubah][kolom_ubah.capitalize()] = isi_ubah.capitalize()
                        print(f"\nBerikut data {id_ubah} yang berhasil diperbaharui")
                        for x,y in database_v4[id_ubah].items():
                            print(f"{x} : {y}")
                        break
                    elif lanjut_ubah.lower() == "no":
                        break
            else:
                print("Data yang anda cari tidak ditemukan")

        elif pilihan_ubah == 2: #Opsi 2.Kembali ke Menu Utama
            break

#Fungsi D-DELETE data
def hapus_data():
    while True:
        print("\nHapus Data Section\n--")
        print("1. Hapus data")
        print("2. Kembali ke Menu Utama")

        pilihan_hapus = int(input("Pilih action (1-2): "))
        if pilihan_hapus == 1: #Opsi 1.Hapus Data
            id_hapus = input("\nID data yang akan dihapus: ")
            if id_hapus in database_v4.keys():
                for x,y in database_v4[id_hapus].items():
                    print(f"{x} : {y}")
                while True:
                    lanjut_hapus = input(f"\nApakah ingin melanjutkan untuk menghapus data tersebut? (Yes, No): ")
                    if lanjut_hapus.lower() == "yes":
                        del database_v4[id_hapus]
                        print(f"\nData {id_hapus} berhasil dihapus dari database")
                        break
                    elif lanjut_hapus.lower() == "no":
                        break
            else:
                print("Data yang anda cari tidak ditemukan")

        elif pilihan_hapus == 2: #Opsi 2.Kembali ke Menu Utama
            break

#Fungsi X-ANALYZE data
def analisis_data():
    while True:
        print("\nAnalisis data Section\n--")
        print("1. Rekomendasi tempat berdasarkan budget")
        print("2. Rekomendasi tempat berdasarkan isu kesehatan")
        print("3. Rekomendasi tempat berdasarkan reputasi")
        print("4. Kembali ke Menu Utama")

        pilihan_analisis = int(input("Pilih action (1-4): "))
        if pilihan_analisis == 1: #Opsi 1.Rekomendasi by budget
            budget_user = int(input("Budget yang biasa anda habiskan untuk makan: "))
            print("\nBerikut rekomendasi untuk anda: \n")
            for x in database_v4:
                price_range = database_v4[x]["Price"]
                if budget_user >= price_range.start:
                    for y,z in database_v4[x].items():
                        print (f"{y} : {z}")

        elif pilihan_analisis == 2: #Opsi 2.Rekomendasi kesehatan
            print("\nBerikut rekomendasi untuk anda: \n")
            for x in database_v4:
                if database_v4[x]["Review_google"] >= 4 and database_v4[x]["Repeat_order"] >= 50:
                    for y,z in database_v4[x].items():
                        print (f"{y} : {z}")

        elif pilihan_analisis == 3: #Opsi 3.Rekomendasi reputasi
            print("\nBerikut rekomendasi untuk anda: \n")
            for x in database_v4:
                if database_v4[x]["Porsi_sayur"] >= 20 and database_v4[x]["Menu_kolesterol"] <= 25:
                    for y,z in database_v4[x].items():
                        print (f"{y} : {z}")

        elif pilihan_analisis == 4: #Opsi 4.Kembali ke Menu Utama
            break

#Fungsi tampilan MENU UTAMA
def menu_utama():
    print("\nMenu Utama\n--------")
    print("1. Lihat Data")
    print("2. Tambahkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Analisis Data")
    print("6. Selesai dan tutup aplikasi")

#Fungsi Flow MENU UTAMA
while True:
    menu_utama ()
    pilihan_awal = int(input("\nPilih action (1-5) : "))
    if pilihan_awal == 1:
        lihat_data() #Opsi A-READ data

    elif pilihan_awal == 2:
        tambah_data () #Opsi B-ADD data

    elif pilihan_awal == 3:
        ubah_data () #Opsi C-EDIT data

    elif pilihan_awal == 4:
        hapus_data () #Opsi D-DELETE data

    elif pilihan_awal == 5:
        analisis_data () #Opsi X-ANALYZE data

    elif pilihan_awal == 6:
        print ("Terima kasih!")                                                  
        print("\"Lidah bagoyang, Hiduik panjang, Hati pun sanang\"")
        break

    else:  
        print("\nMohon maaf! Opsi yang anda pilih tidak tersedia.")