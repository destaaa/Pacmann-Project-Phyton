import pandas as pd
import random

# Menghasilkan id transaksi acak sepanjang 8 karakter
def generate_transaction_id():  
    transaction_id = random.randint(10000000, 99999999)
    return transaction_id

# Membuat class Transaction
class Transaction:
    # Menginisialisasi dictionary
    def __init__(self):
        '''
        Fungsi ini digunakan untuk menginisialisasi data_item sebagai dictionary yang akan menampung key_value yang meupakan daftar belanja
        '''
        self.data_item = dict()
        self.payment = 0

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
                print(f"{item_name} sudah ada dalam daftar")
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
                print(f"{item_name} tidak ada dalam daftar")
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
                print(f"Jumlah {item_name} telah diperbarui")
            else:
                print(f"{item_name} tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan tidak sesuai")

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
                print(f"Harga {item_name} telah diperbarui")
            else:
                print(f"{item_name} tidak ada dalam daftar")
        except ValueError:
            print("Data yang Anda masukkan tidak sesuai")

    # Menghapus daftar produk
    def delete_item(self):
        '''
        Fungsi ini digunakan untuk menghapus produk yang sudah ditambahkan sebelumnya,
        termasuk nama produk, jumlah dan harganya
        item_name       : str, nama produk yang ingin diganti
        '''
        item_name = input("Masukkan nama produk: ").capitalize()
        if item_name in self.data_item:
            self.data_item.pop(item_name)
            print(f"{item_name} sudah dihapus dari daftar")
        else:
            print(f"{item_name} tidak ada dalam daftar")

    # Melakukan check transaksi
    def check_order(self):
        '''
        Fungsi ini digunakan untuk menampilkan daftar belanja yang telah kita buat,
        termasuk nama produk, jumlah dan harganya
        '''
        if (len(self.data_item) == 0):
            print("Daftar belanja Anda kosong")
        else:
            data = pd.DataFrame.from_dict(self.data_item, orient='index', columns=['Jumlah Produk', 'Harga/item','Total Harga'])
            data['Total Harga'] = data['Jumlah Produk'] * data['Harga/item']
            data = data.reset_index().rename(columns={'index': 'Nama Produk'})
            data.index += 1
            data['No'] = range(1, len(data) + 1)
            data = data[['No', 'Nama Produk', 'Jumlah Produk', 'Harga/item', 'Total Harga']]
            headers = ["No", "Nama Produk", "Jumlah Produk", "Harga/item", "Total Harga"]
            aligns = ["center", "center", "right", "right", "right"]
            print(data.to_markdown(index=False, headers=headers, tablefmt="pipe", numalign="center", stralign=aligns))

            total_purchase = data['Total Harga'].sum()
            print(f"Total belanja Anda: {total_purchase}")

    # Mereset daftar transaksi
    def reset_transaction(self):
        '''
        Fungsi ini digunakan untuk mereset/menghapus seluruh daftar belanja
        '''
        self.data_item.clear()
        print("Daftar belanja telah dihapus")
        

    # Melihat total belanja dan diskon yang didapat serta pembayaran
    def total_payment(self):
        '''
        Fungsi ini digunakan untuk menghitung total belanja, diskon yang didapat dan harga setelah diskon serta memasukkan pembayaran dan kembalian yang didapat
        '''
        data = pd.DataFrame.from_dict(self.data_item, orient='index', columns=['Jumlah Produk', 'Harga/item','Total Harga'])
        data['Total Harga'] = data['Jumlah Produk'] * data['Harga/item']
        data = data.reset_index().rename(columns={'index': 'Nama Produk'})
        data.index += 1
        data['No'] = range(1, len(data) + 1)
        data = data[['No', 'Nama Produk', 'Jumlah Produk', 'Harga/item', 'Total Harga']]
        headers = ["No", "Nama Produk", "Jumlah Produk", "Harga/item", "Total Harga"]
        aligns = ["center", "center", "right", "right", "right"]
        print(data.to_markdown(index=False, headers=headers, tablefmt="pipe", numalign="center", stralign=aligns))
        total_purchase = sum([item[0] * item[1] for item in self.data_item.values()])
        if  total_purchase < 200000:
            self.total_payment = int(total_purchase * 1)
            print(f"Total belanja Anda: {total_purchase}")
        elif 200000 <= total_purchase < 300000:
            self.total_payment = int(total_purchase * 0.95)
            print(f"Total belanja Anda: {total_purchase}")
            print("Selamat! Anda mendapat diskon sebesar 5%")
            print(f"Total belanja Anda setelah diskon: {self.total_payment}")
        elif 300000 <= total_purchase < 500000:
            self.total_payment = int(total_purchase * 0.92)
            print(f"Total belanja Anda: {total_purchase}")
            print("Selamat! Anda mendapat diskon sebesar 8%")
            print(f"Total belanja Anda setelah diskon: {self.total_payment}")
        elif total_purchase >= 500000:
            self.total_payment = int(total_purchase * 0.9)
            print(f"Total belanja Anda: {total_purchase}")
            print("Selamat! Anda mendapat diskon sebesar 10%")
            print(f"Total belanja Anda setelah diskon: {self.total_payment}")
        while True:
            try:
                payment = int(input("Masukkan jumlah uang Anda: "))
                if payment < self.total_payment:
                    print("Jumlah uang yang Anda masukkan kurang")
                else:
                    change = payment - self.total_payment
                    self.change = change
                    print(f"Uang kembalian: {change}")
                    break
            except ValueError:
                print("Data yang Anda masukkan tidak sesuai")
       
