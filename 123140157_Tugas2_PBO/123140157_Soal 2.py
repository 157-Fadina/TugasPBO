transaksi = []

def tambah_transaksi (tanggal, kategori_transaksi, nominal_dimasukkan_dikeluarkan):
    transaksi.append([tanggal, kategori_transaksi, nominal_dimasukkan_dikeluarkan])

tambah_transaksi("01-10-2023", "Pemasukan", 300000)
tambah_transaksi("02-10-2023", "Pengeluaran", 150000)
tambah_transaksi("03-10-2023", "Pemasukan", 500000)

def hitung_total ():
    total_pemasukan = 0  
    total_pengeluaran = 0

    for i in transaksi:
        if i[1] == "Pemasukan":
            total_pemasukan += i[2]
        elif i[1] == "Pengeluaran":
            total_pengeluaran += i[2]
    
    print(f"Total pemasukan: {total_pemasukan}")
    print(f"Total pengeluaran: {total_pengeluaran} \n")

hitung_total()

def ambil_nominal(i):
    return i[2]

def tampilkan_transaksi_terbesar_terkecil():
    transaksi_terbesar = max(transaksi, key=ambil_nominal)
    transaksi_terkecil = min(transaksi, key=ambil_nominal) 
 
    print("Transaksi terbesar:")
    print(f"Tanggal: {transaksi_terbesar[0]}, kategori: {transaksi_terbesar[1]}, jumlah: {transaksi_terbesar[2]} \n")

    print("Transaksi terkecil:")
    print(f"Tanggal: {transaksi_terkecil[0]}, kategori: {transaksi_terkecil[1]}, jumlah: {transaksi_terkecil[2]} \n")

tampilkan_transaksi_terbesar_terkecil()

def urutkan_transaksi():
    transaksi.sort(key=ambil_nominal, reverse = True)
    print("Transaksi terurut: ")
    for no, i in enumerate(transaksi, start=1):
        print(f"{no}. {i[0]}, {i[1]}, {i[2]}")
urutkan_transaksi()