ulangin="y"
while ulangin=="y":
    print("""
--------------------------------------------------------------
               SELAMAT DATANG DI OBYEK WISATA ALAM
                            TANGKEBAN
                 NYALEMBANG-PULOSARI-PEMALANG
--------------------------------------------------------------
Silahkan Masukkan User dan Password
User admin
Pass admin
    """)
    user=input("Masukkan Username :")
    password=input("Masukkan Password :")
    if user=="admin" and password=="admin":
        ngulang="y"
        while ngulang=="y":
            print("""
------------------------------------------------------------
               SELAMAT DATANG DI OBYEK WISATA ALAM
                            TANGKEBAN
                 NYALEMBANG-PULOSARI-PEMALANG
------------------------------------------------------------
Silahkan Pilih Pembelian Tiket

a. Tiket Masuk Tangkeban Park
b. Taman Langit
c. Camping Ground
d. Log Out
----------------------------------------------------
            """)
            pilihtiket = input("Silahkan Pilih Pembelian Tiket Dengan Memasukkan Abjad Dari List Di Atas :")

# START FUNGSI A
            if pilihtiket == "a" or pilihtiket == "A":
                ulangtiketbukit = "y"
                while ulangtiketbukit == "y":
                    print("""
------------------------------------
TIKET MASUK TANGKEBAN PARK
------------------------------------
a. Tiket Orang Masuk                  Rp 25000
b. Tiket Kendaraan Motor              Rp 5000
c. Tiket Kendaraan Mobil              Rp 10000
d. Informasi Detail Ketentuan Tiket
e. Kembali ke menu awal
------------------------------------
*Beli Tiket Orang Masuk
Rp 24.000 dengan minimal pembelian 4

*Beli Tiket Kendaraan Motor dan 
Mobil Potongan Harga Rp 1000 Dengan
Minimal Pembelian 2 
------------------------------------                    
                    """)
                    pilihan = input("Silahkan Pilih Tiket Dengan Memasukkan Abjad Dari List Diatas :")

# START TIKET ORANG MASUK
                    if pilihan == "a" or pilihan == "A":
                        stop = "y"
                        while stop == "y":
                            from datetime import datetime

                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            jumlahorang = int(input("Jumlah Orang :"))
                            if jumlahorang > 4:
                                print("Jumlah Maksimal Untuk Satu Tiket 4 Orang")
                                break
                            hargatiketorang = 25000
                            if jumlahorang == 4:
                                hargatiketorang = 24000
                            totalharga = hargatiketorang * jumlahorang
                            print("Total Yang Harus Dibayar : Rp", totalharga)
                            jumlahbayar = int(input("Uang Yang Diterima :"))
                            nama = []
                            umur = []
                            for i in range(jumlahorang):
                                print("\nData ke-", i + 1)
                                nama_pengunjung = input("Masukkan Nama :")
                                nama.append(nama_pengunjung)
                                umur_pengunjung = int(input("Masukkan Umur :"))
                                umur.append(umur_pengunjung)
                            for i in range(jumlahorang):
                                if umur[i] <= 9:
                                    pendamping = input("Masukkan Nama Pendamping :")
                                    kontak = input("Masukkan Nomor Telepon Pendamping :")
                                    break
                                else:
                                    pendamping = "-"
                                    kontak = "-"
                            for i in range(jumlahorang):
                                print("----------------------------------------------")
                                print("Tiket Orang Masuk")
                                print("----------------------------------------------")
                                print("{}/{}/{}".format(hari, bulan, tahun))
                                print("Pendamping :", pendamping)
                                print("Kontak :", kontak)
                                for cetaknama in nama:
                                    print("Nama : {}".format(cetaknama))
                                for cetakumur in umur:
                                    print("Umur : {}".format(cetakumur))
                                print("----------------------------------------------")
                                print("Harga : Rp", hargatiketorang)
                                print("Total Harga : Rp", totalharga)
                                print("Kembali : Rp", jumlahbayar - totalharga)
                                print("----------------------------------------------")
                                print("Terimakasih")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali :")
                            break
# END TIKET ORANG MASUK

# START TIKET MOTOR
                    elif pilihan == "b" or pilihan == "B":
                        pas = "y"
                        while pas == "y":
                            from datetime import datetime

                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            import datetime

                            x = datetime.datetime.now()
                            waktu = (x.strftime("%H:%M:%p"))
                            jumlahmotor = int(input("Masukkan Jumlah Kendaraan Motor :"))
                            if jumlahmotor >= 3:
                                print("Jumlah Maksimal Untuk Satu Tiket 2 Kendaraan Motor")
                                break
                            hargatiketmotor = 5000
                            if jumlahmotor == 2:
                                hargatiketmotor = 4000
                            totalparkirmotor = hargatiketmotor * jumlahmotor
                            print("Total Yang Harus Di Bayar : Rp", totalparkirmotor)
                            bayarparkirmotor = int(input("Uang Yang Diterima :"))
                            listplatmotor = []
                            merkmotor = []
                            for i in range(jumlahmotor):
                                print("\nData ke-", i + 1)
                                platmotor = input("Masukkan Plat Nomor Motor :")
                                listplatmotor.append(platmotor)
                                merk = input("Masukkan Merk Motor :")
                                merkmotor.append(merk)
                            for i in range(jumlahmotor):
                                print("----------------------------------------------")
                                print("Tiket Motor Masuk Bukit Tangkeban")
                                print("----------------------------------------------")
                                print("{}/{}/{}".format(hari, bulan, tahun))
                                print(waktu)
                                for noplat in listplatmotor:
                                    print("Nomor Kendaraan {}".format(noplat))
                                for merk_motor in merkmotor:
                                    print("Merk Motor {}".format(merk_motor))
                                print("----------------------------------------------")
                                print("Harga : Rp", hargatiketmotor)
                                print("Total harga : Rp", totalparkirmotor)
                                print("Kembalian : Rp", bayarparkirmotor - totalparkirmotor)
                                print("----------------------------------------------")
                                print("Terimakasih")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali :")
                            break
# END TIKET MOTOR

# START TIKET MOBIL
                    elif pilihan == "c" or pilihan == "C":
                        cus = "y"
                        while cus == "y":
                            from datetime import datetime

                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            import datetime

                            x = datetime.datetime.now()
                            waktu = (x.strftime("%H:%M:%p"))
                            jumlahmobil = int(input("Masukkan Jumlah Kendaraan Mobil :"))
                            if jumlahmobil >= 3:
                                print("Jumlah Maksimal Untuk Satu Tiket 2 Kendaraan Mobil")
                                break
                            hargatiketmobil = 10000
                            if jumlahmobil == 2:
                                hargatiketmobil = 9000
                            totalparkirmobil = hargatiketmobil * jumlahmobil
                            print("Total Yang Harus Di Bayar : Rp", totalparkirmobil)
                            bayarparkirmobil = int(input("Uang Yang Diterima :"))
                            listplatmobil = []
                            listmerkmobil = []
                            for i in range(jumlahmobil):
                                print("\nData ke-", i + 1)
                                platmobil = input("Masukkan Plat Nomor Mobil :")
                                listplatmobil.append(platmobil)
                                merkmobil = input("Masukkan Merk Mobil :")
                                listmerkmobil.append(merkmobil)
                            for i in range(jumlahmobil):
                                print("----------------------------------------------")
                                print("Tiket Mobil Masuk Bukit Tangkeban")
                                print("----------------------------------------------")
                                print("{}/{}/{}".format(hari, bulan, tahun))
                                print(waktu)
                                for nomobil in listplatmobil:
                                    print("Nomor Kendaraan {}".format(nomobil))
                                for merk_mobil in listmerkmobil:
                                    print("Merk Mobil {}".format(merk_mobil))
                                print("----------------------------------------------")
                                print("Harga : Rp", hargatiketmobil)
                                print("Total harga : Rp", totalparkirmobil)
                                print("Kembalian : Rp", bayarparkirmobil - totalparkirmobil)
                                print("----------------------------------------------")
                                print("Terimakasih")
                                print("----------------------------------------------")
                            ulangtiketbukit = input("Masukkan y untuk kembali :")
                            break
# END TIKET MOBIL

# START DETAIL
                    elif pilihan == "d" or pilihan == "D":
                        print("""
a.  Tiket Orang Masuk Tangkeban Park
    1.  Berlaku untuk 1 (satu) kali masuk
        ke Tangkeban Park, tidak berlaku 
        untuk tempat lainya
    2.  Tiket berlaku Individu 
        (Orang), tidak berlaku untuk kendaraan
    3.  Pengunjung usia di bawah 9 tahun 
        diperbolehkan masuk dengan pendamping
    4.  Tiket hanya berlaku pada tanggal kunjungan yang 
        sudah dipilih dan pada pukul 06.00 – 21.00 WIB
    5.  Tiket yang sudah dibeli tidak dapat dikembalikan 
        (non-refundable)
    6.  Semua pengunjung wajib melaksanakan segala 
        ketentuan yang diatur terkait penerapan pembatasan 
        sosial dan mekanisme pembelian tiket, pihak bukit tangkeban 
        berhak untuk menolak dan/atau mengeluarkan setiap 
        pengunjung yang datang apabila tidak mengikuti 
        ketentuan yang sudah diatur

b.  Tiket Masuk Kendaraan Motor
    1.  Berlaku untuk 1 (satu) kali masuk
    2.  Tiket berlaku untuk kendaraan motor, tidak
        berlaku untuk individu (orang) atau kendaraan mobil
    3.  Tiket berlaku pada tanggal kunjungan yang sudah 
        dipilih dan pada pukul 06.00 – 21.00 WIB
    4.  Tiket yang sudah dibeli tidak dapat dikembalikan 
        (non-refundable)

c.  Tiket Masuk Kendaraan Mobil
    1.  Berlaku untuk 1 (satu) kali masuk
    2.  Tiket berlaku untuk kendaraan mobil, tidak
        berlaku untuk individu (orang) atau kendaraan motor
    3.  Tiket berlaku pada tanggal kunjungan yang sudah 
        dipilih dan pada pukul 06.00 – 21.00 WIB
    4.  Tiket yang sudah dibeli tidak dapat dikembalikan 
        (non-refundable)
                        """)
                        ulangtiketbukit = input("Masukkan anda ingin kembali ke awal y/n :")
# END DETAIL

#KEMBALI
                    elif pilihan=="e" or pilihan=="E":
                        ngulang="y"
                        break
#END KEMBALI

                    else:
                        ulangtiketbukit = input("Pilihan tidak ada apakah anda ingin mengulangi y/n :")
# END FUNGSI A

# START FUNGSI B TAMAN LANGIT
            elif pilihtiket == "b" or pilihtiket == "B":
                ulangtikettaman = "y"
                while ulangtikettaman == "y":
                    import time
                    hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu")
                    sekarang = time.time()
                    infowaktu = time.localtime(sekarang)
                    info_hari = hari[infowaktu[6]]
#KONDISI PERTAMA TAMAN LANGIT WEEKDAY
                    if info_hari == hari[1] or info_hari == hari[2] or info_hari == hari[3] or info_hari == hari[
                        4] or info_hari == hari[5]:
                        print("""
------------------------------------
TIKET MASUK TAMAN LANGIT
------------------------------------
Weekday                 Rp 30.000
*Pembelian Tiket Standard Untuk Satu 
Atau Dua Orang 
------------------------------------
Triple Fun Weekday      Rp 100.000
*Di Minimal Pembelian 3 tiket
------------------------------------
                        """)
                        lanjut=input("Masukkan L untuk lanjut K untuk kembali ke menu awal :")
                        if lanjut=="l" or lanjut=="L":
                            stoptaman = "y"
                            while stoptaman == "y":
                                from datetime import datetime
                                current = datetime.now()
                                tahun = current.year
                                bulan = current.month
                                hari = current.day
                                jumlahorang = int(input("Jumlah orang :"))
                                if jumlahorang > 3:
                                    print("Jumlah maksimal pesan 3 orang")
                                    break
                                hargatikettaman = 30000
                                if jumlahorang == 3:
                                    hargatikettaman = 33000
                                totalharga = hargatikettaman * jumlahorang
                                print("Total Yang Harus Dibayar : Rp", totalharga)
                                jumlahbayar = int(input("Uang Yang Diterima :"))
                                nama = []
                                umur = []
                                for i in range(jumlahorang):
                                    print("\nData ke-", i + 1)
                                    nama_pengunjung = input("Masukkan Nama :")
                                    nama.append(nama_pengunjung)
                                    umur_pengunjung = int(input("Masukkan Umur :"))
                                    umur.append(umur_pengunjung)
                                for i in range(jumlahorang):
                                    if umur[i] <= 9:
                                        pendamping = input("Masukkan Nama Pendamping :")
                                        kontak = input("Masukkan Nomor Telepon Pendamping :")
                                        break
                                    else:
                                        pendamping = "-"
                                        kontak = "-"
                                for i in range(jumlahorang):
                                    print("----------------------------------------------")
                                    print("Tiket Masuk Taman Langit")
                                    print("Weekday")
                                    print("----------------------------------------------")
                                    print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                    print("Pendamping :", pendamping)
                                    print("Kontak :", kontak)
                                    for cetaknama in nama:
                                        print("Nama : {}".format(cetaknama))
                                    for cetakumur in umur:
                                        print("Umur : {}".format(cetakumur))
                                    print("----------------------------------------------")
                                    print("Harga : Rp", hargatikettaman)
                                    print("Total Harga : Rp", totalharga)
                                    print("Kembali : Rp", jumlahbayar - totalharga)
                                    print("----------------------------------------------")
                                    print("Terimakasih")
                                    print("----------------------------------------------")
                                ulangtikettaman = input("Masukkan y untuk kembali :")
                                break
                        elif lanjut=="k" or lanjut=="K":
                           ngulang="y"
                           break
                        else:
                            print("Inputan Salah")
                            ulangtikettaman="y"
#END KONDISI PERTAMA TAMAN LANGIT WEEKDAY

#KONDISI KEDUA TAMAN LANGIT WEEKEND
                    elif info_hari==hari[0] or info_hari==hari[6]:
                        print("""
------------------------------------
TIKET MASUK TAMAN LANGIT
------------------------------------
Weekend Taman Langit   Rp 50.000
*Pembelian tiket standard untuk satu 
atau dua orang 
------------------------------------
Triple Fun Weekend      Rp 135.000
*Di minimal pembelian 3 tiket
------------------------------------
                        """)
                        lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal :")
                        if lanjut == "l" or lanjut == "L":
                            stoptaman = "y"
                            while stoptaman == "y":
                                from datetime import datetime

                                current = datetime.now()
                                tahun = current.year
                                bulan = current.month
                                hari = current.day
                                jumlahorang = int(input("Jumlah orang :"))
                                if jumlahorang > 3:
                                    print("Jumlah maksimal pesan 3 orang")
                                    break
                                hargatikettaman = 50000
                                if jumlahorang == 3:
                                    hargatikettaman = 135000
                                totalharga = hargatikettaman * jumlahorang
                                print("Total Yang Harus Dibayar : Rp", totalharga)
                                jumlahbayar = int(input("Uang Yang Diterima :"))
                                nama = []
                                umur = []
                                for i in range(jumlahorang):
                                    print("\nData ke-", i + 1)
                                    nama_pengunjung = input("Masukkan Nama :")
                                    nama.append(nama_pengunjung)
                                    umur_pengunjung = int(input("Masukkan Umur :"))
                                    umur.append(umur_pengunjung)
                                for i in range(jumlahorang):
                                    if umur[i] <= 9:
                                        pendamping = input("Masukkan Nama Pendamping :")
                                        kontak = input("Masukkan Kontak Pendamping :")
                                        break
                                    else:
                                        pendamping = "-"
                                        kontak = "-"
                                for i in range(jumlahorang):
                                    print("----------------------------------------------")
                                    print("Tiket Masuk Taman Langit")
                                    print("Weekend")
                                    print("----------------------------------------------")
                                    print(info_hari,"{}/{}/{}".format(hari, bulan, tahun))
                                    print("Pendamping :", pendamping)
                                    print("Kontak :", kontak)
                                    for cetaknama in nama:
                                        print("Nama : {}".format(cetaknama))
                                    for cetakumur in umur:
                                        print("Umur : {}".format(cetakumur))
                                    print("----------------------------------------------")
                                    print("Harga : Rp", hargatikettaman)
                                    print("Total Harga : Rp", totalharga)
                                    print("Kembali : Rp", jumlahbayar - totalharga)
                                    print("----------------------------------------------")
                                    print("Terimakasih")
                                    print("----------------------------------------------")
                                ulangtikettaman = input("Masukkan Y Untuk Kembali :")
                                break
                        elif lanjut=="k" or lanjut=="K":
                           ngulang="y"
                           break
                        else:
                            print("Inputan Salah")
                            ulangtikettaman="y"
# END KONDISI KEDUA WEEKEND
# END KONDISI B TAMAN LANGIT

#START CAMPING GROUND
            elif pilihtiket=="c" or pilihtiket=="C":
                stopcamping="y"
                while stopcamping=="y":
                    print("""
-------------------------------------------------------------------------
TIKET MASUK CAMPING GROUND
-------------------------------------------------------------------------
                                            Harga Weekday   Harga Weekend
a. Tiket Camping                            Rp 20.000      Rp 50.000  
b. Sewa Tenda                               Rp 75.000      Rp 150.000
c. Kembali ke menu awal
-------------------------------------------------------------------------
*
Weekday (Hari Senin-Jumat)
Weekend (Hari Sabtu-Minggu)
-------------------------------------------------------
                    """)
                    pilihtiketcamping=input("Silahkan Pilih Tiket Camping Dengan Memasukkan Abjad Dari List Diatas :")
#START KONDISI A
                    if pilihtiketcamping=="a" or pilihtiketcamping=="A":
                        ulangweekdaycamping = "y"
                        while ulangweekdaycamping == "y":
                            import time
                            hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
                            sekarang = time.time()
                            infowaktu = time.localtime(sekarang)
                            camping_hari = hari[infowaktu[6]]

#START KONDISI PERTAMA WEEKDAY CAMPING WEEKDAY
                            if camping_hari==hari[1] or camping_hari==hari[2] or camping_hari==hari[3] or camping_hari==hari[4] or camping_hari==hari[5]:
                                print("""
-------------------------------------
TIKET MASUK CAMPING GROUND
Weekday
-------------------------------------
Weekday Camping Ground   Rp 20.000
*Pembelian tiket standard untuk satu 
atau dua orang 
-------------------------------------
                                    """)
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal :")
                                if lanjut == "l" or lanjut == "L":
                                    stopcamping = "y"
                                    while stopcamping == "y":
                                        from datetime import datetime
                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("Jumlah orang :"))
                                        if jumlahorang > 3:
                                            print("Jumlah maksimal pesan 3 orang")
                                            break
                                        hargatiketcamping = 60000
                                        totalharga = hargatiketcamping * jumlahorang
                                        print("Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input("Uang Yang Diterima :"))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan Nama :")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan Umur :"))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            if umur[i] <= 9:
                                                pendamping = input("Masukkan Nama Pendamping :")
                                                kontak = input("Masukkan Kontak Pendamping :")
                                                break
                                            else:
                                                pendamping = "-"
                                                kontak = "-"
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("Tiket Masuk Camping Ground")
                                            print("Weekday")
                                            print("----------------------------------------------")
                                            print(camping_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print("Pendamping :", pendamping)
                                            print("Pontak :", kontak)
                                            for cetaknama in nama:
                                                print("Nama : {}".format(cetaknama))
                                            for cetakumur in umur:
                                                print("Umur : {}".format(cetakumur))
                                            print("----------------------------------------------")
                                            print("Harga : Rp", hargatiketcamping)
                                            print("Total Harga : Rp", totalharga)
                                            print("Kembali : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("Terimakasih")
                                            print("----------------------------------------------")
                                        ulangweekdaycamping= input("Masukkan y untuk kembali :")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopcamping = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaycamping = "y"
#END KONDISI KEDUA WEEKDAY CAMPING

#START KONDISI WEEKEND CAMPING
                            elif camping_hari==hari[0] or camping_hari==hari[6]:
                                print("""
---------------------------------------
TIKET MASUK CAMPING GROUND
Weekend
---------------------------------------
Weekend Camping Ground   Rp 50.000
*Pembelian tiket standard untuk satu 
atau dua orang 
---------------------------------------
                                """)
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal :")
                                if lanjut == "l" or lanjut == "L":
                                    stop_camping = "y"
                                    while stop_camping == "y":
                                        from datetime import datetime

                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("Jumlah orang :"))
                                        if jumlahorang > 3:
                                            print("Jumlah maksimal pesan 3 orang")
                                            break
                                        hargatiketcamping = 50000
                                        totalharga = hargatiketcamping * jumlahorang
                                        print("Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input("Uang yang diterima :"))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama :")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur :"))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            if umur[i] <= 9:
                                                pendamping = input("Masukkan nama pendamping :")
                                                kontak = input("Masukkan kontak pendamping :")
                                                break
                                            else:
                                                pendamping = "-"
                                                kontak = "-"
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("Tiket Masuk Camping Ground")
                                            print("Weekend")
                                            print("----------------------------------------------")
                                            print(camping_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print("pendamping :", pendamping)
                                            print("kontak :", kontak)
                                            for cetaknama in nama:
                                                print("nama : {}".format(cetaknama))
                                            for cetakumur in umur:
                                                print("umur : {}".format(cetakumur))
                                            print("----------------------------------------------")
                                            print("Harga : Rp", hargatiketcamping)
                                            print("Total Harga : Rp", totalharga)
                                            print("Kembali : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("Terimakasih")
                                            print("----------------------------------------------")
                                        ulangtiketcamping = input("Masukkan y untuk kembali :")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopcamping = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekendcamping= "y"
#END KONDISI KEDUA WEEKEND CAMPING GROUND
#END KONDISI A

#START KONDISI B
                    elif pilihtiketcamping=="b" or pilihtiketcamping=="B":
                        ulangweekendcamping = "y"
                        while ulangweekendcamping == "y":
                            import time

                            hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
                            sekarang = time.time()
                            infowaktu = time.localtime(sekarang)
                            sewa_hari = hari[infowaktu[6]]

# START KONDISI PERTAMA WEEKDAY Sewa Tenda
                            if sewa_hari == hari[1] or sewa_hari == hari[2] or sewa_hari == hari[3] or sewa_hari == hari[
                                4] or sewa_hari == hari[5]:
                                print("""
----------------------------------------------------
TIKET SEWA TENDA
Weekday
----------------------------------------------------
Weekday Sewa Tenda   Rp 75.000
----------------------------------------------------
                                """)
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal :")
                                if lanjut == "l" or lanjut == "L":
                                    stopsewa = "y"
                                    while stopsewa == "y":
                                        from datetime import datetime

                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("Jumlah orang :"))
                                        if jumlahorang > 3:
                                            print("Jumlah maksimal pesan 3 orang")
                                            break
                                        hargatiketsewa = 75000
                                        totalharga = hargatiketsewa * jumlahorang
                                        print("Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input("Uang yang diterima :"))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama :")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur :"))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            if umur[i] <= 9:
                                                pendamping = input("Masukkan nama pendamping :")
                                                kontak = input("Masukkan kontak pendamping :")
                                                break
                                            else:
                                                pendamping = "-"
                                                kontak = "-"
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("TIKET SEWA TENDA")
                                            print("Weekday")
                                            print("----------------------------------------------")
                                            print(sewa_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print("pendamping :", pendamping)
                                            print("kontak :", kontak)
                                            for cetaknama in nama:
                                                print("nama : {}".format(cetaknama))
                                            for cetakumur in umur:
                                                print("umur : {}".format(cetakumur))
                                            print("----------------------------------------------")
                                            print("Harga : Rp", hargatiketsewa)
                                            print("Total Harga : Rp", totalharga)
                                            print("Kembali : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("Terimakasih")
                                            print("----------------------------------------------")
                                        ulangweekdaysewa = input("Masukkan y untuk kembali :")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopsewa = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaysewa = "y"
# END KONDISI KEDUA WEEKDAY SEWA TENDA

# START KONDISI WEEKEND SEWA
                            elif sewa_hari == hari[0] or sewa_hari == hari[6]:
                                print("""
----------------------------------------------------
TIKET SEWA TENDA 
Weekend
----------------------------------------------------
Weekend Sewa Tenda   Rp 150.000
----------------------------------------------------
                                """)
                                lanjut = input("masukkan l untuk lanjut k untuk kembali ke menu awal :")
                                if lanjut == "l" or lanjut == "L":
                                    stopsewa = "y"
                                    while stopsewa == "y":
                                        from datetime import datetime

                                        current = datetime.now()
                                        tahun = current.year
                                        bulan = current.month
                                        hari = current.day
                                        jumlahorang = int(input("Jumlah orang :"))
                                        if jumlahorang > 3:
                                            print("Jumlah maksimal pesan 3 orang")
                                            break
                                        hargatiketsewa = 125000
                                        totalharga = hargatiketsewa * jumlahorang
                                        print("Total yang harus dibayar : Rp", totalharga)
                                        jumlahbayar = int(input("Uang yang diterima :"))
                                        nama = []
                                        umur = []
                                        for i in range(jumlahorang):
                                            print("\nData ke-", i + 1)
                                            nama_pengunjung = input("Masukkan nama :")
                                            nama.append(nama_pengunjung)
                                            umur_pengunjung = int(input("Masukkan umur :"))
                                            umur.append(umur_pengunjung)
                                        for i in range(jumlahorang):
                                            if umur[i] <= 9:
                                                pendamping = input("Masukkan nama pendamping :")
                                                kontak = input("Masukkan kontak pendamping :")
                                                break
                                            else:
                                                pendamping = "-"
                                                kontak = "-"
                                        for i in range(jumlahorang):
                                            print("----------------------------------------------")
                                            print("TIKET SEWA TENDA")
                                            print("Weekday")
                                            print("----------------------------------------------")
                                            print(sewa_hari, "{}/{}/{}".format(hari, bulan, tahun))
                                            print("pendamping :", pendamping)
                                            print("kontak :", kontak)
                                            for cetaknama in nama:
                                                print("nama : {}".format(cetaknama))
                                            for cetakumur in umur:
                                                print("umur : {}".format(cetakumur))
                                            print("----------------------------------------------")
                                            print("Harga : Rp", hargatiketsewa)
                                            print("Total Harga : Rp", totalharga)
                                            print("Kembali : Rp", jumlahbayar - totalharga)
                                            print("----------------------------------------------")
                                            print("Terimakasih")
                                            print("----------------------------------------------")
                                        ulangtiketsewa = input("Masukkan y untuk kembali :")
                                        break
                                elif lanjut == "k" or lanjut == "K":
                                    stopsewa = "y"
                                    break
                                else:
                                    print("inputan salah")
                                    ulangweekdaysewa = "y"
# END KONDISI KEDUA WEEKEND Sewa Tenda
#END KONDISI B

#KEMBALI KE MENU AWAL
                    elif pilihtiketcamping=="c" or pilihtiketcamping=="C":
                        ngulang="y"
                        break
#END KEMBALI KE MENU AWAL
                    else:
                        stopsewa=input("Pilihan tidak ada apakah anda ingin mengulangi y/n :")
#LOGOUT
            elif pilihtiket =="d" or pilihtiket=="D":
                ulangin="y"
                break
            else:
                ngulang=input("Pilihan tidak ada apakah anda ingin mengulangi y/n :")
    else:
        print("User dan password salah")
        ulangin=input("Apakah anda ingin login kembali y/n :")
