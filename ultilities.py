import json
from color import Color, BackgroundColor
import locale

class Utilities:
    # 👇 Constructor untuk class Utilities
    def __init__(self, file_path):
        self.file_path = file_path

    # 👇 Fungsi untuk membuat garis
    def garis(self):
        print("======================================================")
  
    # 👇 Membaca file json
    def read_products_json(self):
        # 👇 membaca file json
        with open(self.file_path, 'r') as products_file:
            product_lists = json.load(products_file)
        # mengembalikan nilai berupa dictionary dari file json
        return product_lists

    # 👇 Menambahkan produk baru ke dalam file json
    def add_product_to_json(self, new_product):
        # 👇 Membaca file json dari method `read_products_json`
        product_lists = self.read_products_json()
        # 👇 Menambahkan data produk baru ke dalam dictionary
        product_lists['products'].append(new_product)
        # 👇 Mengupdate file json
        with open(self.file_path, 'w') as products_file:
            json.dump( product_lists, products_file, indent=4 )  # indent untuk mempercantik tampilan json
        self.garis()
        print(f"{BackgroundColor.BIRU_GELAP}     Produk dengan id {new_product['id']} berhasil ditambahkan      {BackgroundColor.RESET}")
        self.garis()
        return True
    
    # 👇 Menghapus produk berdasarkan key/id
    def del_product(self, key):
        # 👇 Membaca file json dari method `read_products_json`
        product_lists = self.read_products_json()
        # 👇 Melakukan perulangan untuk mencari produk yang akan dihapus
        for product in product_lists['products']:
            if product['id'] == key: # Jika id produk sama dengan key yang diberikan
                product_lists['products'].remove(product)
                self.garis()
                print(f"{BackgroundColor.BIRU_GELAP}       Produk dengan id {key} berhasil dihapus        {BackgroundColor.RESET}")
                self.garis()
                # 👇 mengupdate file json
                with open(self.file_path, 'w') as products_file:
                    json.dump(product_lists, products_file, indent=4)  # indent untuk mempercantik tampilan json
                return True # Mengakhiri perulangan
        # 👇 Jika produk dengan key yang diberikan tidak ditemukan
        print(f"Produk dengan id {key} tidak ditemukan")
        return False
  
    # 👇 Mengupdate produk berdasarkan key/id
    def update_product(self, key, new_product):
        # 👇 Membaca file json dari method `read_products_json`
        product_lists = self.read_products_json()
        # 👇 Melakukan perulangan untuk mencari produk yang akan dihapus
        for product in product_lists['products']:
            if product['id'] == key: # Jika id produk sama dengan key yang diberikan
                # 👇 Menghapus produk lama
                product_lists['products'].remove(product)
                # 👇 Membuat produk baru
                updated_product = { 
                    'id': key, 
                    'name': new_product['name'], 
                    'price': new_product['price'],
                    'stock': new_product['stock']}
                # 👇 Menambahkan produk baru ke dalam `dictionary`
                product_lists['products'].append(updated_product)
                # 👇 mengupdate file json
                with open(self.file_path, 'w') as products_file:
                    json.dump(product_lists, products_file, indent=4)  # indent untuk mempercantik tampilan json
                self.garis()
                print(f"{BackgroundColor.BIRU_GELAP}       Produk dengan id {key} berhasil diupdate       {BackgroundColor.RESET}")
                self.garis()
                return True
        # Jika produk dengan key yang diberikan tidak ditemukan
        print(f"Produk dengan id {key} tidak ditemukan")
        return False
    
    def filter_product(self, name):
        # 👇 Membaca file json dari method `read_products_json`
        product_lists     = self.read_products_json()
        filtered_products = [] 
        # 👇 Melakukan perulangan untuk mencari produk mirip dengan nama yang diberikan
        for product in product_lists['products']:
            if name in product['name']:
                filtered_products.append(product)
        return filtered_products

