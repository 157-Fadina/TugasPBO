while True:
    nama_makanan = input ("Nama Makanan:" )
    kalori = int(input("Jumlah Kalori: "))
    lemak = float(input("Jumlah lemak: "))
    gula = float(input("Jumlah Gula: "))

    if kalori < 500 and lemak < 10 and gula < 25:
        kategori = "Makanan termasuk Sehat"
    elif kalori > 500 or lemak > 20 or gula > 25:
        kategori = "Makanan termasuk Tidak Sehat"
    else:
        kategori = "Makanan yang dikonsumsi perlu batasan"

    print("Analisis Makanan")
    print(f"Nama Makanan: {nama_makanan}")
    print(f"Kalori: {kalori} kcal")
    print(f"Lemak: {lemak} gr")
    print(f"Gula: {gula} gr")
    print(f"Kategori: {kategori}")

    cek_lagi = input("Cek Makanan yang Lain? (Y/N): ").upper()
    if cek_lagi != "Y":
        break
print("Pengecekan Berhenti")