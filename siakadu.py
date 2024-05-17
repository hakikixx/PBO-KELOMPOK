class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.mata_kuliah_diambil = []

    def daftar_mata_kuliah(self, mata_kuliah):
        print(f"{self.nama} (npm: {self.npm}) mendaftar mata kuliah {mata_kuliah.nama_mata_kuliah}")
        mata_kuliah.tambah_mahasiswa(self)
        self.mata_kuliah_diambil.append(mata_kuliah)

    def tampilkan_mata_kuliah(self):
        print(f"{self.nama} (npm: {self.npm}) mengambil mata kuliah:")
        for mk in self.mata_kuliah_diambil:
            print(f"- {mk.nama_mata_kuliah}")

class MataKuliah:
    def __init__(self, nama_mata_kuliah, kode_mata_kuliah):
        self.nama_mata_kuliah = nama_mata_kuliah
        self.kode_mata_kuliah = kode_mata_kuliah
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        print(f"Mahasiswa yang terdaftar di mata kuliah {self.nama_mata_kuliah} (Kode: {self.kode_mata_kuliah}):")
        for mhs in self.daftar_mahasiswa:
            print(f"- {mhs.nama} (npm: {mhs.npm})")

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Hakiki", "2265061001")
mahasiswa2 = Mahasiswa("Nanda", "2215061132")

# Membuat objek MataKuliah
mata_kuliah1 = MataKuliah("Pemrograman Berorientasi Objek", "IF101")
mata_kuliah2 = MataKuliah("Kecerdasan Buatan", "IF102")

# Mahasiswa mendaftar mata kuliah
mahasiswa1.daftar_mata_kuliah(mata_kuliah1)
mahasiswa1.daftar_mata_kuliah(mata_kuliah2)
mahasiswa2.daftar_mata_kuliah(mata_kuliah1)

# Tampilkan daftar mata kuliah yang diambil oleh mahasiswa
mahasiswa1.tampilkan_mata_kuliah()
print("\n")
mahasiswa2.tampilkan_mata_kuliah()
print("\n")

# Tampilkan daftar mahasiswa yang terdaftar di mata kuliah
mata_kuliah1.tampilkan_mahasiswa()
print("\n")
mata_kuliah2.tampilkan_mahasiswa()
