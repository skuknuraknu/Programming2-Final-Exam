from color import Color, BackgroundColor
import time
from ultilities import Utilities
from prettytable import PrettyTable
import locale

# 👇 Membuat class khusus untuk guest
class Guest:
    is_menu_running = True
    is_paying_running = True
    utilities = Utilities('products.json')
    belanjaan = {"products":[{
            "id": "P-003",
            "name": "Karet Gelang",
            "price": "2500",
            "stock": "10",
            "discount": "5%"
        },{
            "id": "P-001",
            "name": "Gelang",
            "price": "5500",
            "stock": "10",
            "discount": "5%"
        }]}

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
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK'])
        total_barang = 0
        # 👇 Melakukan perulangan untuk menampilkan data barang
        for product in lists_barang['products']:
            total_barang += 1
            tabel_barang.add_row([
                product['id'], product['name'], 
                product['price'], product['stock']])
        print(f"{Color.KUNING} TABEL PRODUK {BackgroundColor.RESET}")
        print(tabel_barang)
        print(f"Total produk: {total_barang}")
    
    def cari_produk(self):
        self.garis()
        print(BackgroundColor.BIRU_GELAP + "                      CARI PRODUK                     " + BackgroundColor.RESET)
        self.garis()
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK'])
        nama_produk = input(f"{Color.BIRU}Masukkan nama produk yang ingin dicari: {BackgroundColor.RESET}")
        filter_barang = self.utilities.filter_product(nama_produk)
        total_barang = 0
        for product in filter_barang:
            total_barang += 1
            tabel_barang.add_row([
                product['id'], product['name'], 
                product['price'], product['stock']])
        print(f"{Color.KUNING}Hasil pencarian dari kata `{nama_produk}`: {BackgroundColor.RESET}")
        print(tabel_barang)
        print(f"Total produk: {total_barang}")

    def beli_produk(self):
        self.garis()
        print(BackgroundColor.BIRU_GELAP + "                      BELI PRODUK                     " + BackgroundColor.RESET)
        self.garis()
        id_produk    = input(f"{Color.BIRU}Masukkan id produk yang ingin dibeli: {BackgroundColor.RESET}")
        barang = self.utilities.read_products_json()
        for product in barang['products']:
            if product['id'] == id_produk:
                self.belanjaan['products'].append(product)
                print(f"{Color.IJO}Produk dengan id `{id_produk}` berhasil ditambahkan ke keranjang{BackgroundColor.RESET}")
                return True
        print(f"{Color.MERAH}Produk dengan id `{id_produk}` tidak ditemukan{BackgroundColor.RESET}")
        return False

    def bayar_produk(self):
        locale.setlocale(locale.LC_ALL, 'id_ID')
        self.garis()
        print(BackgroundColor.BIRU_GELAP + "                      BAYAR PRODUK                    " + BackgroundColor.RESET)
        self.garis()
        tabel_barang = PrettyTable(['ID','NAME', 'PRICE', 'STOCK'])
        total_harga = 0
        for product in self.belanjaan['products']:
            total_harga  += int(product['price'])
            tabel_barang.add_row([
                product['id'], product['name'], 
                product['price'], product['stock']])
        print(f"{Color.KUNING}+----------------- KERANJANG KUNING -----------------+{BackgroundColor.RESET}")
        print(tabel_barang)
        print(f"Total uang yang harus dibayar: { locale.currency(total_harga, grouping=True) }")
        print(f"Total produk yang akan dibeli: { len( self.belanjaan['products'] ) } ")
        self.is_paying_running = True
        if len(self.belanjaan['products'] ) == 0:
            print(f"{Color.MERAH}Keranjang anda kosong{BackgroundColor.RESET}")
        elif len( self.belanjaan['products'] ) != 0:
            while self.is_paying_running:
                uang_user = input(f"{Color.BIRU}Masukkan uang anda: {BackgroundColor.RESET}")
                if int(uang_user) < total_harga:
                    print(f"{Color.MERAH}Uang anda kurang!{BackgroundColor.RESET}")
                elif int(uang_user) == total_harga:
                    print(f"{Color.IJO}Uang yang ada berikan pas{BackgroundColor.RESET}")
                    self.belanjaan['products'] = []
                    self.is_paying_running = False 
                elif int(uang_user) >= total_harga:
                    print(f"{Color.IJO}Kembalian anda: { locale.currency(int(uang_user) - total_harga, grouping=True) }{BackgroundColor.RESET}")
                    self.belanjaan['products'] = []
                    self.is_paying_running = False     
                print(f"{Color.KUNING}+---------- Terima kasih sudah berbelanja -----------+{BackgroundColor.RESET}")

    # 👇 Fungsi untuk menampilkan menu
    def menu_guest(self):
        while self.is_menu_running:
            self.garis()
            print(BackgroundColor.IJO + "                      MENU GUEST                      " + BackgroundColor.RESET)
            self.garis()
            print(f"{Color.KUNING}                                             Cart {BackgroundColor.RESET}: {len(self.belanjaan['products'])}")
            print("[1] Lihat Produk")
            print("[2] Cari Produk")
            print("[3] Beli Produk")
            print("[4] Bayar Produk")
            print("[5] Keluar")
            pilihanUser = input(f"{Color.KUNING}Pilihan anda (1/2/3/4): {BackgroundColor.RESET}")
            if pilihanUser == '1':
                self.lihat_produk()
            elif pilihanUser == '2':
                self.cari_produk()
            elif pilihanUser == '3':
                self.beli_produk()
            elif pilihanUser == '4':
                self.bayar_produk()
            elif pilihanUser == '5':
                self.is_menu_running = False
            else:
                print(Color.MERAH + "Pilihan tidak valid" + BackgroundColor.RESET)