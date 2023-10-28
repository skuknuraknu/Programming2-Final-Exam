""" IMPORT LIBRARY YANG DIBUTUHKAN
    👏 datetime untuk mengambil tanggal dan waktu saat ini
    👏 time untuk mengatur waktu
"""
from datetime import datetime
import time
from guest import Guest
from color import Color, BackgroundColor

# 👇 Membuat class khusus untuk admin
class KasirAdmin:
    # 👇 Membuat constructor agar memanggil method welcome pertama kali
    def __init__(self):
        self.welcome()
    
    # 👇 Fungsi untuk membuat garis
    def garis(self):
        print("======================================================")

    # 👇 Fungsi untuk menampilkan pesan selamat datang
    def welcome(self):
        self.garis() # Akan menampilkan garis
        current_date = datetime.today().strftime('%Y-%m-%d')
        # 👇 Menampilkan pesan selamat datang beserta dengan waktu sekarang
        message = f"    Selamat Datang di Aplikasi Kasir / {current_date}     "
        print(BackgroundColor.MERAH + message + BackgroundColor.RESET)
        self.garis() # Akan menampilkan garis

    def tambah_barang(self):
        self.garis()
        print(BackgroundColor.IJO + "                      Tambah Barang                   " + BackgroundColor.RESET)
        self.garis()

    def lihat_barang(self):
        self.garis()
        print("Lihat Barang")
        self.garis()

    def edit_barang(self):
        self.garis()
        print("Edit Barang")
        self.garis()

    def hapus_barang(self):
        self.garis()
        print("Hapus Barang")
        self.garis()

    def admin_menu(self):
        print("[1]. Tambah Barang")
        print("[2]. Lihat Barang")
        print("[3]. Edit Barang")
        print("[4]. Hapus Barang")
        print("[5]. Keluar")
        pilihan_menu = input("Pilihan anda (1/2/3/4/5):")
        if pilihan_menu == "1":
            self.tambah_barang()
        elif pilihan_menu == "2":
            self.lihat_barang()
        elif pilihan_menu == "3":
            self.edit_barang()
        elif pilihan_menu == "4":
            self.hapus_barang()
        elif pilihan_menu == "5":
            return False
        else:
            print(Color.MERAH + "Pilihan tidak valid")
            return False
        
    # 👇 Method untuk melakukan proses autentikasi pengguna
    def auth_admin(self):
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        # 👇 Cek apakah username & password yang dimasukkan adalah `admin`
        if username == "admin" and password == "admin":
            # 👇 Menampilkan pesan sementara
            for x in range(0, 2):
                message = "Mohon tunggu sebentar" + "." * x
                print(message, end="\r")
                time.sleep(0.5)
            # 👇 Menampilkan pesan sementara
            for i in range(0, 2):
                message = "Menghubungkan ke database" + "." * i
                print(message, end="\r")
                time.sleep(0.5)
            self.garis()
            print(Color.IJO + "             Berhasil Login sebagai Admin" + BackgroundColor.RESET)
            self.garis()
            self.admin_menu()
        else:
            print(Color.MERAH + "Login Gagal" + BackgroundColor.RESET)
            return False

    # 👇 Menampilkan menu untuk autentikasi pengguna
    def auth(self):
        print("[1]. Login sebagai Admin")
        print("[2]. Login sebagai Guest")
        print("[3]. Keluar")
        
        pilihan_login = input("Pilihan anda (1/2/3):")

        if pilihan_login == "1":  # 👇 Jika pilihan adalah `1`
            self.auth_admin()
        elif pilihan_login == "2":  # 👇 Jika pilihan adalah `2`
            Guest()  # Tampilkan menu guest
        elif pilihan_login == "3":
            return False
        else:
            print(Color.MERAH + "Pilihan tidak valid")
            return False