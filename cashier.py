import pandas as pd
import random


# Menghasilkan id transaksi acak sepanjang 8 karakter
def generate_transaction_id():  
    transaction_id = random.randint(10000000, 99999999)
    return transaction_id


class Transaction:
    # Menginisialisasi dictionary
    def __init__(self):
        '''
        Fungsi ini digunakan untuk menginisialisasi data_item sebagai dictionary yang akan menampung key_value yang meupakan daftar belanja
        '''
        self.data_item = dict()

    # Menambahkan item produk
    def add_item(self):
        '''
        Fungsi ini digunakan untuk menambah item produk ke dalam dictonary yang telah kita buat sebelumnya
        item_name   : str, nama produk yang ingin kita tambahkan
        item_qty    : int, jumlah produk 
        item_price  : int, harga produk
        => item_name = key, item_qty & item_price = value
        '''
        try:    
            item_name = input("Masukkan nama produk: ").capitalize()
            if item_name in self.data_item:
                print("Produk sudah ada dalam daftar")
            else:
                item_qty = int(input("Masukkan jumlah produk: "))
                item_price = int(input("Masukkan harga produk: "))
                total_price = item_qty * item_price
                self.data_item.update({item_name: [item_qty, item_price, total_price]})
                print(f"{item_name} telah ditambahkan")
        except ValueError:
            print("Data yang Anda masukkan tidak sesuai")

    # Mengupdate nama produk
    def update_item_name(self):
        '''
        Fungsi ini digunakan untuk mengubah nama produk yang sudah ditambahkan sebelumnya
        item_name       : str, nama produk yang ingin diganti
        new_item_name   : str, nama produk yang baru
        '''
        try:
            item_name = input("Masukkan nama produk yang ingin diupdate: ").capitalize()
            if item_name in self.data_item:
                new_item_name = input("Masukkan nama produk baru: ").capitalize()
                self.data_item[new_item_name] = self.data_item.pop(item_name)
                print(f"{item_name} telah diupdate menjadi {new_item_name}")
            else:
                print("Produk tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan salah")

    # Mengupdate jumlah produk
    def update_item_qty(self):
        '''
        Fungsi ini digunakan untuk mengubah jumlah produk yang sudah ditambahkan sebelumnya
        item_name       : str, nama produk yang ingin diganti jumlahnya
        new_item_qty    : str, jumlah produk yang baru
        '''
        try:
            item_name = input("Masukkan nama produk: ")
            item_name = item_name.capitalize()
            if item_name in self.data_item:
                new_item_qty = int(input("Masukkan jumlah produk baru: "))
                self.data_item[item_name][0] = new_item_qty
                print("Jumlah produk telah diperbarui")
            else:
                print("Produk tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan salah")

    # Mengupdate harga produk
    def update_item_price(self):
        '''
        Fungsi ini digunakan untuk mengubah harga produk yang sudah ditambahkan sebelumnya
        item_name       : str, nama produk yang ingin diganti harganya
        new_item_price  : str, harga produk yang baru
        '''
        try:
            item_name = input("Masukkan nama produk: ")
            item_name = item_name.capitalize()
            if item_name in self.data_item:
                new_item_price = int(input("Masukkan harga produk baru: "))
                self.data_item[item_name][1] = new_item_price
                print("Harga produk telah diperbarui")
            else:
                print("Produk tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan salah")

    # Menghapus daftar produk
    def delete_item(self):
        '''
        Fungsi ini digunakan untuk menghapus produk yang sudah ditambahkan sebelumnya,
        termasuk nama produk, jumlah dan harganya
        item_name       : str, nama produk yang ingin diganti
        '''
        try:
            item_name = input("Masukkan nama produk: ").capitalize()
            if item_name in self.data_item:
                self.data_item.pop(item_name)
                print("Produk sudah dihapus dari daftar")
            else:
                print("Produk tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan salah")

    # Melakukan check transaksi
    def check_order(self):
        '''
        Fungsi ini digunakan untuk menampilkan daftar belanja yang telah kita buat,
        termasuk nama produk, jumlah dan harganya
        '''
        if (len(self.data_item) == 0):
            print("Daftar belanja Anda kosong")
        else:
            data = pd.DataFrame(self.data_item).T
            data.columns = ['Jumlah Item', 'Harga/item', 'Total Harga']
            print(data.to_markdown())

    # Mereset daftar transaksi
    def reset_list(self):
        '''
        Fungsi ini digunakan untuk mereset/menghapus seluruh daftar belanja
        '''
        self.data_item.clear()
        print("Daftar belanja telah dihapus")

    # Melihat total belanja dan diskon yang didapat
    def total_purchase(self):
        '''
        Fungsi ini digunakan untuk menghitung total belanja, diskon yang didapat serta harga setelah diskon
        '''
        total_purchase = sum([item[0] * item[1] for item in self.data_item.values()])
        if  total_purchase < 200000:
            self.total_payment = int(total_purchase * 1)
            print(f"Total belanja Anda: {total_purchase}")
        elif 200000 <= total_purchase < 300000:
            self.total_payment = int(total_purchase * 0.95)
            print("Selamat! Anda mendapat diskon sebesar 5%")
            print(f"Total belanja Anda: {total_purchase}")
            print(f"Total pembayaran Anda setelah diskon: {self.total_payment}")
        elif 300000 <= total_purchase < 500000:
            self.total_payment = int(total_purchase * 0.92)
            print("Selamat! Anda mendapat diskon sebesar 8%")
            print(f"Total belanja Anda: {total_purchase}")
            print(f"Total pembayaran Anda setelah diskon: {self.total_payment}")
        elif total_purchase >= 500000:
            self.total_payment = int(total_purchase * 0.9)
            print("Selamat! Anda mendapat diskon sebesar 10%")
            print(f"Total belanja Anda: {total_purchase}")
            print(f"Total pembayaran Anda setelah diskon: {self.total_payment}")
    

    def pay_checkout(self):
        '''
        Fungsi ini digunakan untuk memasukkan pembayaran dan kembalian yang didapat
        '''
        try:
            bill = int(input("Masukkan jumlah uang Anda: "))
            payment = bill - self.total_payment
        except ValueError:
            print("Data yang Anda masukkan salah")
        if payment < 0:
            print("Jumlah uang yang Anda masukkan kurang")
        else:
            self.payment_amount = payment
            print(f"Uang kembalian: {payment}")
