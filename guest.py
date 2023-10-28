from color import Color, BackgroundColor
import time

# 👇 Membuat class khusus untuk guest
class Guest:
    # 👇 Membuat constructor agar memanggil method welcome pertama kali
    def __init__(self):
        self.welcome()

    # 👇 Fungsi untuk membuat garis
    def garis(self):
        print("======================================================")

    # 👇 Fungsi untuk menampilkan pesan selamat datang
    def welcome(self):
        for x in range(0, 4):
                message = "Anda login sebagai guest" + "-" * x
                print(message, end="\r")
                time.sleep(0.5)
        print("")
        self.garis()
        print(Color.IJO + "             Berhasil Login sebagai Guest" + BackgroundColor.RESET)
        self.garis()