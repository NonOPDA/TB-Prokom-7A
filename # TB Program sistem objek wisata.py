#Program sistem objek wisata
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


class Tempat_Wisata:
    def __init__(self, nama, lokasi, harga):
        self.nama = nama
        self.lokasi = lokasi
        self.harga = harga

    def info(self):
        return f"{self.nama} | {self.lokasi} | Rp{self.harga:,.0f}".replace(",", ".")
    
    def menu_awal(self):
        while True:
            print("\n=== SISTEM PEMESANAN TEMPAT WISATA ===")
            print("1. Login sebagai Admin")
            print("2. Login / Register Customer")
            print("0. Keluar")
            pilihan = input("Pilih opsi: ")

            if pilihan == "1":
                self.login_admin()
            elif pilihan == "2":
                self.menu_customer()
            elif pilihan == "0":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")

    def login_admin(self):
        username = input("Username: ")
        password = input("Password: ")
        if self.admin.login(username, password):
            print("Login berhasil sebagai Admin.")
            self.menu_admin()
        else:
            print("Login gagal.")

    def menu_admin(self):
        while True:
            print("\n--- MENU ADMIN ---")
            print("1. Tambah Tempat Wisata")
            print("2. Lihat Daftar Tempat")
            print("3. Edit Tempat Wisata")
            print("4. Hapus Tempat Wisata")
            print("5. Logout")
            pilih = input("Pilih (1/2/3/4/5): ")

            if pilih == "1":
                nama = input("Nama Tempat: ")
                lokasi = input("Lokasi: ")
                harga = int(input("Harga Tiket: "))
                self.tempat_wisata.append(Tempat_Wisata(nama, lokasi, harga))
                print("Tempat wisata ditambahkan.")
            elif pilih == "2":
                self.tampilkan_tempat_wisata()
            elif pilih == "3":
                self.edit_tempat_wisata()
            elif pilih == "4":
                self.hapus_tempat_wisata()
            elif pilih == "5":
                break
            else:
                print("Pilihan tidak valid.")

    def tampilkan_tempat_wisata(self):
        if not self.tempat_wisata:
            print("Belum ada tempat wisata.")
            return
        for i, tempat in enumerate(self.tempat_wisata):
            print(f"{i+1}. {tempat.info()}")

    def edit_tempat_wisata(self):
        self.tampilkan_tempat_wisata()
        try:
            idx = int(input("Pilih nomor yang ingin diedit: ")) - 1
            if 0 <= idx < len(self.tempat_wisata):
                tempat = self.tempat_wisata[idx]
                print(f"Edit data untuk: {tempat.info()}")
                nama_baru = input("Nama baru (biarkan kosong jika tidak ingin mengubah): ")
                lokasi_baru = input("Lokasi baru (biarkan kosong jika tidak ingin mengubah): ")
                harga_baru = input("Harga baru (biarkan kosong jika tidak ingin mengubah): ")

                if nama_baru:
                    tempat.nama = nama_baru
                if lokasi_baru:
                    tempat.lokasi = lokasi_baru
                if harga_baru:
                    tempat.harga = int(harga_baru)

                print("Data berhasil diperbarui.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input tidak valid.")

    def hapus_tempat_wisata(self):
        self.tampilkan_tempat_wisata()
        try:
            idx = int(input("Pilih nomor yang ingin dihapus: ")) - 1
            if 0 <= idx < len(self.tempat_wisata):
                konfirmasi = input(f"Yakin ingin menghapus '{self.tempat_wisata[idx].nama}'? (y/n): ").lower()
                if konfirmasi == "y":
                    del self.tempat_wisata[idx]
                    print("Data berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input tidak valid.")
    
if __name__ == "__main__":
    wisata = Tempat_Wisata()
    data_wisata = []
    wisata.menu_awal()