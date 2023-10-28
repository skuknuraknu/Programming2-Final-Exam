# 👇 Membuat class `warna` untuk menyimpan data warna
class Color:
    BIRU = '\033[94m'  # Warna biru
    CYAN = '\033[96m'  # Warna cyan
    IJO = '\033[92m'   # Warna hijau
    KUNING = '\033[93m'  # Warna kuning
    MERAH = '\033[91m'  # Warna merah

# 👇 Membuat class `bgWarna` untuk menyimpan data warna background
class BackgroundColor:
    MERAH = '\x1b[5;30;47m'  # Warna latar belakang merah
    IJO   = '\x1b[5;30;42m'  # Warna latar belakang hijau
    RESET = '\x1b[0m'  # RESET berguna untuk mereset warna menjadi default
