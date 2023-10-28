from color import Color, BackgroundColor
import time
from ultilities import Utilities
from prettytable import PrettyTable

# 👇 Membuat class khusus untuk guest
class Guest:
    is_menu_running = True
    utilities = Utilities('products.json')

    # 👇 Membuat constructor agar memanggil method welcome pertama kali
    def __init__(self):
        self.welcome()

    # 👇 Fungsi untuk membuat garis
    def garis(self):
        print("======================================================")

    # 👇 Fungsi untuk menampilkan pesan selamat datang
    def welcome(self):
        # for x in range(0, 4):
        #         message = "Anda login sebagai guest" + "-" * x
        #         print(message, end="\r")
        #         time.sleep(0.5)
        print("")
        print(Color.IJO + "Berhasil Login sebagai Guest" + BackgroundColor.RESET)
        self.menu_guest()
    
    def lihat_produk(self):
        self.garis()
        print(BackgroundColor.BIRU_GELAP + "                         PRODUK                       " + BackgroundColor.RESET)
        self.garis()
        # 👇 Membaca file json dari method `read_products_json`
        lists_barang = self.utilities.read_products_json()
        # 👇 Membuat tabel dari library `PrettyTable` untuk menampilkan data barang
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK', "DISCOUNT"])
        total_barang = 0
        # 👇 Melakukan perulangan untuk menampilkan data barang
        for product in lists_barang['products']:
            total_barang += 1
            tabel_barang.add_row([
                product['id'], product['name'], 
                product['price'], product['stock'],
                product['discount']])
        print(f"{Color.KUNING} TABEL PRODUK {BackgroundColor.RESET}")
        print(tabel_barang)
        print(f"Total produk: {total_barang}")
    
    def cari_produk(self):
        self.garis()
        print(BackgroundColor.BIRU_GELAP + "                      CARI PRODUK                     " + BackgroundColor.RESET)
        self.garis()
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK', "DISCOUNT"])
        nama_produk = input(f"{Color.BIRU}Masukkan nama produk yang ingin dicari: {BackgroundColor.RESET}")
        filter_barang = self.utilities.filter_product(nama_produk)
        total_barang = 0
        for product in filter_barang:
            total_barang += 1
            tabel_barang.add_row([
                product['id'], product['name'], 
                product['price'], product['stock'],
                product['discount']])
        print(f"{Color.KUNING}Hasil pencarian dari kata `{nama_produk}`: {BackgroundColor.RESET}")
        print(tabel_barang)
        print(f"Total produk: {total_barang}")

    # 👇 Fungsi untuk menampilkan menu
    def menu_guest(self):
        while self.is_menu_running:
            self.garis()
            print(BackgroundColor.IJO + "                      MENU GUEST                      " + BackgroundColor.RESET)
            self.garis()
            print("[1] Lihat Produk")
            print("[2] Cari Produk")
            print("[3] Beli Produk")
            print("[4] Keluar")
            pilihanUser = input(f"{Color.KUNING}Pilihan anda (1/2/3/4): {BackgroundColor.RESET}")
            if pilihanUser == '1':
                self.lihat_produk()
            elif pilihanUser == '2':
                self.cari_produk()
            elif pilihanUser == '3':
                self.beli_produk()
                self.is_menu_running = False
            elif pilihanUser == '4':
                self.is_menu_running = False
            else:
                print(Color.MERAH + "Pilihan tidak valid" + BackgroundColor.RESET)