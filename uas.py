""" IMPORT LIBRARY YANG DIBUTUHKAN
    👏 datetime untuk mengambil tanggal dan waktu saat ini
    👏 time untuk mengatur waktu
"""
from datetime import datetime
import time

# 👇 Membuat class `warna` untuk menyimpan data warna
class warna:
    BIRU = '\033[94m'  # Warna biru
    CYAN = '\033[96m'  # Warna cyan
    IJO = '\033[92m'   # Warna hijau
    KUNING = '\033[93m'  # Warna kuning
    MERAH = '\033[91m'  # Warna merah

# 👇 Membuat class `bgWarna` untuk menyimpan data warna background
class bgWarna:
    MERAH = '\x1b[5;30;47m'  # Warna latar belakang merah
    RESET = '\x1b[0m'  # RESET berguna untuk mereset warna menjadi default

# 👇 Fungsi untuk mengambil waktu saat ini
def waktuSekarang():
    return datetime.today().strftime('%Y-%m-%d')

# 👇 Fungsi untuk membuat garis
def garis():
    print("======================================================")

# 👇 Fungsi untuk menampilkan pesan selamat datang
def welcome():
    garis()  # Akan menampilkan garis
    # 👇 Menampilkan pesan selamat datang beserta dengan waktu sekarang dan melakukan reset warna
    print(bgWarna.MERAH + f"    Selamat Datang di Aplikasi Kasir / {waktuSekarang()}     " + bgWarna.RESET)
    garis()  # Akan menampilkan garis

# 👇 Fungsi untuk melakukan proses autentikasi pengguna
def authAdmin():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    # 👇 Cek apakah username & password yang dimasukkan adalah `admin`
    if username == "admin" and password == "admin":
        # 👇 Menampilkan pesan sementara
        for x in range(0, 3):
            b = "Mohon tunggu sebentar" + "." * x
            print(b, end="\r")
            time.sleep(0.5)
        # 👇 Menampilkan pesan sementara
        for i in range(0, 5):
            pesan = "Menghubungkan ke database" + "." * i
            print(pesan, end="\r")
            time.sleep(0.5)
        garis()
        print(warna.IJO + "             Berhasil Login sebagai Admin" + bgWarna.RESET)
        garis()
        return True
    else:
        print(warna.MERAH + "Login Gagal" + bgWarna.RESET)
        return False

# 👇 Menampilkan menu untuk autentikasi pengguna
def auth():
    print("[1]. Login sebagai Admin")
    print("[2]. Login sebagai Guest")
    print("[3]. Keluar")
    pilihanLogin = input("Pilihan anda(1/2/3):")
    if (pilihanLogin == "1"):  # 👇 Jika pilihan adalah `1`
        authAdmin()
    elif (pilihanLogin == "2"):  # 👇 Jika pilihan adalah `2`
        # 👇 Menampilkan pesan sementara
        for x in range(0, 4):
            pesan = "Anda login sebagai guest" + " - " * x
            print(pesan, end="\r")
            time.sleep(0.5)
    elif (pilihanLogin == "3"):  # 👇 Jika pilihan adalah `3`
        return False
    else:  # 👇 Jika pilihan bukan 1, 2, dan 3
        print(warna.MERAH + "Pilihan tidak valid")
        return False

def main():
    welcome()
    auth()

main()