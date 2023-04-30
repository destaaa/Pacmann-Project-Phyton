from cashier import *
import datetime as dt

ban = ("""
================= /////////////////////////////////// =================

=================== SELAMAT DATANG DI SWALAYAN ANDI ===================
------------------------- Selamat Berbelanja --------------------------

================= .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. =================
""")
scr = ('''
            
========================== DAFTAR BELANJA ANDA ==========================           
''')

print(ban)

# Customer memasukkan ID
customer_name = input("Masukkan nama Anda: ").capitalize()
transaction_id = generate_transaction_id()
hari_ini = dt.date.today().strftime('%d-%m-%Y')

strip = ("""
---------------------------------------------------------------------
""")
print(strip)
print(f"Selamat datang {customer_name}!")
print(f"ID transaksi   :  {transaction_id}")
print(f"Tanggal        :  {hari_ini}")

# Membuat objek transaksi dengan trnsct_123
trnsct_123 = Transaction()

# Menampilkan menu utama
while True:
    print("\n1. Tambah produk")
    print("2. Perbarui produk")
    print("3. Perbarui jumlah produk")
    print("4. Perbarui harga produk")
    print("5. Hapus produk dari daftar")
    print("6. Cek daftar belanja ")
    print("7. Reset daftar belanja")
    print("8. Pembayaran")
    print("0. Keluar\n")

    # Memasukkan pilihan menu
    try:
        choice = int(input("Masukkan pilihan Anda : "))
    except ValueError:
        print("Data yang Anda tidak sesuai")
        continue

    if choice == 1:
        trnsct_123.add_item()

    elif choice == 2:
        trnsct_123.update_item_name()

    elif choice == 3:
        trnsct_123.update_item_qty()

    elif choice == 4:
        trnsct_123.update_item_price()

    elif choice == 5:
        trnsct_123.delete_item()

    elif choice == 6:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        trnsct_123.check_order()

    elif choice == 7:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        trnsct_123.reset_transaction()

    elif choice == 8:
        print(f"Nama Customer  :  {customer_name}")
        print(f"ID transaksi   :  {transaction_id}")
        print(f"Tanggal        :  {hari_ini}")
        print(scr)
        trnsct_123.total_payment()

    elif choice == 0:
        print("Terima kasih sudah berbelanja di Supermarket Andi 😊")
        break

    else:
        print("Menu tidak tersedia")
    
