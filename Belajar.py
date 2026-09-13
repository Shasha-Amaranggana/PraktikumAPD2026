from abc import ABC, abstractmethod


# =========================
# CLASS USER
# =========================

class User:
    def __init__(self, username, password, saldo, email):
        self.username = username
        self._password = password
        self.__saldo = saldo
        self.__email = email
        self.library = Library()
        self.daftarTransaksi = []

    # Mengecek password
    def lihatPassword(self, password):
        return self._password == password

    # Getter saldo
    @property
    def saldo(self):
        return self.__saldo

    # Top up saldo
    def topup(self, nominal):
        if 0 < nominal <= 500000:
            self.__saldo += nominal
            print(f"Top up ente berhasil sebesar Rp{nominal}")
            return True
        elif nominal > 500000:
            print("Jumlah top up melebihi batas maksimal, uy!")
            return False
        else:
            print("Jumlah top up tidak valid, uy!")
            return False

    # Membeli ebook
    def beliEbook(self, ebook):
        if ebook in self.library.daftarEbook:
            print("Ente sudah punya E-book ini.")
            return False

        if self.__saldo >= ebook.harga:
            self.__saldo -= ebook.harga

            # Masukkan ebook ke library setelah pembayaran berhasil
            self.library.tambahEbook(ebook)

            # Buat transaksi
            transaksi = Transaksi(self, ebook, ebook.harga, "Berhasil")
            self.daftarTransaksi.append(transaksi)

            print(f"Pembelian {ebook.judul} berhasil, yey!")
            return True

        else:
            print("Saldo tidak mencukupi woy!")
            return False

    # Getter dan setter email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email_baru):
        if "@" in email_baru:
            self.__email = email_baru
        else:
            print("Email tidak valid, uy!")



# =========================
# ABSTRACT CLASS EBOOK
# =========================

class Ebook(ABC):
    def __init__(self, judul, penulis, harga, genre, tahunTerbit, kode):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.genre = genre
        self.tahunTerbit = tahunTerbit
        self.kode = kode

    @abstractmethod
    def lihatInfoEbook(self):
        pass



# =========================
# CLASS NOVEL
# =========================

class Novel(Ebook):
    def __init__(self, judul, penulis, harga, genre, tahunTerbit, kode, sinopsis):
        super().__init__(judul, penulis, harga, genre, tahunTerbit, kode)
        self.sinopsis = sinopsis

    # Overriding
    def lihatInfoEbook(self):
        print("=== NOVEL ===")
        print(f"Judul        : {self.judul}")
        print(f"Penulis      : {self.penulis}")
        print(f"Harga        : Rp{self.harga}")
        print(f"Genre        : {self.genre}")
        print(f"Tahun Terbit : {self.tahunTerbit}")
        print(f"Sinopsis     : {self.sinopsis}")
        print(f"Kode         : {self.kode}")



# =========================
# CLASS BUKU PELAJARAN
# =========================

class BukuPelajaran(Ebook):
    def __init__(self, judul, penulis, harga, genre, tahunTerbit, kode, ringkasan):
        super().__init__(judul, penulis, harga, genre, tahunTerbit, kode)
        self.ringkasan = ringkasan

    # Overriding
    def lihatInfoEbook(self):
        print("=== BUKU PELAJARAN ===")
        print(f"Judul        : {self.judul}")
        print(f"Penulis      : {self.penulis}")
        print(f"Harga        : Rp{self.harga}")
        print(f"Genre        : {self.genre}")
        print(f"Tahun Terbit : {self.tahunTerbit}")
        print(f"Ringkasan    : {self.ringkasan}")
        print(f"Kode         : {self.kode}")



# =========================
# CLASS KATALOG
# =========================

class Katalog:
    def __init__(self, daftarEbook):
        self.daftarEbook = daftarEbook

    # Menampilkan semua ebook
    def tampilKatalog(self):
        if len(self.daftarEbook) == 0:
            print("Katalog masih kosong.")
        else:
            print("=== KATALOG E-BOOK ===")
            for i in self.daftarEbook:
                print(f"{i.kode} - {i.judul} - Rp{i.harga}")

    # Mencari ebook berdasarkan judul
    def cariEbook(self, judul):
        for i in self.daftarEbook:
            if i.judul.lower() == judul.lower():
                return i
        return None



# =========================
# CLASS LIBRARY
# =========================

class Library:
    def __init__(self):
        self.daftarEbook = []

    # Menambahkan ebook yang sudah dibeli
    def tambahEbook(self, ebook):
        self.daftarEbook.append(ebook)

     # Menampilkan Library
    def tampilLibrary(self):
        if len(self.daftarEbook) == 0:
            print("Library ente masih kosong.")
        else:
            print("=== LIBRARY SAYA ===")
            for i in self.daftarEbook:
                print(f"{i.kode} - {i.judul} - Rp{i.harga}")



# =========================
# CLASS TRANSAKSI
# =========================

class Transaksi:
    noTransaksi = 1

    def __init__(self, user, ebook, total, status):
        self.nomor = Transaksi.noTransaksi
        Transaksi.noTransaksi += 1
        self.user = user
        self.ebook = ebook
        self.total = total
        self.status = status

    def lihatInfoTransaksi(self):
        print("=== DETAIL TRANSAKSI ===")
        print(f"Nomor Transaksi : TRX{self.nomor}")
        print(f"Pembeli         : {self.user.username}")
        print(f"E-book          : {self.ebook.judul}")
        print(f"Total           : Rp{self.total}")
        print(f"Status          : {self.status}")


# =========================
# MEMBUAT USER DAN E-BOOK
# =========================

user1 = User("Shashak", "AuahCpek123", 200000, "dinda@gmail.com")
user2 = User("Julpak", "Salam90Bangga", 200000, "siti@gmail.com")
user3 = User("Ayak", "PilihNo3", 200000, "intan@gmail.com")

novel1 = Novel(
    "Malice", "Keigo Higashino",
    99000, "Detektif",
    1996, "NOV001",
    "Detektif Kaga menyelidiki kasus pembunuhan dengan motif pelaku yang rumit.")

buku1 = BukuPelajaran(
    "Kalkulus Dasar", "Budi Santoso",
    80000, "Pendidikan",
    2020, "BKP001",
    "Materi dasar matematika untuk siswa SMA.")

novel2 = Novel(
    "The Devotion of Suspect X", "Keigo Higashino",
    105000, "Misteri",
    2005, "NOV002",
    "Seorang guru matematika membantu menyembunyikan sebuah kejahatan.")


# =========================
# PENGGUNAAN METHOD KATALOG
# =========================
# BUAT DAFTAR E-BOOK DAN KATALOG
daftarEbook = [novel1, buku1, novel2]
katalog = Katalog(daftarEbook)

# LIHAT KATALOG
katalog.tampilKatalog()

# CARI E-BOOK DARI KATALOG
ebook_ditemukan = katalog.cariEbook("Malice")
if ebook_ditemukan:
    print("E-book ditemukan:")
    ebook_ditemukan.lihatInfoEbook()
print()


# =========================
# PENGGUNAAN METHOD E-BOOK
# =========================
print("=== INFO SEMUA E-BOOK ===")
for i in daftarEbook:
    i.lihatInfoEbook()
    print()


# =========================
# PENGGUNAAN METHOD USER
# =========================
print(user1.lihatPassword("AuahCpek123"))
print(user2.saldo)
print(user3.email)
user1.email = "dindakAmara@gmail.com"

# TOPUP SALDO
user3.topup(100000)
print("Saldo setelah top up:", user3.saldo)


# =========================
# PENGGUNAAN METHOD LIBRARY
# =========================
user1.library.tampilLibrary()


# =========================
# PEMBELIAN E-BOOK
# =========================
print("Saldo awal:", user1.saldo)
user1.beliEbook(ebook_ditemukan)
print("Saldo setelah membeli:", user1.saldo)


# =========================
# PENGGUNAAN METHOD TRANSAKSI
# =========================
for i in user1.daftarTransaksi:
    i.lihatInfoTransaksi()