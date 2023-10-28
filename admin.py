""" IMPORT LIBRARY YANG DIBUTUHKAN
    👏 datetime untuk mengambil tanggal dan waktu saat ini
    👏 time untuk mengatur waktu
"""
from datetime import datetime
import time
from guest import Guest
from color import Color, BackgroundColor
import json
from ultilities import Utilities
from prettytable import PrettyTable

# 👇 Membuat class khusus untuk admin
class KasirAdmin:
    utilities        = Utilities("products.json")
    admin_is_running = True

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
        id_barang    = input("Masukkan id barang: ")
        nama_barang  = input("Masukkan nama barang: ")
        stock_barang = input("Masukkan stock barang: ")
        harga_barang = input("Masukkan harga barang: ")
        barang = {
            'id': id_barang,
            'name': nama_barang,
            'price': harga_barang,
            'stock': stock_barang
        }
        self.utilities.add_product_to_json(barang)

    def lihat_barang(self):
        self.garis()
        print(BackgroundColor.IJO + "                      Lihat Barang                    " + BackgroundColor.RESET)
        self.garis()
        # 👇 Membaca file json dari method `read_products_json`
        lists_barang = self.utilities.read_products_json()
        # 👇 Membuat tabel dari library `PrettyTable` untuk menampilkan data barang
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK'])
        # 👇 Melakukan perulangan untuk menampilkan data barang
        for product in lists_barang['products']:
            tabel_barang.add_row([product['id'], product['name'], product['price'], product['stock']])
        print(f"{Color.KUNING} TABEL BARANG {BackgroundColor.RESET}")
        print(tabel_barang)

    def edit_barang(self):
        self.garis()
        print(BackgroundColor.IJO + "                       Edit Barang                    " + BackgroundColor.RESET)
        id_barang = input("Masukkan id barang yang ingin diedit: ")
        nama_barang  = input("Masukkan nama barang: ")
        stock_barang = input("Masukkan stock barang: ")
        harga_barang = input("Masukkan harga barang: ")
        barang = {
            'id': id_barang,
            'name': nama_barang,
            'price': harga_barang,
            'stock': stock_barang
        }
        self.utilities.update_product(id_barang, barang)

    def hapus_barang(self):
        self.garis()
        print(BackgroundColor.IJO + "                      Hapus Barang                    " + BackgroundColor.RESET)
        id_barang = input("Masukkan id barang yang ingin dihapus: ")
        self.utilities.del_product(id_barang)
        self.garis()

    def admin_menu(self):
        while self.admin_is_running == True:
            self.garis()
            print(f"{BackgroundColor.IJO}                       MENU ADMIN                     {BackgroundColor.RESET}")
            self.garis()
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
                self.admin_is_running = False
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
            print(Color.IJO + "Berhasil Login sebagai Admin" + BackgroundColor.RESET)
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