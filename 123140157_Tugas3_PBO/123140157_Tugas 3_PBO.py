class KipasAngin:
    def __init__(self, merk, warna):
        self.merk= merk
        self.warna = warna
        self.kecepatan = 0
        self.daya = 50

    def menambah_kecepatan (self, tambahan):
        if tambahan > 0:
            self.kecepatan += tambahan
            print(f"Kecepatan kipas {self.merk} bertambah menjadi {self.kecepatan}")
        else:
            print("Kecepatan harus lebih dari 0")

    def mengurangi_kecepatan (self, kurang):
        if kurang > 0 and self.kecepatan - kurang >= 0:
            self.kecepatan -= kurang
            print(f"Kecepatan kipas {self.merk} berkurang menjadi {self.kecepatan}")
        elif self.kecepatan - kurang < 0:
            self.kecepatan = 0
            print(f"Kipas {self.merk} berhenti")
        else:
            print("Kecepatan harus lebih dari 0")

    def info(self):
        print(f"Kipas {self.merk} warna {self.warna}, kecepatan {self.kecepatan}, dengan daya {self.daya} watt")

kipas1 = KipasAngin("Miyako", "Hitam")
kipas2 = KipasAngin("Cosmos", "Putih")
kipas1.menambah_kecepatan(3)
kipas1.mengurangi_kecepatan(1)
kipas1.info()
print("\n")
kipas2.menambah_kecepatan(2)
kipas2.mengurangi_kecepatan(5)
kipas2.info()