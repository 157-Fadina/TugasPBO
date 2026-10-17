data_mahasiswa = ("1234567890", "John Doe", (80, 75, 85))

nim, nama, nilai = data_mahasiswa

nilai_akhir = (nilai[0] * 0.3) + (nilai[1] * 0.3) + (nilai[2] * 0.4)
status = "Lulus" if nilai_akhir >= 70 else "Tidak Lulus"

print(f"\nNIM: {nim}\nNama: {nama}\nNilai Tugas: {nilai[0]}, Nilai UTS: {nilai[1]}, Nilai UAS: {nilai[2]}\nNilai Akhir: {nilai_akhir}\nStatus: {status}")