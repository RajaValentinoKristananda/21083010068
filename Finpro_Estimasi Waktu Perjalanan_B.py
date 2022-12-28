from datetime import datetime

print("+"+"~"*45+"+",
      "\n|"+" "*5, "PROGRAM ESTIMASI WAKTU PERJALANAN", " "*5+"|",
      "\n|"+" "*6, "By : Raja Valentino Kristananda", " "*6+"|",
      "\n+"+"~"*45+"+",)

now = datetime.now()
loop = True
while(loop):
    print("\n+"+"~"*45+"+",
          "\n|"+" "*19, "Menu", " "*20+"|",
          "\n+"+"~"*45+"+",
          "\n|", "1. Surabaya ke Jakarta", " "*20, "|",
          '\n|', '2. Surabaya ke Yogyakarta', " "*17, "|",
          '\n|', '3. Bandung  ke Surabaya', " "*19, "|",
          '\n|', '4. Bandung  ke Yogyakarta', " "*17, "|",
          '\n|', '5. Custom', " "*33, "|",
          '\n|', '6. Exit', " "*35, "|",
          "\n|" + " " * 45 + "|",
          '\n|'+" "*17, now, "|",
          "\n+" + "~" * 45 + "+")
    pilihan = str(input("Masukan Pilihan [1-6] : "))

    if pilihan == '1':
        print("\n+"+"~"*45+"+",
              "\n|"+" "*9, "Kendaraan Yang Digunakan", " "*10+"|",
              "\n+"+"_"*45+"+",
              '\n|', '1. Via Mobil (Tol)', " "*25+"|",
              '\n|', '2. Via Sepeda Motor', " "*24+"|",
              '\n|', '3. Via Jalan Kaki', " "*26+"|",
              '\n|', '4. Custom', " "*34+"|",
              "\n+"+"~"*45+"+")
        kendaraan = str(input("Masukkan Kendaraan Yang Digunakan [1-4]: "))
        if kendaraan == '1':
            print("Jarak Surabaya ke Jakarta : 783 km (Via Tol)",
                  "\nEstimasi Waktu Perjalanan : 10 jam, 1 menit (Gmaps)")
        elif kendaraan == '2':
            print("Jarak Surabaya ke Jakarta : 798 km",
                  "\nEstimasi Waktu Perjalanan : 17 jam, 3 menit (Gmaps)")
        elif kendaraan == '3':
            print("Jarak Surabaya ke Jakarta : 741 km",
                  "\nEstimasi Waktu Perjalanan : 6 hari, 7 jam (Gmaps)")
        elif kendaraan == '4':
            min1 = int(input("Masukkan rata-rata kecepatan minimum kendaraan (Km/h) :"))
            max1 = int(input("Masukkan rata-rata kecepatan maksimum kendaraan (Km/h) :"))
            jarak = 798
            rata1 = (min1+min1)/2
            waktu1 = jarak/rata1
            print("Estimasi Waktu Surabaya ke Jakarta dengan Jarak 798 km adalah", waktu1, 'jam')

    if pilihan == "2":
        print("\n+" + "~" * 45 + "+",
              "\n|" + " " * 9, "Kendaraan Yang Digunakan", " " * 10 + "|",
              "\n+" + "_" * 45 + "+",
              '\n|', '1. Via Mobil (Tol)', " " * 25 + "|",
              '\n|', '2. Via Sepeda Motor', " " * 24 + "|",
              '\n|', '3. Via Jalan Kaki', " " * 26 + "|",
              '\n|', '4. Custom', " " * 34 + "|",
              "\n+" + "~" * 45 + "+")
        kendaraan = str(input("Masukkan Kendaraan Yang Digunakan [1-4]: "))
        if kendaraan == '1':
            print("Jarak Surabaya ke Yogyakarta : 324 km (Via Tol)",
                  "\nEstimasi Waktu Perjalanan : 4 jam, 33 menit (Gmaps)")
        elif kendaraan == '2':
            print("Jarak Surabaya ke Yogyakarta : 327 km",
                  "\nEstimasi Waktu Perjalanan : 7 jam, 29 menit (Gmaps)")
        elif kendaraan == '3':
            print("Jarak Surabaya ke Yogyakarta : 312 km",
                  "\nEstimasi Waktu Perjalanan : 2 hari, 16 jam (Gmaps)")
        elif kendaraan == '4':
            min1 = int(input("Masukkan rata-rata kecepatan minimum kendaraan (Km/h) :"))
            max1 = int(input("Masukkan rata-rata kecepatan maksimum kendaraan (Km/h) :"))
            jarak = 327
            rata1 = (min1 + min1) / 2
            waktu1 = jarak / rata1
            print("Estimasi Waktu Surabaya ke Yogyakarta dengan Jarak 327 km adalah", waktu1, 'jam')

    if pilihan == "3":
        print("\n+" + "~" * 45 + "+",
              "\n|" + " " * 9, "Kendaraan Yang Digunakan", " " * 10 + "|",
              "\n+" + "_" * 45 + "+",
              '\n|', '1. Via Mobil (Tol)', " " * 25 + "|",
              '\n|', '2. Via Sepeda Motor', " " * 24 + "|",
              '\n|', '3. Via Jalan Kaki', " " * 26 + "|",
              '\n|', '4. Custom', " " * 34 + "|",
              "\n+" + "~" * 45 + "+")
        kendaraan = str(input("Masukkan Kendaraan Yang Digunakan [1-4]: "))
        if kendaraan == '1':
            print("Jarak Bandung ke Surabaya : 778 km (Via Tol)",
                  "\nEstimasi Waktu Perjalanan : 9 jam, 36 menit (Gmaps)")
        elif kendaraan == '2':
            print("Jarak Bandung ke Surabaya : 660 km",
                  "\nEstimasi Waktu Perjalanan : 15 jam, 25 menit (Gmaps)")
        elif kendaraan == '3':
            print("Jarak Bandung ke Surabaya : 635 km",
                  "\nEstimasi Waktu Perjalanan : 5 hari, 9 jam (Gmaps)")
        elif kendaraan == '4':
            min1 = int(input("Masukkan rata-rata kecepatan minimum kendaraan (Km/h) :"))
            max1 = int(input("Masukkan rata-rata kecepatan maksimum kendaraan (Km/h) :"))
            jarak = 660
            rata1 = (min1 + min1) / 2
            waktu1 = jarak / rata1
            print("Estimasi Waktu Bandung ke Surabaya dengan Jarak 660 km adalah", waktu1, 'jam')

    if pilihan == "4":
        print("\n+" + "~" * 45 + "+",
              "\n|" + " " * 9, "Kendaraan Yang Digunakan", " " * 10 + "|",
              "\n+" + "_" * 45 + "+",
              '\n|', '1. Via Mobil (Tol)', " " * 25 + "|",
              '\n|', '2. Via Sepeda Motor', " " * 24 + "|",
              '\n|', '3. Via Jalan Kaki', " " * 26 + "|",
              '\n|', '4. Custom', " " * 34 + "|",
              "\n+" + "~" * 45 + "+")
        kendaraan = str(input("Masukkan Kendaraan Yang Digunakan [1-4]: "))
        if kendaraan == '1':
            print("Jarak Bandung ke Yogyakarta : 558 km (Via Tol)",
                  "\nEstimasi Waktu Perjalanan : 7 jam, 56 menit (Gmaps)")
        elif kendaraan == '2':
            print("Jarak Bandung ke Yogyakarta : 394 km",
                  "\nEstimasi Waktu Perjalanan : 8 jam, 58 menit (Gmaps)")
        elif kendaraan == '3':
            print("Jarak Bandung ke Yogyakarta : 372 km",
                  "\nEstimasi Waktu Perjalanan : 3 hari, 5 jam (Gmaps)")
        elif kendaraan == '4':
            min1 = int(input("Masukkan rata-rata kecepatan minimum kendaraan (Km/h) :"))
            max1 = int(input("Masukkan rata-rata kecepatan maksimum kendaraan (Km/h) :"))
            jarak = 394
            rata1 = (min1 + min1) / 2
            waktu1 = jarak / rata1
            print("Estimasi Waktu Bandung ke Yogyakarta dengan Jarak 394 km adalah", waktu1, 'jam')

    if pilihan == "5":
        dari = str(input("Masukkan Kota Keberangkatan : "))
        tujuan = str(input("Masukkan Kota Tujuan : "))
        jarak = int(input("Masukkan Jarak Perjalanan : "))
        min1 = int(input("Masukkan rata-rata kecepatan minimum kendaraan (Km/h) : "))
        max1 = int(input("Masukkan rata-rata kecepatan maksimum kendaraan (Km/h) : "))
        rata1 = (min1+max1) / 2
        waktu1 = jarak / rata1
        print("Estimasi Waktu", dari, 'ke', tujuan, 'dengan Jarak', jarak, 'km adalah', waktu1, 'jam')

    if pilihan == "6":
        print("Program Berhenti",
              "\nTerima Kasih Telah Menggunakan Program Ini :)")
        loop = False

    else:
        print("Loading...")
