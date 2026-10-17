mahasiswa = {}

def tambah_data(nim, nama, nilai):
    mahasiswa[nim] = {nama: nilai}

tambah_data("1234567890", "John Doe",
{"Algoritma": [85, 90, 88], "Struktur Data": [78, 85, 80]})
tambah_data("0987654321", "Jane Doe",
{"Algoritma": [70, 75, 80], "Struktur Data": [85, 90, 95]})

def cari_nilai_akhir(nim, mata_kuliah):
    nama = list(mahasiswa[nim].keys())[0]
    nilai_akhir = round(sum(mahasiswa[nim][nama][mata_kuliah]) / len(mahasiswa[nim][nama][mata_kuliah]), 1)
    return nama, nilai_akhir

nama, nilai_akhir = cari_nilai_akhir("1234567890", "Algoritma")
print(f"Nilai akhir {nama} untuk mata kuliah Algoritma: {nilai_akhir} \n")

def tampilkan_mahasiswa_diatas_80(mata_kuliah):
    for nim, data in mahasiswa.items():
        nama = list(data.keys())[0]
        nilai_mata_kuliah = data[nama]

        if mata_kuliah in nilai_mata_kuliah:
            nilai_akhir = round(sum(nilai_mata_kuliah[mata_kuliah]) / len(nilai_mata_kuliah[mata_kuliah]), 1)
            if nilai_akhir > 80:
                print(f"Mahasiswa dengan nilai akhir di atas 80 untuk mata kuliah Algoritma: \n - {nama}: {nilai_akhir}")

tampilkan_mahasiswa_diatas_80("Algoritma")