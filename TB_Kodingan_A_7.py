class DataDasar:
    def __init__(self, kode, lokasi, nama, desc, cp):
        self.kode = kode
        self.lokasi = lokasi
        self.nama = nama
        self.desc = desc
        self.cp = cp

class Data:
    def __init__(self):
        self.namah_daftar = []
        self.namaw_daftar = [] 
        self.namar_daftar = []

    def data_ahotel(self):
        datah = [
            {"kode": "PDH01", "lokasi": "Padang", "nama": "Mercure Padang", "desc": "Western Food", "cp": "0811"},
            {"kode": "PDH02", "lokasi": "Padang", "nama": "Grand Zuri Padang", "desc": "Tengah Kota", "cp": "0812"},
            {"kode": "BTH01", "lokasi": "Batam", "nama": "Batam Marriott Hotel Harbour Bay", "desc": "Sea View", "cp": "0813"},
            {"kode": "BTH02", "lokasi": "Batam", "nama": "The Music Hotel ", "desc": "Budget-friendly", "cp": "0814"},
            {"kode": "BLH01", "lokasi": "Bali", "nama": "Neo Kuta Jelantik Hotel", "desc": "Budget-friendly", "cp": "0815"},
            {"kode": "BLH02", "lokasi": "Bali", "nama": "Hotel Siesta Legian", "desc": "Dekat Pantai", "cp": "0816"},
        ]
        for dh in datah:
            self.namah_daftar.append(DataDasar(dh["kode"], dh["lokasi"], dh["nama"], dh["desc"], dh["cp"]))

    def data_awis(self):
        dataw = [
            {"kode": "PDW01", "lokasi": "Padang", "nama": "Pantai Air Manis", "desc": "Legenda Malin Kundang", "cp": "0821"},
            {"kode": "PDW02", "lokasi": "Padang", "nama": "Jembatan Siti Nurbaya", "desc": "Pemandangan Pelabuhan", "cp": "0822"},
            {"kode": "BTW01", "lokasi": "Batam", "nama": "Mega wisata Ocarina Theme Park", "desc": "Taman Hiburan Keluarga", "cp": "0823"},
            {"kode": "BTW02", "lokasi": "Batam", "nama": "Miniature House Indonesia", "desc": "Free-Entry", "cp": "0824"},
            {"kode": "BLW01", "lokasi": "Bali", "nama": "Pura Uluwatu", "desc": "Kuil Hindu", "cp": "0825"},
            {"kode": "BLW02", "lokasi": "Bali", "nama": "Garuda Wisnu Kencana", "desc": "Patung raksasa", "cp": "0826"}
        ]
        for dw in dataw:
            self.namaw_daftar.append(DataDasar(dw["kode"], dw["lokasi"], dw["nama"], dw["desc"], dw["cp"]))

    def data_arm(self):
        datar = [
            {"kode": "PDR01", "lokasi": "Padang", "nama": "Ayam Bakar Sing A Song ", "desc": "Spesialis ayam bakar", "cp": "0831"},
            {"kode": "PDR02", "lokasi": "Padang", "nama": "RM Lamun Ombak", "desc": "Masakan Padang", "cp": "0832"},
            {"kode": "BTR01", "lokasi": "Batam", "nama": "Wey Wey Seafood ", "desc": "Spesialis seafood", "cp": "0833"},
            {"kode": "BTR02", "lokasi": "Batam", "nama": "My Garden Resto", "desc": "Cafe berkonsep taman", "cp": "0834"},
            {"kode": "BLR01", "lokasi": "Bali", "nama": "Kala Uluwatu", "desc": "Greek-Inspired Restaurant", "cp": "0835"},
            {"kode": "BLR02", "lokasi": "Bali", "nama": "Warung Laota", "desc": "Hidangan ala Hongkong", "cp": "0836"}
        ]
        for dr in datar:
            self.namar_daftar.append(DataDasar(dr["kode"], dr["lokasi"], dr["nama"], dr["desc"], dr["cp"]))

    def tampil_data(self, data_list):
        if not data_list:
            print("Belum ada data")
        else:
            print("=" * 106)
            print("\n| {:^5} | {:^10} | {:^35} | {:^25} | {:^14} |".format("Kode", "Lokasi", "Nama", "Deskripsi", "Contact Person"))
            for item in data_list:
                print("-" * 106)
                print("| {:^5} | {:^10} | {:^35} | {:^25} | {:^14} |".format(item.kode, item.lokasi, item.nama, item.desc, item.cp))
            print("=" * 106)

    def tambah_data(self, kota_choise, data_list):
        kode = input("Kode: ").upper()
        lokasi = kota_choise
        nama = input("Nama: ").capitalize()
        desc = input("Deskripsi: ").capitalize()
        cp = input("Contact Person: ")
        data_list.append(DataDasar(kode, lokasi, nama, desc, cp))
        print("Data berhasil ditambahkan")

    def hapus_data(self, data_list):
        kode = input("Masukkan Kode: ").upper()
        for item in data_list:
            if item.kode == kode:
                data_list.remove(item)
                print("Data berhasil dihapus")
                return
        print("Kode tidak valid")

    def edit_data(self, item):
        print("Data yang dapat diubah:")
        print("a. Lokasi")
        print("b. Nama")
        print("c. Deskripsi")
        print("d. Contact Person")
        
        pilihan = input("Masukkan pilihan yang akan di edit: ")
        
        if pilihan == "a":
            lokasi = input(f"Lokasi [{item.lokasi}]: ").capitalize()
            item.lokasi = lokasi if lokasi else item.lokasi
        elif pilihan == "b":
            nama = input(f"Nama [{item.nama}]: ").capitalize()
            item.nama = nama if nama else item.nama
        elif pilihan == "c":
            desc = input(f"Deskripsi [{item.desc}]: ").capitalize()
            item.desc = desc if desc else item.desc
        elif pilihan == "d":
            cp = input(f"Contact Person [{item.cp}]: ").capitalize()
            item.cp = cp if cp else item.cp
        else:
            print("Pilihan tidak valid")

        print(f"Data {item.nama} telah diperbarui")

    def edit_data_menu(self, data_list):
        kode = input("Masukkan kode yang akan diubah: ").upper()
        for item in data_list:
            if item.kode == kode:
                self.edit_data(item)
                return
        print("Data tidak ditemukan")

class SistemPariwisata:
    def __init__(self):
        self.users = {}  # Menyimpan username dan password
        self.data = Data()
        self.data.data_ahotel()
        self.data.data_awis()
        self.data.data_arm()

    def sign_up(self):
        print("\n=== Sign Up ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        role = input("Masukkan peran (admin/user): ").lower()

        if role not in ["admin", "user"]:
            print("Peran tidak valid. Harap masukkan 'admin' atau 'user'.")
            return

        if username in self.users:
            print("Username sudah terdaftar. Silakan gunakan username lain.")
            return
        
        if not username or not password:
            print("Username dan password tidak boleh kosong!")
            return


        self.users[username] = {"password": password, "role": role}
        print("\n!!!Pendaftaran berhasil. Silakan Login !!!")

    def login(self):
        while True:
            print("\n=== Login Sistem Pariwisata ===")
            username = input("Username: ")
            password = input("Password: ")

            if username in self.users and self.users[username]["password"] == password:
                role = self.users[username]["role"]
                if role == "admin":
                    print("\n!!!Berhasil login sebagai admin!!!")
                    self.menu_admin()
                else:
                    print("\n!!!Berhasil login sebagai user!!!")
                    self.menu_user()
                break
            else:
                print("Login gagal! Username atau password salah. Silahkan coba lagi")
                continue

    def menu_admin(self):
        while True: 
            print("\n===SELAMAT DATANG DI MENU ADMIN===")
            print("\nMenu Admin")
            print("1. Tampilkan Data")
            print("2. Tambah Data")
            print("3. Hapus Data")
            print("4. Edit Data")
            print("5. Keluar")

            pilihan = input("Silakan masukkan menu (1/2/3/4/5): ")
            if pilihan == "5":
                print("Program selesai. Terimakasih sudah menggunakan program kami!")
                exit()
            elif pilihan in ["1", "2", "3", "4"]:
                print("\nPilih kota:")
                print("1. Padang")
                print("2. Batam")
                print("3. Bali")
                kota_choice = input("Masukkan pilihan kota (1/2/3): ")

                if kota_choice == "1":
                    kota = "Padang"
                elif kota_choice == "2":
                    kota = "Batam"
                elif kota_choice == "3":
                    kota = "Bali"
                else:
                    print("Pilihan tidak valid.")
                    continue
                while True:
                    print("\nData yang dapat dipilih:")
                    print("1. Hotel")
                    print("2. Wisata")
                    print("3. Rumah Makan")
                    print("x. Kembali ke menu utama")
                    sub_pilihan = input("Silakan masukkan pilihan: ").lower()

                    if sub_pilihan == "x":
                        break
                    if sub_pilihan == "1":
                        data_list = self.data.namah_daftar
                    elif sub_pilihan == "2":
                        data_list = self.data.namaw_daftar
                    elif sub_pilihan == "3":
                        data_list = self.data.namar_daftar
                    else:
                        print("Pilihan tidak valid.")
                        continue

                    filtered_data = [item for item in data_list if item.lokasi.lower() == kota.lower()]

                    if pilihan == "1":
                        self.data.tampil_data(filtered_data)
                    elif pilihan == "2":
                        self.data.tampil_data(filtered_data)
                        self.data.tambah_data(kota, data_list)
                    elif pilihan == "3":
                        self.data.tampil_data(filtered_data)
                        self.data.hapus_data(data_list)
                    elif pilihan == "4":
                        self.data.tampil_data(filtered_data)
                        self.data.edit_data_menu(data_list)
                    lanjut = input("Apakah ingin lanjut? (y/n): ").lower()
                    if lanjut != "y":
                        break

            else:
                print("Pilihan tidak valid. Silahkan coba lagi")

    def menu_user(self):
        while True:
            print("\n===SELAMAT DATANG DI MENU USER===")
            print("\nMenu User")
            print("1. Tampilkan Data Berdasarkan Kota")
            print("2. Keluar")

            pilihan = input("Silakan masukkan menu (1/2): ")

            if pilihan == "1":
                print("\nPilih kota:")
                print("1. Padang")
                print("2. Batam")
                print("3. Bali")
                kota_choice = input("Masukkan pilihan kota (1/2/3): ")

                if kota_choice == "1":
                    kota = "Padang"
                elif kota_choice == "2":
                    kota = "Batam"
                elif kota_choice == "3":
                    kota = "Bali"
                else:
                    print("Pilihan tidak valid.")
                    continue

                print("\nData apa yang ingin ditampilkan?")
                print("1. Hotel")
                print("2. Wisata")
                print("3. Rumah Makan")
                print("x. Kembali ke menu utama")
                sub_pilihan = input("Silakan masukkan pilihan: ").lower()

                if sub_pilihan == "1":
                    self.data.tampil_data([h for h in self.data.namah_daftar if h.lokasi.lower() == kota.lower()])
                elif sub_pilihan == "2":
                    self.data.tampil_data([w for w in self.data.namaw_daftar if w.lokasi.lower() == kota.lower()])
                elif sub_pilihan == "3":
                    self.data.tampil_data([r for r in self.data.namar_daftar if r.lokasi.lower() == kota.lower()])
                elif sub_pilihan == "x":
                    continue
                else:
                    print("Pilihan tidak tersedia.")
                    continue

                lanjut = input("Apakah ingin lanjut? (y/n): ").lower()
                if lanjut != "y":
                    print("Program selesai. Terimakasih sudah menggunakan program kami!")
                    break

            elif pilihan == "2":
                print("Program selesai. Terimakasih sudah menggunakan program kami!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    def tampilkan_data_kota(self, kota):
        print(f"Data untuk kota {kota}:")
        if kota == "Padang":
            self.data.tampil_data(self.data.namah_daftar)
            self.data.tampil_data(self.data.namaw_daftar)
            self.data.tampil_data(self.data.namar_daftar)
        elif kota == "Batam":
            self.data.tampil_data(self.data.namah_daftar)
            self.data.tampil_data(self.data.namaw_daftar)
            self.data.tampil_data(self.data.namar_daftar)
        elif kota == "Bali":
            self.data.tampil_data(self.data.namah_daftar)
            self.data.tampil_data(self.data.namaw_daftar)
            self.data.tampil_data(self.data.namar_daftar)

    def get_data_list(self, pilihan, kota):
        if pilihan == "1":
            return [h for h in self.data.namah_daftar if h.lokasi.lower() == kota.lower()]
        elif pilihan == "2":
            return [w for w in self.data.namaw_daftar if w.lokasi.lower() == kota.lower()]
        elif pilihan == "3":
            return [r for r in self.data.namar_daftar if r.lokasi.lower() == kota.lower()]


def main():
    sistem = SistemPariwisata()
    while True:
        print("\n=== Selamat Datang di Sistem Objek Pariwisata ===")
        print("Kota Padang Batam Bali")
        print("\n==MENU UTAMA==")
        print("1. Sign Up")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Silakan masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            sistem.sign_up()
        elif pilihan == "2":
            sistem.login()
        elif pilihan == "3":
            print("Program selesai. Terimakasih sudah menggunakan program kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
